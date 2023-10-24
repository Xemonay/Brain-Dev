from won import WonGame
from PyQt5 import uic
from PyQt5.QtCore import QUrl, Qt
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent, QMediaPlaylist
from PyQt5.QtWidgets import QMainWindow
from random import choice as ch
from english_words import get_english_words_set
from oh_no import OhNo
from timer_co import Timer


class GOWORD(QMainWindow):
    def __init__(self, other, other1):
        super().__init__()
        uic.loadUi('Design//goword.ui', self)
        other1.close()
        self.cw6 = ""
        self.lstacw6 = tuple(filter(lambda x: len(x) >= 5, list(get_english_words_set(['web2'], lower=True))))
        self.lstacw6was = set()
        self.cw6 = ch(self.lstacw6)
        self.alpha = {}
        for x in self.cw6:
            if x not in self.alpha:
                self.alpha[x] = 1
            else:
                self.alpha[x] += 1
        self.word_lal.setText(self.cw6)
        self.count_6 = 0
        self.lstam = 0
        self.lsta = []
        self.other1 = other1
        self.main = other
        self.timer_w = Timer(self, goword=True)
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
        okay = True
        alpha1 = {}
        if self.enter_word.text().lower() in self.lstacw6:
            for x in self.enter_word.text():
                if x not in alpha1:
                    alpha1[x] = 1
                else:
                    alpha1[x] += 1
            for x in alpha1.keys():
                if self.alpha.get(x, 0) - alpha1.get(x) < 1:
                    okay = False
        else:
            okay = False
        if okay:
            self.lsta.append(self.timer_w.seconds)
            self.count_6 += 1
            self.count_lal_2.setText(str(self.count_6))
            self.enter_word.setText("")
        else:
            pass

    def do1(self):
        self.timer_w.seconds = 0

    def not_good(self):
        self.not_wonthegame = True
        self.ohno = OhNo(self, self.main, self.other1)
        self.ohno.show()

    def closeEvent(self, event):
        if not self.wonthegame and not self.not_wonthegame:
            self.main.player.play()
        self.player.stop()
        self.timer_w.timer.stop()
