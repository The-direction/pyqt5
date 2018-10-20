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
            sys.exit('连接错误', e)
        print('已连接到服务端')
        self.run()

    def run(self):
        print('客户端启动')
