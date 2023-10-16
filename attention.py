from random import choice as ch

from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtGui import QPainter, QColor, QBrush, QPen
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent, QMediaPlaylist
from PyQt5.QtWidgets import QMainWindow
from PyQt5 import uic
from timer_co import Timer


class Attention(QMainWindow):
    def __init__(self, other, other1):
        super().__init__()
        uic.loadUi('Design//attention.ui', self)
        self.x, self.y = 650, 240
        other1.close()
        self.other1 = other1
        self.main = other
        self.n1 = tuple(range(1, 11))
        self.bananas_green = 0
        self.bananas_yellow = 0
        self.apples_green = 0
        self.apples_yellow = 0
        self.yellow = False
        self.green = False
        self.apples = False
        self.bananas = False
        # self.timer_w = Timer(self)
        # self.timer_w.timer.start(1000)
        # self.player = QMediaPlayer(self)
        # self.music_lst1 = QMediaPlaylist(self)
        # self.music_lst1.addMedia(QMediaContent(QUrl.fromLocalFile(r"")))
        # self.player = QMediaPlayer(self)
        # self.music_lst1.setPlaybackMode(QMediaPlaylist.Loop)
        # self.player.setPlaylist(self.music_lst1)
        # self.player.play()
        # self.player.setVolume(self.main.player.volume())
        self.key_BS = Qt.Key_Backspace
        self.key_0 = Qt.Key_0
        self.key_1 = Qt.Key_1
        self.key_2 = Qt.Key_2
        self.key_3 = Qt.Key_3
        self.key_4 = Qt.Key_4
        self.key_5 = Qt.Key_5
        self.key_6 = Qt.Key_6
        self.key_7 = Qt.Key_7
        self.key_8 = Qt.Key_8
        self.key_9 = Qt.Key_9
        self.bt_0.clicked.connect(self.addx)
        self.bt_1.clicked.connect(self.addx)
        self.bt_2.clicked.connect(self.addx)
        self.bt_3.clicked.connect(self.addx)
        self.bt_4.clicked.connect(self.addx)
        self.bt_5.clicked.connect(self.addx)
        self.bt_6.clicked.connect(self.addx)
        self.bt_7.clicked.connect(self.addx)
        self.bt_8.clicked.connect(self.addx)
        self.bt_9.clicked.connect(self.addx)
        self.back_bt.clicked.connect(self.backb)

    def keyReleaseEvent(self, eventQKeyEvent):
        if eventQKeyEvent.key() == self.key_0 and not eventQKeyEvent.isAutoRepeat():
            self.bt_0.click()
        if eventQKeyEvent.key() == self.key_1 and not eventQKeyEvent.isAutoRepeat():
            self.bt_1.click()
        if eventQKeyEvent.key() == self.key_2 and not eventQKeyEvent.isAutoRepeat():
            self.bt_2.click()
        if eventQKeyEvent.key() == self.key_3 and not eventQKeyEvent.isAutoRepeat():
            self.bt_3.click()
        if eventQKeyEvent.key() == self.key_4 and not eventQKeyEvent.isAutoRepeat():
            self.bt_4.click()
        if eventQKeyEvent.key() == self.key_5 and not eventQKeyEvent.isAutoRepeat():
            self.bt_5.click()
        if eventQKeyEvent.key() == self.key_6 and not eventQKeyEvent.isAutoRepeat():
            self.bt_6.click()
        if eventQKeyEvent.key() == self.key_7 and not eventQKeyEvent.isAutoRepeat():
            self.bt_7.click()
        if eventQKeyEvent.key() == self.key_8 and not eventQKeyEvent.isAutoRepeat():
            self.bt_8.click()
        if eventQKeyEvent.key() == self.key_9 and not eventQKeyEvent.isAutoRepeat():
            self.bt_9.click()
        if eventQKeyEvent.key() == self.key_BS:
            self.back_bt.click()

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        sum_x = ch(self.n1)
        choice_a = ch(tuple(range(0, sum_x)))
        choice_b = sum_x - choice_a
        choice_a_g = ch(tuple(range(0, choice_a)))
        choice_a_y = choice_a - choice_a_g
        choice_b_g = ch(tuple(range(0, choice_b)))
        choice_b_y = choice_b - choice_b_g
        color_banana_yellow = "#FDD835"
        color_apple_yellow = "#FFEB3B"
        color_banana_green = "#ARD581"
        color_apple_green = "#C5E1A5"
        for x in range(choice_a_g):
            self.draw_apple(color_apple_green, qp)
        for x in range(choice_a_y):
            self.draw_apple(color_apple_yellow, qp)
        for x in range(choice_b_g):
            self.draw_apple(color_banana_green, qp)
        for x in range(choice_b_y):
            self.draw_apple(color_banana_yellow, qp)
        qp.end()

    def draw_banana(self, color, qp):
        pass

    def draw_apple(self, color, qp):
        qp.setBrush(QColor(color))
        qp.setPen(QColor(0, 0, 0))
        qp.drawRect(30, 30, 120, 30)

    # def closeEvent(self, event):
    #     if not self.wonthegame:
    #         self.main.player.play()
    #     # self.player.stop()
    #     # self.timer_w.timer.stop()
