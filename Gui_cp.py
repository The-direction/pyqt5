#!/usr/bin/env python3
# coding=utf-8

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, \
    QHBoxLayout, QVBoxLayout, QGridLayout, QDialog, QMessageBox
import signal
# from PyQt5 import QtCore
# from pyqt5_08 import *


USER_PWD = {'15755': '123456', '123456': '123456', '1': '1'}


class Demo(QWidget):
    def __init__(self):
        super(Demo, self).__init__()
        self.userinfo = []
        self.setWindowTitle("登陆界面")
        self.resize(270, 400)
        self.move(600, 100)
        # self.setGeometry(600,100,450,500)
        self.e = QLabel('    ')
        self.user_label = QLabel('帐号      ', self)
        self.user_label.setFont(QFont('黑体', 14))
        self.pwd_label = QLabel('密码      ', self)
        self.pwd_label.setFont(QFont('黑体', 14))
        self.user_line = QLineEdit(self)
        # self.user_line.resize(150,30)
        self.pwd_line = QLineEdit(self)
        # self.pwd_line.resize(150,30)
        self.login_button = QPushButton('登录', self)
        self.signin_button = QPushButton('注册', self)
        self.pwd_line.setEchoMode(QLineEdit.Password)
        # self.black = QLabel('    ',self)
        self.grid_layout = QGridLayout()
        self.h_layout = QHBoxLayout()
        self.v_layout = QVBoxLayout()

        self.layout_init()  # 布局
        self.lineedit_init()            # 单行文本输入框
        self.pushbutton_init()          # 按钮
        self.signin_page = SigninPage()     # 实例化SigninPage()

    def paintEvent(self, event):
        painter = QPainter(self)
        pixmap = QPixmap("bgpic2.jpg")
        painter.drawPixmap(self.rect(), pixmap)

    def layout_init(self):
        self.grid_layout.addWidget(self.user_label, 0, 0, 1, 1)
        self.grid_layout.addWidget(self.user_line, 0, 1, 1, 1)
        # self.grid_layout.addWidget(self.e,1,0,1,1)
        self.grid_layout.addWidget(self.pwd_label, 1, 0, 1, 1)
        self.grid_layout.addWidget(self.pwd_line, 1, 1, 1, 1)

        self.h_layout.addWidget(self.login_button)
        self.h_layout.addWidget(self.signin_button)
        self.v_layout.addLayout(self.grid_layout)
        self.v_layout.addLayout(self.h_layout)

        self.setLayout(self.v_layout)

    def lineedit_init(self):
        self.user_line.setPlaceholderText('请输入QQ')
        self.pwd_line.setPlaceholderText('请输入密码')
        self.user_line.textChanged.connect(self.check_input_func)
        self.pwd_line.textChanged.connect(self.check_input_func)

    def check_input_func(self):
        if self.user_line.text() and self.pwd_line.text():
            self.login_button.setEnabled(True)
        else:
            self.login_button.setEnabled(False)

    def pushbutton_init(self):
        self.login_button.setEnabled(False)
        self.login_button.clicked.connect(self.check_login_func)
        self.signin_button.clicked.connect(self.show_signin_page_func)

    def show_signin_page_func(self):
        self.signin_page.exec_()

    # def show_login_page_func(self):
    #     self.login_page.exec_()

    def check_login_func(self):
        self.return_info()
        if USER_PWD.get(self.user_line.text()) == self.pwd_line.text():
            QMessageBox.information(self, 'Information', '登录成功')
            # self.login_button.clicked.connect(self.show_login_page_func)
            self.close()
            self.login_page = loginPage()
            self.login_page.show()

        else:
            QMessageBox.critical(self, 'Wrong', '用户名或密码错误')
            self.user_line.clear()
            self.pwd_line.clear()

    def return_info(self):
        self.userinfo.append(self.user_line.text())
        self.userinfo.append(self.pwd_line.text())
        print(self.userinfo)


class loginPage(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("用户界面")
        self.setGeometry(900, 100, 270, 480)
        user_label = QLabel('  '*5+'>我的好友', self)
        user_label.setFont(QFont('黑体', 15))
        user_label.resize(290, 170)
        user_label.move(50, 10)
        user_label.setStyleSheet('QLabel{color:blank}')

        users_label = QLabel('  '*5+'>我的群聊', self)
        users_label.setFont(QFont('黑体', 15))
        users_label.resize(290, 170)
        users_label.move(50, 40)
        users_label.setStyleSheet('QLabel{color:blank}')

    def closeEvent(self,event):
        signal.signal(signal.SIGINT,signal.SIG_IGN)

    def paintEvent(self, event):
        painter = QPainter(self)
        pixmap = QPixmap("bgpic2.jpg")
        painter.drawPixmap(self.rect(), pixmap)


class SigninPage(QDialog):
    def __init__(self):
        super(SigninPage, self).__init__()
        self.setGeometry(600, 100, 400, 300)
        self.signin_user_label = QLabel('       '*2+'注册帐号         ')
        self.signin_user_label.setFont(QFont('黑体', 14))
        self.signin_pwd_label = QLabel('       '*2+'密　　码         ')
        self.signin_pwd_label.setFont(QFont('黑体', 14))
        self.signin_pwd2_label = QLabel('      '*2+'再次输入密码  ')
        self.signin_pwd2_label.setFont(QFont('黑体', 14))
        self.signin_user_line = QLineEdit()
        self.a = QLabel('       '*3)
        self.signin_pwd_line = QLineEdit()
        self.b = QLabel('       '*3)
        self.signin_pwd2_line = QLineEdit()
        self.c = QLabel('       '*3)
        self.signin_button = QPushButton('完成')
        self.d = QLabel('        '*5)
        self.signin_pwd_line.setEchoMode(QLineEdit.Password)
        self.signin_pwd2_line.setEchoMode(QLineEdit.Password)
        self.user_h_layout = QHBoxLayout()
        self.pwd_h_layout = QHBoxLayout()
        self.pwd2_h_layout = QHBoxLayout()
        self.button_layout = QHBoxLayout()
        self.all_v_layout = QVBoxLayout()

        self.lineedit_init()            # 单行文本输入框
        self.pushbutton_init()          # 按钮
        self.layout_init()

    def paintEvent(self, event):
        painter = QPainter(self)
        pixmap = QPixmap("bgpic4.jpg")
        painter.drawPixmap(self.rect(), pixmap)

    def layout_init(self):
        self.user_h_layout.addWidget(self.signin_user_label)
        self.user_h_layout.addWidget(self.signin_user_line)
        self.user_h_layout.addWidget(self.a)
        self.pwd_h_layout.addWidget(self.signin_pwd_label)
        self.pwd_h_layout.addWidget(self.signin_pwd_line)
        self.pwd_h_layout.addWidget(self.b)
        self.pwd2_h_layout.addWidget(self.signin_pwd2_label)
        self.pwd2_h_layout.addWidget(self.signin_pwd2_line)
        self.pwd2_h_layout.addWidget(self.c)
        self.button_layout.addWidget(self.d)
        self.button_layout.addWidget(self.signin_button)
        self.button_layout.addWidget(self.a)
        self.all_v_layout.addLayout(self.user_h_layout)
        self.all_v_layout.addLayout(self.pwd_h_layout)
        self.all_v_layout.addLayout(self.pwd2_h_layout)
        self.all_v_layout.addLayout(self.button_layout)

        self.setLayout(self.all_v_layout)

    def lineedit_init(self):
        self.signin_user_line.textChanged.connect(self.check_input_func)
        self.signin_pwd_line.textChanged.connect(self.check_input_func)
        self.signin_pwd2_line.textChanged.connect(self.check_input_func)

    def check_input_func(self):
        if self.signin_user_line.text() and \
                self.signin_pwd_line.text() and \
                self.signin_pwd2_line.text():
            self.signin_button.setEnabled(True)
        else:
            self.signin_button.setEnabled(False)

    def pushbutton_init(self):
        self.signin_button.setEnabled(False)
        self.signin_button.clicked.connect(self.check_signin_func)

    def check_signin_func(self):
        if self.signin_pwd_line.text() != self.signin_pwd2_line.text():
            QMessageBox.critical(
                self, 'Wrong', '两次密码输入不一样!')
        elif self.signin_user_line.text() not in USER_PWD:
            USER_PWD[self.signin_user_line.text()] = self.signin_pwd_line.text()
            QMessageBox.information(
                self, 'Information', '注册成功!')
            self.close()
        else:
            QMessageBox.critical(
                self, 'Wrong', '已被注册!')

        self.signin_user_line.clear()
        self.signin_pwd_line.clear()
        self.signin_pwd2_line.clear()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())


'''
5.5 小结

1. setPlaceholderText()方法用于在输入框显示浅灰色的提示文本；

2. exec_()方法可以让窗口成为模态窗口，而调用show()方法，窗口是非模态的。模态窗口将程序控制权占据，只有对当前窗口关闭后才能操作其他窗口；

3. QDialog有ecec_()方法，而QWidget没有；

4. 可以用setEchoMode(QLineEdit.Password)将普通输入框中的文字变成原点。

'''
