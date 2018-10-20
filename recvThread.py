# -*- coding: utf-8 -*-

from PyQt5 import QtCore


class myThread(QtCore.QThread):
    pressed = QtCore.pyqtSignal(str)

    def __init__(self, s):
        super(myThread, self).__init__()
        self.s = s
        self.message = ""

    def run(self):
        while 1:
            msg = self.s.recv(1024)
            if msg:
                self.message = msg.decode()
                print(msg)
                self.pressed.emit(self.message)
