from won import WonGame
from PyQt5 import uic
from PyQt5.QtCore import QUrl, Qt
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent, QMediaPlaylist
from PyQt5.QtWidgets import QMainWindow
from random import choice as ch
from oh_no import OhNo
from timer_co import Timer


class GOWORD(QMainWindow):
    def __init__(self, other, other1):
        super().__init__()
        uic.loadUi('Design//goword.ui', self)
        other1.close()
        self.cw6 = ""
        with open("TEXT//WORDS1.txt", mode="r", encoding="utf-8") as a:
            self.lstacw6 = tuple(x.strip("\n") for x in a.readlines())
        self.cw6 = ch(self.lstacw6)
        self.lstam = 0
        self.lsta = []
        self.other1 = other1
        self.main = other
        self.timer_w = Timer(self)
        self.timer_w.timer.start(1000)
        self.count = 0
        self.player = QMediaPlayer(self)
        self.music_lst1 = QMediaPlaylist(self)
        self.music_lst1.addMedia(QMediaContent(QUrl.fromLocalFile(r"Music/videoplayback.wav")))
        self.player = QMediaPlayer(self)
        self.player.setVolume(self.main.player.volume())
        self.enter_key = Qt.Key_Return
        self.enter_bat.clicked.connect(self.check_corr)
        if self.player.volume() > 26:
            self.player.setVolume(26)
        self.music_lst1.setPlaybackMode(QMediaPlaylist.Loop)
        self.wonthegame = False
        self.not_wonthegame = False
        self.player.setPlaylist(self.music_lst1)
        self.player.play()

    def keyReleaseEvent(self, eventQKeyEvent):
        if eventQKeyEvent.key() == self.enter_key and not eventQKeyEvent.isAutoRepeat():
            self.enter_bat.click()

    def check_corr(self):


    def not_good(self):
        self.not_wonthegame = True
        self.ohno = OhNo(self, self.main, self.other1)
        self.ohno.show()

    def closeEvent(self, event):
        if not self.wonthegame and not self.not_wonthegame:
            self.main.player.play()
        self.player.stop()
        self.timer_w.timer.stop()
