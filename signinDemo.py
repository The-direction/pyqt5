from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from loginDemo import loginPage


class SigninPage(QDialog):
    def __init__(self, c_handler):
        self.registinfo = []
        self.c_handler = c_handler
        super(SigninPage, self).__init__()
        self.setGeometry(600, 100, 400, 300)
        s1 = '       ' * 2 + '注册帐号         '
        self.signin_user_label = QLabel(s1)
        self.signin_user_label.setFont(QFont('黑体', 14))
        s2 = '       ' * 2 + '密　　码         '
        self.signin_pwd_label = QLabel(s2)
        self.signin_pwd_label.setFont(QFont('黑体', 14))
        s3 = '      ' * 2 + '再次输入密码  '
        self.signin_pwd2_label = QLabel(s3)
        self.signin_pwd2_label.setFont(QFont('黑体', 14))
        self.signin_user_line = QLineEdit()
        self.a = QLabel('       ' * 3)
        self.signin_pwd_line = QLineEdit()
        self.b = QLabel('       ' * 3)
        self.signin_pwd2_line = QLineEdit()
        self.c = QLabel('       ' * 3)
        self.signin_button = QPushButton('完成')
        self.d = QLabel('        ' * 5)
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
        self.registinfo.append(self.signin_user_line.text())
        self.registinfo.append(self.signin_pwd_line.text())
        self.registinfo.append(self.signin_pwd2_line.text())
        answer = self.c_handler.register(self.registinfo)

        if answer == True:
            QMessageBox.information(
                self, 'Information', '注册成功!')
            self.close()
            # self.login_page = loginPage(self.c_handler)
            # self.login_page.show()
        else:
            QMessageBox.critical(
                self, 'Wrong', answer)

        self.signin_user_line.clear()
        self.signin_pwd_line.clear()
        self.signin_pwd2_line.clear()
        self.registinfo = []
