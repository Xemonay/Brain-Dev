from PyQt5 import uic
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QDialog
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent


class OhNo(QDialog):
    def __init__(self, other, main):
        super().__init__()
        uic.loadUi('Design//oh_noo.ui', self)
        self.try_again_bt.clicked.connect(self.again)
        self.quit_bt.clicked.connect(self.yeah)
        self.other = other
        self.main = main
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
        self.close()

    def again(self):
        self.player.stop()
        self.main.quick_math()
        self.close()
        self.again = True

    def closeEvent(self, event):
        if not self.again:
            self.main.player.play()
        self.player.stop()
