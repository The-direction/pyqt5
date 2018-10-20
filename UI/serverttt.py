import socket
import time
from PyQt5 import QtCore, QtGui, QtWidgets
from Thread1 import Thread1
from PyQt5.QtWidgets import *
import sys
from lanse import Ui_MainWindow

class ServerWidget(QMainWindow, Ui_MainWindow):

    def __init__(self, parent = None):
             
        QWidget.__init__(self, parent)
        self.setupUi(self)
        self.th = Thread1()
        self.th.start()
        
       
        
        # QtCore.QObject.connect(self.th, QtCore.SIGNAL("pressed()"), self.display)
        self.pushButton.clicked.connect(self.sendMsg)
        
    def sendMsg(self):
        text = self.textEdit.toPlainText()
        ch =str(text) #!!!注意，如果不进行"str()"这一步字符转换，则接收端只能显示第一个字符
        name ="花无缺～(26534487)       "  #不进行编码处理，中文是乱码
        nowtime = time.strftime('%H：%M：%S')
        header =name+nowtime+'\n'
        text=header+ch+'\n'
        self.textBrowser.setStyleSheet("color: rgb(126, 12, 120);")
        self.textBrowser.append(text)
        self.th.sendMsg(text.encode())
        #self.s.send(ch)     #将 'text’ 发送给对方
        
        self.textEdit.setText("")
        
    def display(self):
        
        self.textBrowser.append((self.th.message).decode('utf-8') ) #这时append比setText好用了
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWin = ServerWidget()
    myWin.show()
    sys.exit(app.exec_())