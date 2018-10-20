# -*- coding: utf-8 -*-

import socket
from PyQt5 import QtCore

class Thread1(QtCore.QThread):
    pressed=QtCore.pyqtSignal()
    released=QtCore.pyqtSignal()
    def __init__(self):
        super(Thread1, self).__init__()

        self.message=""
        self.Host = "localhost"
        self.Port = 4959
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)        #新建socket
        self.s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
        self.s.bind((self.Host,self.Port))   #socket绑定该主机的ip和端口
        self.s.listen(5)
        
    def run(self):
        self.s.listen(5)
        self.con,self.addr = self.s.accept()
        
        while 1:
           # msg,(addr,port) = s.recvfrom(100)    # 接受数据
            msg = self.con.recv(1024)
            if msg !="":
                self.message=msg
                print(msg)
                self.pressed.emit()
            else:
                self.message=self.message
    def sendMsg(self, textMsg):
        self.con.send(textMsg)
        
        
        
        
        
