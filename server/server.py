#!/usr/bin/env python3
# coding=utf-8

'''
name : Zhou
data : 2018-9-28
email : 18871778583@163.com
modules : python3.5 pymysql re
This is a chatroom server for AID1807
'''
from socket import *
from pymysql import *
from threading import Thread
import sys
import re
import time


# 设置本地服务器监听端口
HOST = '0.0.0.0'
PORT = 8000
ADDR = (HOST, PORT)
# 客户端套接字列表
# rlist = []
# 客户端套接字－－－用户名
userdict = {}

# 创建Server类


class Server:
    def __init__(self, ADDR):
        self.ADDR = ADDR
        # 设置监听套接字
        self.sockfd = socket()
        # 设置端口立即释放
        self.sockfd.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        # 绑定本地地址和端口
        self.sockfd.bind(self.ADDR)
        # 设置监听
        self.sockfd.listen(5)
        self.run()

    def run(self):
        print('启动服务端....')
        while 1:
            try:
                # 等待连接
                c, addr = self.sockfd.accept()
                print('服务端等待连接...=====')
            except KeyboardInterrupt:
                self.sockfd.close()
                sys.exit('服务端退出')
            except Exception:
                print('连接错误')
                continue
            # 调用连接请求处理函数
            self.accept_handler(c)

    def accept_handler(self, c):
        # rlist.append(c)
        mth = Mythread_handler(c)
        t = Mythread(target=mth.handler, args=(c,))
        t.start()


# 重写线程类,重写__init__和run函数
class Mythread(Thread):
    def __init__(self, target, args=(), kwargs={}):
        self.target = target
        self.args = args
        self.kwargs = kwargs
        # 继承Thread的__init__函数
        super().__init__()
        # 分支线程随主线程退出而退出
        self.setDaemon(True)

    def __del__(self):
        print('退出--->> ', self.name)
        self.args[0].close()

    def run(self):
        print('这是分支线程:', self.name)
        # 调用Mythread_handler类中handler函数
        self.target()


# 封装,创建线程处理类
class Mythread_handler:
    def __init__(self, c):
        self.c = c
        self.username = ''

    def __del__(self):
        print('客户端退出')
        # 从客户端套接字列表中去掉已退出的套接字
        # rlist.remove(self.c)
        self.exit_record()

    def handler(self):
        print('服务端处理函数')
        print('========Connect from', self.c.getpeername(), '========')
        while 1:
            data = self.c.recv(1024).decode()
            print(data)
            # 正则判定
            L = re.split(r'[ ]+', data)
            option = L[0]
            # 根据请求的首字母选择功能函数
            try:
                if option == 'L':
                    self.login(L)
                elif option == 'R':
                    self.register(L)
                elif option == 'E':
                    print('exit--->> ', self.c.getpeername())
                    # 结束线程
                    return
                else:
                    self.c.send(b'===error===')
            except MyException:
                # 捕获代表操作成功的异常,结束请求处理循环
                print('开始聊天')
                break
            except BrokenPipeError:
                # 结束线程
                break

        # 发送聊天确认信息
        while 1:
            time.sleep(1)
            print("等候选择聊天对象")
            data = self.c.recv(1024)
            if data == b'OK all':
                self.chatroom()
            if data == b'OK one':
                self.chatone()
            elif data == b'friendlist':
                print('好友列表')
                self.find_friend()
            if data == b'E' or data == b'exit':
                # 结束线程
                break

    # 显示好友列表
    def find_friend(self):
        with open('../friendlist.txt', 'rt') as f:
            for line in f:
                print(line)
                if self.username in re.findall(r'^\w+', line):
                    #　发送好友列表
                    self.c.send(line.encode())

    # 单人聊天
    def chatone(self):
        try:
            while 1:
                data = self.c.recv(1024).decode()
                print('-----', data, '-------')
                if re.findall(r'^\w+$', data) == ['exit']:
                    break
                name = re.findall(r'^\w+\#', data)[0]
                n = len(name)
                data = data[n:]
                objname = name[:-1]
                userdict[objname].send(data.encode())
        except BrokenPipeError:
            pass

    # 多人聊天室
    def chatroom(self):
        while 1:
            try:
                data = self.c.recv(1024)
                if re.findall(r'^\w+$', data.decode()) == ['exit']:
                    print("退出聊天室")
                    break
                data = self.username.encode() + b' : '+data
                print(data.decode())
                for conndf in userdict.values():
                    conndf.send(data)
            except BrokenPipeError:
                break

    def register(self, L):
        try:
            with open('../userinformation.txt', 'rt') as f:
                for line in f:
                    l = re.split(r'[ ]+', line)
                    # 查看用户名是否已存在
                    if l[0] == L[1]:
                        self.c.send('用户已存在'.encode())
                        break
                else:
                    self.c.send(b'register')
                    print('正在注册')
                    raise MyException
        except MyException:
            # 保存信息记录
            with open('../userinformation.txt', 'at') as f:
                s = ' '.join(L[1:])
                s += ' ' + time.ctime()
                f.write(s + '\n')
        except Exception as e:
            print('打开文件失败', e)

    def login(self, L):
        try:
            with open('../userinformation.txt', 'rt') as f:
                for line in f:
                    l = re.split(r'[ ]+', line)
                    if L[1] == l[0]:  # 匹配姓名
                        if L[2] == l[1]:  # 匹配密码
                            # 判断用户是否已登录
                            for name in userdict:
                                if name == L[1]:
                                    self.c.send('用户已登录'.encode())
                                    break
                            else:
                                self.c.send(b'login')
                                print('正在登录...')
                                # 登录成功，抛出自定义异常
                                self.login_record(L[1])
                                raise MyException
                            break
                        else:
                            self.c.send('密码错误'.encode())
                            break
                else:
                    print('==================================')
                    self.c.send('用户不存在'.encode())
        except MyException:
            raise MyException
        except Exception as e:
            print('打开文件失败', e)

    def login_record(self, username):
        self.username = username
        # 在已登录字典中添加username和套接字
        userdict[self.username] = self.c
        with open('../records.txt', 'at') as f:
            s = username + ' login ' + time.ctime()
            f.write(s + '\n')

    def exit_record(self):
        if self.username:
            # 在登录字典中去掉username和它的套接字
            del userdict[self.username]
            with open('../records.txt', 'at') as f:
                s = self.username + ' exit ' + time.ctime()
                f.write(s + '\n')


# 定义一个异常类，用来传递操作成功的消息
class MyException(Exception):
    def __init__(self):
        Exception.__init__(self)

        # 创建IO多路复用


if __name__ == '__main__':
    server = Server(ADDR)
