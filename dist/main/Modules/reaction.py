from random import choice as ch

from PyQt5.QtCore import QUrl
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent, QMediaPlaylist
from PyQt5.QtWidgets import QMainWindow

from DesingPY.design_reaction import Ui_MainWindow
from oh_no import OhNo
from timer_co import Timer
from won import WonGame


class Reaction(QMainWindow, Ui_MainWindow):
    def __init__(self, other, other1):
        super().__init__()
        self.setupUi(self)
        other1.close()
        self.lstam = 0
        self.name = "ra"
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
        if self.player.volume() > 26:
            self.player.setVolume(26)
        self.music_lst1.setPlaybackMode(QMediaPlaylist.Loop)
        self.wonthegame = False
        self.not_wonthegame = False
        self.player.setPlaylist(self.music_lst1)
        self.alpha = ("yellow", "green", "white", "orange", "magenta", "cyan", "pink", "light blue", "black",
                      "purple", "light green", "FFF9C4", "FFE0B2")
        self.shake_the_buttons()
        self.player.play()
        self.target_bt.clicked.connect(self.check_corr)

    def check_corr(self):
        if self.sender() == self.target_bt:
            self.count += 1
            if self.count == 10:
                self.timer_w.timer.stop()
                self.wonthegame = True
                self.timer_w.yes = False
                self.won = WonGame(self, self.main)
                self.won.show()
            else:
                self.shake_the_buttons()
                self.count_lal.setText(str(self.count))
                self.lsta.append(self.timer_w.seconds)
                self.timer_w.seconds = 0
        else:
            self.lstam += 1

    def not_good(self):
        self.not_wonthegame = True
        self.ohno = OhNo(self, self.main, self.other1)
        self.ohno.show()

    def shake_the_buttons(self):
        for x in range(1, 81):
            eval(f"self.fa_target_bt_{x + 1}.move({ch(range(60, 741))}, {ch(range(60, 541))})")
            eval(f"self.fa_target_bt_{x + 1}.setStyleSheet('background-color: {ch(self.alpha)}')")
            eval(f"self.fa_target_bt_{x + 1}.clicked.connect(self.check_corr)")
        self.target_bt.move(ch(range(60, 741)), ch(range(60, 541)))

    def closeEvent(self, event):
        if not self.wonthegame and not self.not_wonthegame:
            self.main.player.play()
        self.player.stop()
        self.timer_w.timer.stop()
