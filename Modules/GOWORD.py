from won import WonGame
from PyQt5 import uic
from PyQt5.QtCore import QUrl, Qt
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent, QMediaPlaylist
from PyQt5.QtWidgets import QMainWindow
from random import choice as ch
from english_words import get_english_words_set
from oh_no import OhNo
from timer_co import Timer
from icecream import ic

class GOWORD(QMainWindow):
    def __init__(self, other, other1):
        super().__init__()
        uic.loadUi('Design//goword.ui', self)
        other1.close()
        self.cw6 = ""
        self.lstacw6 = tuple(filter(lambda x: len(x) >= 5, list(get_english_words_set(['web2'], lower=True))))
        self.lstacw6c = tuple(filter(lambda x: len(x) >= 3, list(get_english_words_set(['web2'], lower=True))))
        self.lstacw6was = set()
        self.cw6 = ch(self.lstacw6)
        self.cw6a = 0
        self.alpha = {}
        self.word_lal.setAlignment(Qt.AlignCenter)
        for x in self.cw6:
            if x not in self.alpha:
                self.alpha[x] = 1
            else:
                self.alpha[x] += 1
        self.word_lal.setText(self.cw6)
        self.count_6 = 0
        self.lstam = 0
        self.lsta = [[0]]
        self.other1 = other1
        self.main = other
        self.timer_w = Timer(self, goword=True)
        self.timer_w.timer.start(1000)
        self.count = 1
        self.count_lal.setText("1")
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
        if self.enter_word.text().lower() == self.cw6:
            self.label_T.setText("You cant put the exact same word!")
        else:
            if self.enter_word.text().lower() not in self.lstacw6was:
                if self.enter_word.text().lower() in self.lstacw6c:
                    for x in self.enter_word.text().lower():
                        if x not in alpha1:
                            alpha1[x] = 1
                        else:
                            alpha1[x] += 1
                    for x in alpha1.keys():
                        if self.alpha.get(x, 0) - alpha1.get(x) < 0:
                            okay = False
                            break
                else:
                    okay = False
                if okay:
                    self.lstacw6was.add(self.enter_word.text().lower())
                    self.lsta[-1].append(self.timer_w.seconds - self.cw6a)
                    self.cw6a = self.timer_w.seconds
                    self.count_6 += 1
                    self.count_lal_2.setText(str(self.count_6))
                    self.enter_word.setText("")
                else:
                    self.lstam += 1
                    self.enter_word.setStyleSheet("color: red")
            else:
                self.label_T.setStyleSheet("color: FFEB3B")
                self.label_T.setText("Already was checked!")

    def do1(self):
        self.cw6a = 0
        if self.count_6 < 1:
            self.not_good()
        self.count_lal.setText(str(self.count))
        if self.count == 10:
            ic(self.lsta)
            self.lsta = [sum(x) for x in self.lsta]
            self.wonthegame = True
            self.won = WonGame(self, self.main)
            self.won.show()
        self.count_lal_2.setText("0")
        self.lsta.append([0])
        self.cw6 = 0
        self.count += 1
        self.timer_w.seconds = 0
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
        self.enter_word.setText("")

    def not_good(self):
        self.not_wonthegame = True
        self.ohno = OhNo(self, self.main, self.other1)
        self.ohno.show()

    def closeEvent(self, event):
        if not self.wonthegame and not self.not_wonthegame:
            self.main.player.play()
        self.player.stop()
        self.timer_w.timer.stop()
