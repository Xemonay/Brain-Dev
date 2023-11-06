from random import choice as ch

from PyQt5.QtCore import QUrl
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent, QMediaPlaylist
from PyQt5.QtWidgets import QMainWindow

from DesingPY.spatialmemdesign import Ui_MainWindow
from oh_no import OhNo
from timer_co import Timer
from won import WonGame


class SpatialMem(QMainWindow, Ui_MainWindow):
    def __init__(self, other, other1):
        super().__init__()
        self.setupUi(self)
        self.other1 = other1
        other1.close()
        self.name = "sa"
        self.main = other
        self.count = 0
        self.lstam = 0
        self.lsta = []
        self.picke = set()
        self.pressedP = set()
        self.timer_w = Timer(self, True)
        self.player = QMediaPlayer(self)
        self.music_lst1 = QMediaPlaylist(self)
        self.music_lst1.addMedia(QMediaContent(QUrl.fromLocalFile(r"Music/dsi-shop-theme-high-quality-y2bs.com.wav")))
        self.player = QMediaPlayer(self)
        for x in range(1, 37):
            eval(f"self.pushButton_{x}.clicked.connect(self.pbt)")
            eval(f"self.pushButton_{x}.setEnabled(False)")
        self.player.setVolume(self.main.player.volume())
        if self.player.volume() > 26:
            self.player.setVolume(26)
        self.music_lst1.setPlaybackMode(QMediaPlaylist.Loop)
        self.wonthegame = False
        self.not_wonthegame = False
        self.player.setPlaylist(self.music_lst1)
        self.player.play()
        self.okay_byt.clicked.connect(self.check_corr)
        self.do()
        self.timer_w.timer.start(1000)

    def pbt(self):
        if "#8BC34A" in self.sender().styleSheet():
            self.sender().setStyleSheet('background-color: #26C6DA;\ncolor:Transparent')
            self.pressedP.add(self.sender().text())
        else:
            self.sender().setStyleSheet('background-color: #8BC34A;\ncolor:Transparent')
            self.pressedP.remove(self.sender().text())

    def do(self):
        self.okay_byt.setEnabled(False)
        a = ';\ncolor:Transparent'
        for x in range(1, 37):
            eval(f"self.pushButton_{x}.setStyleSheet('background-color: #8BC34A' + a)")
            eval(f"self.pushButton_{x}.setEnabled(False)")
        self.okay_byt.setEnabled(False)
        for x in range(1, 37):
            choice = ch((1, 2))
            if choice == 1:
                eval(f"self.pushButton_{x}.setStyleSheet('background-color: #26C6DA' + a)")
                self.picke.add(str(x))

    def do1(self):
        a = ';\ncolor:Transparent'
        for x in self.picke:
            eval(f"self.pushButton_{int(x)}.setStyleSheet('background-color: #8BC34A' + a)")
        for x in range(1, 37):
            eval(f"self.pushButton_{x}.setEnabled(True)")
        self.timer_w.seconds = 0
        self.okay_byt.setEnabled(True)

    def check_corr(self):
        mist = 0
        a = ';\ncolor:Transparent'
        for x in self.pressedP:
            if x not in self.picke:
                eval(f"self.pushButton_{int(x)}.setStyleSheet('background-color: red' + a)")
                mist += 1
            else:
                eval(f"self.pushButton_{int(x)}.setStyleSheet('background-color: #DCEDC8' + a)")
        for x in self.picke:
            if x not in self.pressedP:
                eval(f"self.pushButton_{int(x)}.setStyleSheet('background-color: yellow' + a)")
                mist += 1
        for x in range(1, 37):
            eval(f"self.pushButton_{x}.setEnabled(False)")
        self.okay_byt.setEnabled(False)
        self.count += 1
        self.lsta.append(self.timer_w.seconds)
        self.lstam += mist
        if self.lstam > 60:
            self.not_good()
        if self.count == 10:
            self.wonthegame = True
            self.player.stop()
            self.timer_w.yes = False
            self.timer_w.timer.stop()
            self.won_the_game = WonGame(self, self.main)
            self.won_the_game.show()
        else:
            self.count_lal.setText(str(self.count))
            self.picke.clear()
            self.pressedP.clear()
            self.timer_w.look6 = True
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
