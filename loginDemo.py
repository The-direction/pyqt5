from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import signal
import os
import re
import time
from lanse import *
from clientChat import F_thread
# from lanse import MyMainWindow


class loginPage(QDialog):
    def __init__(self, c_handler):
        self.c_handler = c_handler
        self.s = self.c_handler.s
        super().__init__()
        self.setStyleSheet(
            'QPushButton{background-color:#9C2D43;border:none;}')
        # Qthread中创建的信号
        self.rlist = []
        # 好友列表 {好友名称:按钮}
        self.add_friend_button = []
        self.setWindowTitle("用户界面")
        self.setGeometry(900, 100, 270, 480)
        user_button = QPushButton('>我的好友', self)
        users_button = QPushButton('>我的群聊', self)
        self.user_list = QListWidget()
        self.layout = QGridLayout()
        self.layout.addWidget(users_button, 1, 0)
        self.layout.addWidget(user_button, 2, 0)
        self.layout.addWidget(self.user_list, 3, 0)
        self.setLayout(self.layout)

        user_button.clicked.connect(self.find_friend)
        users_button.clicked.connect(self.createchat)
        # user_button.setFont(QFont('黑体', 15))
        # user_button.resize(80, 30)
        # user_button.move(50, 60)
        # user_button.setStyleSheet(
        # 'QPushButton{background-color:#FFE3E5;border:none;}')
        # self.listfile = QListWidget()
        # self.listfile.resize(80,50)
        # self.listfile.move(100,100)

        # users_button.setFont(QFont('黑体', 15))
        # users_button.resize(80, 30)
        # users_button.move(50, 10)
        # users_button.setStyleSheet(
        # 'QPushButton{background-color:#FFE3E5;border:none;}')
        # self.find_friend()

    # def check_func(self):
    #     self.chat_in_room = Chatthread(
    #         target=self.createchat, args=(self.c_handler.s,))
    #     self.chat_in_room.start()
    #     self.chat_in_room.join()

    def find_friend(self):
        print('创建线程收取消息')
        self.f_th = F_thread(self.s)
        self.f_th.friendlist_recv.connect(self.show_list)
        self.add_signal(self.f_th.friendlist_recv)
        self.f_th.start()

    def add_signal(self, SIG):
        self.rlist.append(SIG)

    def show_list(self, f_info):
        print(f_info, "-----show_list----")
        friend_l = re.split(r'\W', f_info.decode())
        friend_l.pop(0)
        friend_l.pop(-1)
        print(friend_l)
        if friend_l:
            self.user_list.clear()
            for friend_name in friend_l:
                #把好友信息都添加到列表里
                self.user_list.addItem(friend_name)
                self.user_list.itemClicked.connect(lambda:self.createchat_1(friend_name))
                #每循环一次，就刷新一次
                QApplication.processEvents()
                time.sleep(0.1)
                #widget = QPushButton(friend_name, self)
                #self.layout.addWidget(widget)
                #self.add_friend_button.append({friend_name: widget})
                #widget.clicked.connect(lambda:self.createchat_1(friend_name))
        #         button_name = friend_name + '_button'
        #         button_name = QPushButton(friend_name,self)
        #         button_name.setFont(QFont("黑体",10))
        #         button_name.resize(80,15)
        #         button_name.move(100,y)
        #         y += 20
                # self.listfile.addItem(friend_name)
            # QApplication.processEvents()
            # time.sleep(1)

    def createchat_1(self, friend_name):
        classname = friend_name + "page"

        class classname(MyChatWindow):
            def __init__(self, s, obj, parent=None):
                super().__init__(s, obj)
                
        self.chat_page1 = classname(self.s, friend_name)
        self.chat_page1.show()

    def createchat(self, s):
        self.chat_page = MyMainWindow(self.c_handler.s)
        self.chat_page.show()

    def closeEvent(self, event):
        print('退出客户端')
        self.c_handler.exit()
        # os.kill(os.getpid(), signal.SIGINT)

    def paintEvent(self, event):
        painter = QPainter(self)
        pixmap = QPixmap("bgpic5.jpg")
        painter.drawPixmap(self.rect(), pixmap)
