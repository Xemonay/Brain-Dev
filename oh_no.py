import sqlite3

from PyQt5.QtCore import QUrl
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtWidgets import QDialog

from DesingPY.oh_noodesign import Ui_Dialog


class OhNo(QDialog, Ui_Dialog):
    def __init__(self, other, main, other1):
        super().__init__()
        self.setupUi(self)
        self.try_again_bt.clicked.connect(self.again)
        self.how = other1
        self.quit_bt.clicked.connect(self.yeah)
        self.other = other
        self.main = main
        if main.log:
            cor = sqlite3.connect("DataBases//accounts.sqlite")
            c = cor.cursor()
        match self.other.name:
            case "QM":
                a = 0
                if main.log:
                    c.execute("""UPDATE quickmath
                                SET lost = lost + 1, mistakes = mistakes + ?
                                WHERE name = ?""", (other.lstam, self.main.username.text()))
            case "at":
                a = 2
                if main.log:
                    c.execute("""UPDATE attention
                                SET lost = lost + 1, mistakes = mistakes + ?
                                WHERE name = ?""", (other.lstam, self.main.username.text()))
            case "go":
                a = 1
                if main.log:
                    c.execute("""UPDATE goword
                                SET lost = lost + 1, mistakes = mistakes + ?
                                WHERE name = ?""", (other.lstam, self.main.username.text()))
            case "ra":
                a = 3
                if main.log:
                    c.execute("""UPDATE reaction
                                SET lost = lost + 1, mistakes = mistakes + ?
                                WHERE name = ?""", (other.lstam, self.main.username.text()))
            case "ua":
                a = 4
                if main.log:
                    c.execute("""UPDATE unscramble
                                SET lost = lost + 1, mistakes = mistakes + ?
                                WHERE name = ?""", (other.lstam, self.main.username.text()))
            case "sa":
                a = 5
                if main.log:
                    c.execute("""UPDATE spatialmem
                                SET lost = lost + 1, mistakes = mistakes + ?
                                WHERE name = ?""", (other.lstam, self.main.username.text()))
        if main.log:
            cor.commit()
            cor.close()
        self.main.lst_mist[a] += self.other.lstam
        self.main.lst_lost[a] += 1
        self.other.close()
        self.player = QMediaPlayer(self)
        self.player.setMedia(
            QMediaContent(QUrl.fromLocalFile(r"Sounds\You Failed!.wav")))
        self.player.setVolume(main.player.volume())
        self.player.play()
        self.other.close()
        self.again = False

    def yeah(self):
        self.player.stop()
        self.main.player.play()
        self.main.again = False
        self.close()

    def again(self):
        self.player.stop()
        self.how.start_bt.click()
        self.again = True
        self.close()

    def closeEvent(self, event):
        if not self.again:
            self.main.player.play()
        self.player.stop()
