#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'lanse.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtWidgets import *
from recvThread import myThread

# import 1369025_165540642000_2_rc


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(581, 424)
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setAcceptDrops(False)
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setStyleSheet(
            "#centralwidget{background-image: url(:bgpic3.jpg);}")
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-30, -60, 641, 531))
        self.label.setAcceptDrops(False)
        self.label.setAutoFillBackground(False)
        # self.label.setStyleSheet("\n"
        #                          "background-image: url(:bgpic3.jpg);")
        self.label.setFrameShape(QtWidgets.QFrame.Box)
        self.label.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label.setText("")
        self.label.setTextFormat(QtCore.Qt.PlainText)
        self.label.setObjectName("label")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(0, 280, 391, 78))
        self.textEdit.setMouseTracking(False)
        self.textEdit.setStyleSheet("background-color: rgb(219, 239, 255);")
        self.textEdit.setFrameShape(QtWidgets.QFrame.Panel)
        self.textEdit.setObjectName("textEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(320, 370, 61, 21))
        self.pushButton.setAutoFillBackground(False)
        self.pushButton.setStyleSheet("background-color: rgb(170, 170, 170);")
        self.pushButton.setCheckable(False)
        self.pushButton.setAutoRepeat(False)
        self.pushButton.setFlat(False)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(90, 250, 71, 21))
        self.pushButton_2.setAutoFillBackground(False)
        self.pushButton_2.setStyleSheet(
            "background-color: rgb(170, 170, 170);")
        self.pushButton_2.setAutoDefault(False)
        self.pushButton_2.setDefault(False)
        self.pushButton_2.setFlat(False)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(10, 250, 41, 21))
        self.pushButton_3.setAutoFillBackground(False)
        self.pushButton_3.setStyleSheet(
            "background-color: rgb(170, 170, 170);")
        self.pushButton_3.setFlat(False)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(10, 370, 61, 21))
        self.pushButton_4.setAutoFillBackground(False)
        self.pushButton_4.setStyleSheet("background-color: rgb(170, 170, 170);\n"
                                        "border-bottom-color: rgb(182, 182, 182);")
        self.pushButton_4.setFlat(False)
        self.pushButton_4.setObjectName("pushButton_4")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setEnabled(True)
        self.textBrowser.setGeometry(QtCore.QRect(0, 10, 391, 231))
        self.textBrowser.setMouseTracking(False)
        self.textBrowser.setAcceptDrops(True)
        self.textBrowser.setToolTipDuration(-1)
        self.textBrowser.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.textBrowser.setAutoFillBackground(False)
        self.textBrowser.setStyleSheet("background-color: rgb(219, 239, 255);")
        self.textBrowser.setFrameShape(QtWidgets.QFrame.Panel)
        self.textBrowser.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.textBrowser.setLineWidth(-1)
        self.textBrowser.setMidLineWidth(0)
        self.textBrowser.setVerticalScrollBarPolicy(
            QtCore.Qt.ScrollBarAsNeeded)
        self.textBrowser.setHorizontalScrollBarPolicy(
            QtCore.Qt.ScrollBarAsNeeded)
        self.textBrowser.setSizeAdjustPolicy(
            QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.textBrowser.setTabChangesFocus(False)
        self.textBrowser.setUndoRedoEnabled(False)
        self.textBrowser.setLineWrapMode(QtWidgets.QTextEdit.WidgetWidth)
        self.textBrowser.setOverwriteMode(False)
        self.textBrowser.setAcceptRichText(True)
        self.textBrowser.setOpenLinks(True)
        self.textBrowser.setObjectName("textBrowser")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(280, 250, 99, 21))
        self.pushButton_5.setAutoFillBackground(False)
        self.pushButton_5.setStyleSheet(
            "background-color: rgb(170, 170, 170);")
        self.pushButton_5.setFlat(False)
        self.pushButton_5.setObjectName("pushButton_5")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(400, 10, 181, 401))
        self.listWidget.setStyleSheet("background-color: rgb(219, 239, 255);")
        self.listWidget.setObjectName("listWidget")
        self.label.raise_()
        self.textBrowser.raise_()
        self.textEdit.raise_()
        self.pushButton.raise_()
        self.pushButton_2.raise_()
        self.pushButton_3.raise_()
        self.pushButton_4.raise_()
        self.pushButton_5.raise_()
        self.listWidget.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "发送"))
        self.pushButton_2.setText(_translate("MainWindow", "语音通话"))
        self.pushButton_3.setText(_translate("MainWindow", "录音"))
        self.pushButton_4.setText(_translate("MainWindow", "关闭"))
        self.pushButton_5.setText(_translate("MainWindow", "聊天记录"))

# import 1369025_165540642000_2_rc


class MyMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, s, parent=None):
        self.s = s
        print("欢迎来到群组聊天室")
        self.s.send(b'OK all')
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)
        self.th = myThread(self.s)
        self.th.pressed.connect(self.display)
        self.th.start()
        self.pushButton.clicked.connect(self.chat)
        self.pushButton_4.clicked.connect(self.close_window)

    def close_window(self):
        self.close()
        # self.th.finished()
        # self.s.send(b'exit')
        # print('退出群组聊天室')

    def closeEvent(self, event):
        self.s.send(b'exit')
        print('退出群组聊天室')

    def chat(self):
        data = self.textEdit.toPlainText()
        self.textEdit.clear()
        print(data)
        if data == 'exit':
            self.s.send(b'exit')
        else:
            self.s.send(data.encode())

    def display(self, text):
        # (self.th.message).decode('utf-8')
        self.textBrowser.append(text)


class MyChatWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, s, obj, parent=None):
        self.s = s
        self.obj = obj
        print("欢迎来到与", obj, "的聊天室")
        #self.setWindowTitle("与%s聊天中"%obj)
        self.s.send(b'OK all')
        super(MyChatWindow, self).__init__(parent)
        self.setupUi(self)
        self.th = myThread(self.s)
        self.th.pressed.connect(self.display)
        self.th.start()
        self.pushButton.clicked.connect(self.chat)
        self.pushButton_4.clicked.connect(self.close_window)

    def close_window(self):
        self.close()
        # self.th.finished()
        # self.s.send(b'exit')
        # print('退出群组聊天室')

    def closeEvent(self, event):
        self.s.send(b'exit')
        print('退出单人聊天室')

    def chat(self):
        data = self.textEdit.toPlainText()
        self.textEdit.clear()
        print(data)
        if data == 'exit':
            self.s.send(b'exit')
        else:
            self.s.send(data.encode())

    def display(self, text):
        # (self.th.message).decode('utf-8')
        self.textBrowser.append(text)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = MyMainWindow()
    myWin.show()
    sys.exit(app.exec_())

# self.textBrowser显示
# self.textEdit  输入框   --- >  handler  --> 服务端
