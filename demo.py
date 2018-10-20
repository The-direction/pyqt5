 #!/usr/bin/env python3
# coding=utf-8


from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from loginDemo import loginPage
from signinDemo import SigninPage

HOST = '127.0.0.1'
PORT = 8000
ADDR = (HOST, PORT)


class Demo(QWidget):
    def __init__(self, c_handler):
        self.c_handler = c_handler
        super(Demo, self).__init__()
        try:
            # 显示登录界面
            self.show_page()
        except Exception as e:
            print('error', e)

    def show_page(self):
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
        # self.login_button.setGeometry(50,150,80,40)
        self.setStyleSheet("QPushButton{background-color:#B4997E;color:snow;}")
        self.grid_layout = QGridLayout()
        self.h_layout = QHBoxLayout()
        self.v_layout = QVBoxLayout()

        self.layout_init()  # 布局
        self.lineedit_init()            # 单行文本输入框
        self.pushbutton_init()          # 按钮
        self.signin_page = SigninPage(self.c_handler)     # 实例化SigninPage()

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
        self.user_line.setPlaceholderText('请输入账号')
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
        # self.close()
        self.signin_page.exec_()

    def check_login_func(self):
        self.userinfo.append(self.user_line.text())
        self.userinfo.append(self.pwd_line.text())
        answer = self.c_handler.login(self.userinfo)
        if answer == True:
            QMessageBox.information(self, 'Information', '登录成功')
            # self.login_button.clicked.connect(self.show_login_page_func)
            self.close()
            self.login_page = loginPage(self.c_handler)
            self.login_page.show()

        else:
            QMessageBox.critical(self, 'Wrong', answer)
            self.user_line.clear()
            self.pwd_line.clear()
            self.userinfo = []
