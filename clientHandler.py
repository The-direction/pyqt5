from threading import Thread
from PyQt5 import QtCore
from PyQt5.QtWidgets import *
import os
import sys
import re
import signal

# 客户端处理类


class Client_handler:
    def __init__(self, sockfd):
        self.s = sockfd

    def login(self, userinfo):
        self.userlist = userinfo
        username = userinfo[0]
        password = userinfo[1]
        data = 'L ' + username + ' ' + password
        # 发送登录请求
        self.s.send(data.encode())
        # 接收服务端消息
        data = self.s.recv(1024).decode()
        if data == 'login':
            # 允许登录显示正在登录界面
            return True
        else:
            # 密码或者用户名错误，回到客户端打开界面
            return data

    def register(self, registinfo):
        # 确认密码输入正确
        self.registinfo = registinfo
        username = registinfo[0]
        password_1 = registinfo[1]
        password_2 = registinfo[2]
        # phonenum = input('phonenum >>')
        # 正则判定
        # 姓名密码判定
        if not (re.findall(r'^\w+$', username) and re.findall(r'^\w+$', password_1)):
            return '用户名或密码格式不正确'
        # 手机号判定
        # if not re.findall(r'[0-9]{11}', phonenum):
        #     print('手机号不正确')
        #     continue
        # 两次密码确认
        if password_1 != password_2:
            return '两次输入密码不同'
        data = 'R ' + username + ' ' + password_1
        # 发送注册请求
        self.s.send(data.encode())
        # 接受客户端消息
        data = self.s.recv(1024).decode()
        if data == 'register':
            # 允许注册
            return True
        else:
            # 用户名已存在
            return data

    def exit(self):
        self.s.send(b'E')
        sys.exit('客户端退出')

#     def chatroom(self):
#         print('来到聊天室')
#         self.s.send(b'OK all')
#         # 创建进程接受消息
#         pid = os.fork()
#         signal.signal(signal.SIGCHLD, signal.SIG_IGN)
#         if pid == 0:
#             pressed = QtCore.pyqtSignal()
#             while 1:
#                 data = self.s.recv(1024)
#                 if data:

#                     def display(data):
#                         self.chat_page.textBrowser.append(
#                             (data).decode('utf-8'))

#                     QtCore.QObject.connect(self, QtCore.SIGNAL(
#                         "pressed()"), self.display(data))

#                     print('\n---------------')
#                     print(data.decode())
#         else:
#             room = Chatthread(self.s, pid, chat_page)

    # def friendlist(self):
    #     self.s.send(b'friendlist')
    #     data = self.s.recv(1024).decode()
    #     friend_L = re.split(r'\W', data)
    #     friend_L.pop(0)
    #     self.p.num = 6
    #     chat_object = self.p.match(friend_L)
    #     self.object_chatroom(chat_object)
    #     # 显示好友列表

#     def object_chatroom(self, chat_object, chat_page):
#         self.chat_page = chat_page
#         self.s.send(b'OK one')
#         # 创建进程接受消息
#         pid = os.fork()
#         signal.signal(signal.SIGCHLD, signal.SIG_IGN)
#         if pid == 0:
#             while 1:
#                 data = self.s.recv(1024)
#                 if data:
#                     print('\n---------------')
#                     print(data.decode())
#         else:
#             room = Chatthread(self.s, pid, self.chat_page, chat_object)


# class Chatthread(Thread):
#     def __init__(self, s, childpid, chat_page, object=None):
#         self.s = s
#         self.childpid = childpid
#         self.chat_page = chat_page
#         if object:
#             self.object = object
#             self.chatone()
#         else:
#             self.conn()

#     def __del__(self):
#         print('退出聊天室')
#         os.kill(self.childpid, signal.SIGKILL)

#     def chat(self):
#         # print('222222222222222')
#         data = self.chat_page.textEdit.toPlainText()
#         self.chat_page.textEdit.clear()
#         print(data)
#         if data == 'exit':
#             self.s.send(b'exit')
#         else:
#             self.s.send(self.data.encode())

#     def chatone(self):
#         while 1:
#             data = input()
#             if data == 'exit':
#                 self.s.send(b'exit')
#                 break
#             data = self.object + '#' + data
#             self.s.send(data.encode())
