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
            QMediaContent(QUrl.fromLocalFile(r"C:\Users\faken\PycharmProjects\Brain-Dev\Sounds\You Failed!.wav")))
        self.player.play()
        self.other.close()

    def yeah(self):
        self.player.stop()
        self.close()

    def again(self):
        self.player.stop()
        self.main.quick_math()
        self.close()
