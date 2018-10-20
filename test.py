#!/usr/bin/env python3
# coding=utf-8


from demo import *
from clientMain import Client
from clientHandler import Client_handler
import sys
import signal



try:
    # 创建客户端
    client = Client(ADDR)
    # 处理客户端
    c_handler = Client_handler(client.sockfd)
except Exception as e:
    print('error', e)


# def func(sig, frame):
#     if sig == signal.SIGINT:
#         c_handler.exit()


# signal.signal(signal.SIGINT, func)

app = QApplication(sys.argv)
demo = Demo(c_handler)
demo.show()

sys.exit(app.exec_())