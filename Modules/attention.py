from random import choice as ch

from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtGui import QPixmap
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent, QMediaPlaylist
from PyQt5.QtWidgets import QMainWindow

from DesingPY.design_attention import Ui_MainWindow
from oh_no import OhNo
from timer_co import Timer
from won import WonGame


class Attention(QMainWindow, Ui_MainWindow):
    def __init__(self, other, other1):
        super().__init__()
        self.setupUi(self)
        other1.close()
        self.name = "at"
        self.what = ""
        self.other1 = other1
        self.main = other
        self.n1 = 10
        self.count = 0
        self.lsta = []
        self.lstam = 0
        self.labels = [self.label_0, self.label_2, self.label_3, self.label_4, self.label_5, self.label_6, self.label_7,
                       self.label_8, self.label_9, self.label_10]
        self.ans = "0"
        self.timer_w = Timer(self)
        self.timer_w.timer.start(1000)
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
        self.player.play()
        self.key_equal = Qt.Key_Equal
        self.key_enter = Qt.Key_Return
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
        self.equal_bt.clicked.connect(self.check_corr)
        self.back_bt.clicked.connect(self.backb)
        self.gen_fruits()

    def addx(self):
        if self.answer.text() != "0":
            self.answer.setText(self.answer.text() + self.sender().text())

    def backb(self):
        if self.answer.text() != "":
            self.answer.setText(self.answer.text()[:-1])

    def check_corr(self):
        if self.ans == self.answer.text():
            self.count += 1
            self.lsta.append(self.timer_w.seconds)
            if self.count == 16:
                self.wonthegame = True
                self.player.stop()
                self.timer_w.yes = False
                self.timer_w.timer.stop()
                self.won_the_game = WonGame(self, self.main)
                self.won_the_game.show()
            else:
                self.answer.setText("")
                self.count_lalo.setText(str(self.count))
                self.gen_fruits()
                self.timer_w.seconds = 0
        else:
            self.lstam += 1

    def not_good(self):
        self.not_wonthegame = True
        self.ohno = OhNo(self, self.main, self.other1)
        self.ohno.show()

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
        if eventQKeyEvent.key() == self.key_equal and not eventQKeyEvent.isAutoRepeat():
            self.equal_bt.click()
        if eventQKeyEvent.key() == self.key_enter and not eventQKeyEvent.isAutoRepeat():
            self.equal_bt.click()
        if eventQKeyEvent.key() == self.key_BS:
            self.back_bt.click()

    def gen_fruits(self):
        self.labels = [self.label_0, self.label_2, self.label_3, self.label_4, self.label_5, self.label_6, self.label_7,
                       self.label_8, self.label_9, self.label_10]
        choice_a = ch(tuple(range(0, self.n1 + 1)))
        choice_b = self.n1 - choice_a
        if choice_b < 2:
            choice_b = 2
            choice_a = 8
        choice_a_g = ch(tuple(range(0, choice_a + 1)))
        choice_a_y = choice_a - choice_a_g
        choice_b_g = ch(tuple(range(0, choice_b + 1)))
        choice_b_y = choice_b - choice_b_g
        self.what = ch(("GREEN APPLES", "YELLOW APPLES", "YELLOW BANANAS", "GREEN BANANAS"))
        match self.what:
            case "GREEN APPLES":
                self.ans = str(choice_a_g)
            case "YELLOW APPLES":
                self.ans = str(choice_a_y)
            case "YELLOW BANANAS":
                self.ans = str(choice_b_y)
            case "GREEN BANANAS":
                self.ans = str(choice_b_g)
        self.What_tofind.setText(self.what)
        if ch(('yellow', 'green')) == 'yellow':
            self.What_tofind.setStyleSheet(f"color: {ch(('#D4E157', '#9CCC65'))};\nbackground-color: "
                                           f"{ch(('#FDD835', '#FFF176'))}")
        else:
            self.What_tofind.setStyleSheet(f"color: {ch(('#FDD835', '#FFF176'))};\nbackground-color: "
                                           f"{ch(('#D4E157', '#9CCC65'))}")
        for x in range(choice_a_g):
            self.draw_apple("G")
        for x in range(choice_a_y):
            self.draw_apple("YE")
        for x in range(choice_b_g):
            self.draw_banana("G")
        for x in range(choice_b_y):
            self.draw_banana("YE")

    def draw_banana(self, color):
        label = ch(self.labels)
        label.setPixmap(QPixmap(f"Pictures//banana{color}.png"))
        self.labels.pop(self.labels.index(label))

    def draw_apple(self, color):
        label = ch(self.labels)
        label.setPixmap(QPixmap(f"Pictures//apple{color}.png"))
        self.labels.pop(self.labels.index(label))

    def closeEvent(self, event):
        if not self.wonthegame and not self.not_wonthegame:
            self.main.player.play()
        self.player.stop()
        self.timer_w.timer.stop()
