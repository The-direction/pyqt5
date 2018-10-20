# from threading import Thread
# # from lanse import MyMainWindow


# class Chatthread(Thread):
#     def __init__(self, target, args=(), kwargs={}):
#         super().__init__()
#         self.target = target
#         self.args = args
#         self.s = self.args[0]

#     def run(self):
#         print("欢迎来到群组聊天室")
#         self.s.send(b'OK all')
#         self.target(*self.args)


from PyQt5.QtCore import *


class F_thread(QThread):
    friendlist_recv = pyqtSignal(bytes)

    def __init__(self, s):
        super().__init__()
        self.s = s
        print("线程收消息")

    def run(self):
        self.s.send(b"friendlist")
        while 1:
            data = self.s.recv(2014)
            if data:
                print('=======')
                self.friendlist_recv.emit(data)
                print(data)
                break
