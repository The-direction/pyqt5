import socket
import time
from PyQt5 import QtCore, QtGui, QtWidgets
from Thread2 import Thread2
from PyQt5.QtWidgets import *
import sys
from lanse import Ui_MainWindow

class ClientWidget(QMainWindow, Ui_MainWindow):

    def __init__(self, parent = None):

        QWidget.__init__(self, parent)
        self.setupUi(self)
        
        
        self.Host="localhost"
        self.Port = 4959
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)        #新建socket
        self.s.connect((self.Host,self.Port))
        
        self.th = Thread2(self.s)
        self.th.start()
        
        # QtCore.QObject.connect(self.th, QtCore.SIGNAL("pressed()"), self.display)
        self.pushButton.clicked.connect(self.sendMsg)

    def sendMsg(self):
        text = self.textEdit.toPlainText()
        ch =str(text) 
        name ="小鱼儿～(496577309)       "  
        nowtime = time.strftime('%H：%M：%S')
        header =name+nowtime+'\n'
        text=header+ch+'\n'
        self.textBrowser.setStyleSheet("color: rgb(126, 210, 120);")
        self.textBrowser.append(text)
        self.s.send(text.encode())
        #self.s.send(ch)     #将 'text’ 发送给对方
        
        self.textEdit.setText("")
    def display(self):
        self.textBrowser.append((self.th.message).decode('utf-8') ) #这时append比setText好用了   
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWin = ClientWidget()
    myWin.show()
    sys.exit(app.exec_())
