from PyQt5.QtCore import QUrl
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtWidgets import QDialog

from DesingPY.won_game1 import Ui_Form


class WonGame(QDialog, Ui_Form):
    def __init__(self, other, main):
        super().__init__()
        self.setupUi(self)
        self.avg_sec.setText(str(sum(other.lsta) / 10))
        self.mistake_l.setText(str(other.lstam))
        self.name_label.setText(main.username.text())
        self.okay_bt.clicked.connect(self.yeah)
        self.other = other
        self.main = main
        self.player = QMediaPlayer(self)
        self.player.setMedia(
            QMediaContent(QUrl.fromLocalFile(r"Sounds\WON!.wav")))
        self.player.setVolume(main.player.volume())
        self.player.play()
        self.other.close()

    def yeah(self):
        self.player.stop()
        self.main.player.play()
        self.close()

    def closeEvent(self, event):
        self.player.stop()
        self.main.player.play()
