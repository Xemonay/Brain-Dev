from random import choice as ch

from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent, QMediaPlaylist
from PyQt5.QtWidgets import QMainWindow

from DesingPY.design_quickmath import Ui_MainWindow
from oh_no import OhNo
from timer_co import Timer
from won import WonGame


class QuickMath(QMainWindow, Ui_MainWindow):
    def __init__(self, other, other1):  # ИНИЦИАЛИЗАЦИЯ
        super().__init__()
        self.setupUi(self)
        other1.close()
        self.other1 = other1
        self.main = other
        self.name = "QM"
        self.lsta = []
        self.lstam = 0
        self.nx = tuple(range(-20, 21))
        self.sign = ("+", "-", "*")
        self.count = 0
        self.main.player.pause()
        self.seq = f"{ch(self.nx)} {ch(self.sign)} {ch(self.nx)} = ?"
        self.sequance.setText(self.seq)
        self.correct = str(eval(self.seq[:-4]))
        self.timer_w = Timer(self)
        self.timer_w.timer.start(1000)
        self.player = QMediaPlayer(self)
        self.music_lst1 = QMediaPlaylist(self)
        self.music_lst1.addMedia(QMediaContent(QUrl.fromLocalFile(r"Music\the-pink-panther-theme-savefrom.com.wav")))
        self.player = QMediaPlayer(self)
        self.music_lst1.setPlaybackMode(QMediaPlaylist.Loop)
        self.player.setPlaylist(self.music_lst1)
        self.player.play()
        self.player.setVolume(self.main.player.volume())
        self.key_equal = Qt.Key_Equal
        self.key_enter = Qt.Key_Return
        self.key_MINUS = Qt.Key_Minus
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
        self.minus_bt.clicked.connect(self.addx)
        self.equal_bt.clicked.connect(self.check_corr)
        self.wonthegame = False
        self.not_wonthegame = False

    def addx(self):
        if ((self.sender().text() != "0" and self.sender().text() != "-") or
                (self.sender().text() == "0" and self.answer.text() != "0") or
                (self.sender().text() == "-" and self.answer.text() == "")):
            self.answer.setText(self.answer.text() + self.sender().text())

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
        if eventQKeyEvent.key() == self.key_MINUS and not eventQKeyEvent.isAutoRepeat():
            self.minus_bt.click()
        if eventQKeyEvent.key() == self.key_equal and not eventQKeyEvent.isAutoRepeat():
            self.equal_bt.click()
        if eventQKeyEvent.key() == self.key_enter and not eventQKeyEvent.isAutoRepeat():
            self.equal_bt.click()
        if eventQKeyEvent.key() == self.key_BS:
            self.back_bt.click()

    def backb(self):
        if self.answer.text() != "":
            self.answer.setText(self.answer.text()[:-1])

    def not_good(self):
        self.not_wonthegame = True
        self.ohno = OhNo(self, self.main, self.other1)
        self.ohno.show()

    def check_corr(self):
        if self.answer.text() == self.correct:
            self.lsta.append(self.timer_w.seconds)
            self.seq = f"{ch(self.nx)} {ch(self.sign)} {ch(self.nx)} = ?"
            self.sequance.setText(self.seq)
            self.correct = str(eval(self.seq[:-4]))
            self.answer.setText("")
            self.timer_w.seconds = 0
            self.count += 1
            self.count_seq.setText(str(self.count))
            if self.count == 10:
                self.timer_w.yes = False
                self.wonthegame = True
                self.won = WonGame(self, self.main)
                self.player.stop()
                self.won.show()
        else:
            self.lstam += 1

    def closeEvent(self, event):
        if not self.wonthegame and not self.not_wonthegame:
            self.main.player.play()
        self.player.stop()
        self.timer_w.timer.stop()
