#!/usr/bin/env python3
# coding=utf-8

'''
name : Zhou
data : 2018-9-28
email : 18871778583@163.com
modules : python3.5 os
This is a chatroom client for AID1807
'''
from socket import *
from threading import Thread
import os
import sys
import re
import signal

HOST = '127.0.0.1'
PORT = 8000
ADDR = (HOST, PORT)


# 创建客户端类
class Client:
    def __init__(self, ADDR):
        self.ADDR = ADDR
        # 创建套接字　
        self.sockfd = socket()
        # 发起连接
        try:
            self.sockfd.connect(ADDR)
        except Exception as e:
            sys.exit('连接错误',e)
        print('已连接到服务端')
        self.run()

    def run(self):
        print('客户端启动')
        # 处理客户端请求
        # try:
        #     chd = Client_handler(self.sockfd)
        # except KeyboardInterrupt:
        #     self.sockfd.send(b'exit')
        #     sys.exit('客户端推出')
        # except Exception as e:
        #     print('error', e)

        # try:
        #     while 1:
        #         data = input('请输入>>')
        #         self.sockfd.sendall(data.encode())
        #         print(self.sockfd.recv(1024).decode())
        # except KeyboardInterrupt:
        #     sys.exit('客户端退出')
        # except Exception:
        #     print('Error!!!')




# 客户端处理类
class Client_handler:
    def __init__(self, sockfd):
        self.s = sockfd
    #     self.run()

    # def run(self):
    #     # 选择功能函数处理请求
    #     while 1:
    #         option = self.p.num
    #         if option == 1:
    #             self.login()
    #         elif option == 2:
    #             self.register()
    #         elif option == 3:
    #             self.exit()
    #         elif option == 5:
    #             self.p.match()
    #         elif option == 22:
    #             self.chatroom()
    #         elif option == 11:
    #             print('显示好友列表')
    #             self.friendlist()
    #         else:
    #             print('===重新输入===')
    #             self.p.num = 0
    #             self.p.match()

    def login(self):
        username = input('username >>')
        password = input('password >>')
        data = 'L ' + username + ' ' + password
        # 发送登录请求
        self.s.send(data.encode())
        # 接收服务端消息
        data = self.s.recv(1024).decode()
        if data == 'login':
            # 允许登录显示正在登录界面
            self.p.num = 4
            self.p.match()
        else:
            print(data)
            # 密码或者用户名错误，回到客户端打开界面
            self.p.num = 0
            self.p.match()
            self.run()

    def register(self):
        # 确认密码输入正确
        while 1:
            username = input('username >>')
            password_1 = input('password >>')
            password_2 = input('password >>')
            phonenum = input('phonenum >>')
            # 正则判定
            # 姓名密码判定
            if not (re.findall(r'^\w+$', username) and re.findall(r'^\w+$', password_1)):
                print('用户名或密码格式不正确')
                continue
            # 手机号判定
            if not re.findall(r'[0-9]{11}', phonenum):
                print('手机号不正确')
                continue
            # 两次密码确认
            if password_1 == password_2:
                break
            else:
                print('两次输入密码不同')
        data = 'R ' + username + ' ' + password_1 + ' ' + phonenum
        # 发送注册请求
        self.s.send(data.encode())
        # 接受客户端消息
        data = self.s.recv(1024).decode()
        if data == 'register':
            # 允许注册
            self.p.num = 4
            self.p.match()
        else:
            print(data)
            # 用户名已存在,回到客户端打开界面
            self.p.num = 0
            self.p.match()
            self.run()

    def exit(self):
        self.s.send(b'E')
        sys.exit()

    def chatroom(self):
        self.s.send(b'OK all')
        # 创建进程接受消息
        pid = os.fork()
        signal.signal(signal.SIGCHLD,signal.SIG_IGN)
        if pid == 0:
            while 1:
                data = self.s.recv(1024)
                if data:
                    print('\n---------------')
                    print(data.decode())
        else:
            room = Chatthread(self.s)
            print('出现选择界面')
            self.p.num = 5

    def friendlist(self):
        self.s.send(b'friendlist')
        data = self.s.recv(1024).decode()
        friend_L = re.split(r'\W', data)
        friend_L.pop(0)
        self.p.num = 6
        chat_object = self.p.match(friend_L)
        self.object_chatroom(chat_object)
        # 显示好友列表

    def object_chatroom(self,chat_object):
        self.s.send(b'OK one')
        # 创建进程接受消息
        pid = os.fork()
        signal.signal(signal.SIGCHLD,signal.SIG_IGN)
        if pid == 0:
            while 1:
                data = self.s.recv(1024)
                if data:
                    print('\n---------------')
                    print(data.decode())
        else:
            room = Chatthread(self.s, pid, chat_object)
            print('出现选择界面')
            self.p.num = 5


# 显示界面
# handler_0客户端打开界面
# handler_1登录界面
# handler_2注册界面
# handler_3退出界面
# handler_4正在登录界面
# handler_5主页面
# handler_6好友列表


class Chatthread(Thread):
    def __init__(self, s, childpid, object=None):
        self.s = s
        self.childpid = childpid        
        if object:
            self.object = object
            self.chatone()
        else:
            self.chat()

    def __del__(self):
        print('退出聊天室')
        os.kill(self.childpid,signal.SIGKILL)

    def chat(self):
        while 1:
            data = input()
            if data == 'exit':
                self.s.send(b'exit')
                break
            self.s.send(data.encode())

    def chatone(self):
        while 1:
            data = input()
            if data == 'exit':
                self.s.send(b'exit')
                break
            data = self.object + '#' + data
            self.s.send(data.encode())




# class Client_handler:
#     def __init__(self,sockfd):
#         self.s = sockfd
#         self.run()

#     def run(self):
#         print('show')

# class Page:
#     def __init__(self, num):
#         self.num = num

#     def match(self, friend_L=[]):
#         if self.num == 0:
#             self.handler_0()
#         elif self.num == 1:
#             self.handler_1()
#         elif self.num == 2:
#             self.handler_2()
#         elif self.num == 3:
#             self.handler_3()
#         elif self.num == 4:
#             self.handler_4()
#         elif self.num == 5:
#             self.handler_5()
#         elif self.num == 6:
#             return self.handler_6(friend_L)

#     def handler_0(self):
#         print('''
# +-----------------------+
# |                       |
# |       1.login         |
# |       2.register      |
# |       3.exit          |
# |                       |
# +-----------------------+''')
#         answer = input('请输入选项>>\n')
#         self.num = int(answer)
#         self.match()

#     def handler_1(self):
#         print('''
# +-----------------------+
# | Login                 |
# |       username        |
# |                       |
# |       password        |
# |                       |
# +-----------------------+''')

#     def handler_2(self):
#         print('''
# +------------------------+
# |Register                |
# |       username         |
# |                        |
# |       password         |
# |       password         |
# |       phonenum         |
# |                        |
# +------------------------+''')

#     def handler_3(self):
#         print('''
# +--------------+
# |   正在注销   |
# +--------------+
#             ''')

#     def handler_4(self):
#         print('''
# +----------------------+
# |    正在登录....      |
# +----------------------+''')
#         # 跳转主页面
#         self.num = 5
#         self.match()

#     def handler_5(self):
#         print('''
# +-------------------------------+
# |                               |
# |                               |
# |           22.群聊             |
# |         11.好友列表           |
# |                               |
# |                               |
# +-------------------------------+
#             ''')
#         answer = input('请输入选项>>')
#         self.num = int(answer)

#     def handler_6(self, friend_L):
#         print('+-------------------------------+')
#         print('|                               |')
#         for name in friend_L:
#             print('|'+name.center(32)+'|')
#         print('|                               |')
#         print('+-------------------------------+')
#         s = input('选择聊天对象>>')
#         return s


if __name__ == '__main__':
    client = Client(ADDR)
