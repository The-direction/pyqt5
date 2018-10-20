from PyQt5.QtCore import QObject, pyqtSignal

class QTypeSignal(QObject):

    msg = pyqtSignal(object)

    def __init__(self):
        super().__init__()

    def run(self):
        self.msg.emit('hello pyqt5')

class QTypeSlot(QObject):
    def __init__(self):
        super().__init__()

    def get(self,msg):
        print(msg)

send = QTypeSignal()
recv = QTypeSlot()

send.msg.connect(recv.get)
send.run()                        