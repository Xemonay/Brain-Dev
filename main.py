import sys
from random import choice as ch

from PyQt5 import uic
from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtGui import QPixmap
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent, QMediaPlaylist
from PyQt5.QtWidgets import QApplication, QMainWindow

from changeprofile import ChangeProfileForm
from howtoplay import Choice
from list_of_games import ListOfGames
from questionmark import Creator
from set_form import SetMusic

if hasattr(Qt, 'AA_EnableHighDpiScaling'):
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)

if hasattr(Qt, 'AA_UseHighDpiPixmaps'):
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps, True)


class BrainDevMain(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('Design//main0.ui', self)
        self.list_of_games_bt.clicked.connect(self.list_of_games_window)
        self.training_bt.clicked.connect(self.training)
        self.edit_profile_bt.clicked.connect(self.change_profile_form)
        self.what_is_that.clicked.connect(self.mystery_bt)
        self.player = QMediaPlayer(self)
        self.music_lst1 = QMediaPlaylist(self)
        self.hat_lal.setPixmap(QPixmap("Pictures//dasabucket_sand6.png"))
        self.ron_va_lal.setPixmap(QPixmap("Pictures//ron_va6.png"))
        self.ron_del_lal.setPixmap(QPixmap("Pictures//ron_del.png"))
        self.ron_lu_lal.setPixmap(QPixmap("Pictures//ron_lu.png"))
        self.ron_te_lal.setPixmap(QPixmap("Pictures//ron_te.png"))
        self.music_lst1.addMedia([QMediaContent(QUrl.fromLocalFile(
            r"Music\c418-haggstrom-minecraft-volume-alpha-savefrom.com.wav")),
            QMediaContent(QUrl.fromLocalFile(
                r"Music\c418-wet-hands-minecraft-volume-alpha-savefrom.com.wav")),
            QMediaContent(QUrl.fromLocalFile(
                r"Music\c418-droopy-likes-your-face-minecraft-volume-alpha-savefrom.live.wav")),
            QMediaContent(QUrl.fromLocalFile(
                r"Music\c418-subwoofer-lullaby-minecraft-volume-alpha-savefrom.live.wav")),
            QMediaContent(QUrl.fromLocalFile(
                r"Music\c418-sweden-minecraft-volume-alpha-savefrom.live.wav")),
            QMediaContent(QUrl.fromLocalFile(
                r"Music\c418-equinoxe-minecraft-volume-alpha-savefrom.live.wav"))])
        self.player = QMediaPlayer(self)
        self.music_lst1.setPlaybackMode(QMediaPlaylist.Loop)
        self.player.setPlaylist(self.music_lst1)
        self.player.play()
        self.shop_bt.clicked.connect(self.test)
        self.music_bt.clicked.connect(self.setting)
        self.edit_profile_bt.clicked.connect(self.change_profile_form)
        self.what_is_that.clicked.connect(self.mystery_bt)

    def test(self):
        print("I clicked ->) ", self.sender().text())

    def change_profile_form(self):
        self.change_form = ChangeProfileForm(self)
        self.change_form.show()

    def list_of_games_window(self):
        self.list_of_games = ListOfGames(self)
        self.list_of_games.show()

    def setting(self):
        self.set = SetMusic(self)
        self.set.show()

    def training(self):
        eval(ch(["self.quick_math()", "self.math()", "self.attention()", "self.reaction()", "self.spatial_mem()",
                 "self.unscramble()"]))

    def quick_math(self):
        self.how = Choice(self, "QuickMath")

    def goword(self):
        self.how = Choice(self, "GOWORD")

    def attention(self):
        self.how = Choice(self, "Attention")

    def reaction(self):
        self.how = Choice(self, "Reaction")

    def spatial_mem(self):
        self.how = Choice(self, "SpatialMem")

    def unscramble(self):
        self.how = Choice(self, "Unscramble")

    def mystery_bt(self):
        self.questionmark = Creator()
        self.questionmark.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = BrainDevMain()
    ex.show()
    sys.exit(app.exec_())
