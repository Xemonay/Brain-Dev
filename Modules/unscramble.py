from random import choice as ch, shuffle as sh
from oh_no import OhNo
from won import WonGame
from PyQt5.QtCore import QUrl, Qt
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent, QMediaPlaylist
from PyQt5.QtWidgets import QMainWindow
from PyQt5 import uic

from timer_co import Timer


class Unscramble(QMainWindow):
    def __init__(self, other, other1):
        super().__init__()
        uic.loadUi('Design//unscramble.ui', self)
        self.other1 = other1
        other1.close()
        self.main = other
        self.count = 0
        self.lstam = 0
        self.lsta = []
        with open("TEXT//WORDS1.txt", mode="r", encoding="utf-8") as a:
            self.lstaw6 = tuple(x.strip("\n") for x in a.readlines())
        self.timer_w = Timer(self, unscramble=True)
        self.cw6 = ch(self.lstaw6)
        self.answer.setText(self.cw6)
        self.answer.setAlignment(Qt.AlignCenter)
        self.good_cw = ch((1, 2, 3, 4))
        for x in range(1, 5):
            if self.good_cw == x:
                self.cw61 = list(self.cw6)
                sh(self.cw61)
                eval(f"self.answer{x}.setText(''.join(self.cw61))")
            else:
                self.newcw6 = list(self.cw6)
                sh(self.newcw6)
                self.newcw6[ch(range(0, len(self.cw6)))] = ch(self.cw6)
                eval(f"self.answer{x}.setText(''.join(self.newcw6))")
        self.player = QMediaPlayer(self)
        self.music_lst1 = QMediaPlaylist(self)
        self.music_lst1.addMedia(QMediaContent(QUrl.fromLocalFile(r"Music/dsi-shop-theme-high-quality-y2bs.com.wav")))
        self.player = QMediaPlayer(self)
        self.player.setVolume(self.main.player.volume())
        if self.player.volume() > 26:
            self.player.setVolume(26)
        self.music_lst1.setPlaybackMode(QMediaPlaylist.Loop)
        self.wonthegame = False
        self.not_wonthegame = False
        self.player.setPlaylist(self.music_lst1)
        self.player.play()
        self.answer1.clicked.connect(self.check_corr)
        self.answer2.clicked.connect(self.check_corr)
        self.answer3.clicked.connect(self.check_corr)
        self.answer4.clicked.connect(self.check_corr)
        self.timer_w.timer.start(1000)

    def check_corr(self):
        self.count += 1
        self.count_lal.setText(str(self.count))
        self.lsta.append(self.timer_w.seconds)
        if self.count == 10:
            self.wonthegame = True
            self.won = WonGame(self, self.main)
            self.won.show()
        else:
            self.timer_w.look6 = True
            for x in range(1, 5):
                eval(f"self.answer{x}.setEnabled(False)")
            eval(f"self.answer{self.good_cw}.setStyleSheet('color: green')")
            if eval(f"self.answer{self.good_cw}") != self.sender():
                self.sender().setStyleSheet('color: red')
                self.lstam += 1
            if self.lstam > 5:
                self.not_good()
            self.timer_w.seconds = 0

    def do1(self):
        for x in range(1, 5):
            eval(f"self.answer{x}.setEnabled(True)")
        self.answer1.setStyleSheet('')
        self.answer2.setStyleSheet('')
        self.answer3.setStyleSheet('')
        self.answer4.setStyleSheet('')
        self.cw6 = ch(self.lstaw6)
        self.answer.setText(self.cw6)
        self.answer.setAlignment(Qt.AlignCenter)
        self.good_cw = ch((1, 2, 3, 4))
        for x in range(1, 5):
            if self.good_cw == x:
                self.cw61 = list(self.cw6)
                sh(self.cw61)
                eval(f"self.answer{x}.setText(''.join(self.cw61))")
            else:
                self.newcw6 = list(self.cw6)
                sh(self.newcw6)
                self.newcw6[ch(range(0, len(self.cw6)))] = ch(self.cw6)
                eval(f"self.answer{x}.setText(''.join(self.newcw6))")

    def not_good(self):
        self.not_wonthegame = True
        self.ohno = OhNo(self, self.main, self.other1)
        self.ohno.show()

    def closeEvent(self, event):
        if not self.wonthegame and not self.not_wonthegame:
            self.main.player.play()
        self.player.stop()
        self.timer_w.timer.stop()
