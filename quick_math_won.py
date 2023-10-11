from PyQt5 import uic
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QDialog


class WonGame(QDialog):
    def __init__(self, other, main):
        super().__init__()
        uic.loadUi('Design//won_game_quick_math.ui', self)
        self.avg_sec.setText(str(sum(other.lsta) / 10))
        self.name_label.setText(main.username.text())
        self.okay_bt.clicked.connect(self.yeah)
        self.other = other
        self.player = QMediaPlayer(self)
        self.player.setMedia(
            QMediaContent(QUrl.fromLocalFile(r"C:\Users\faken\PycharmProjects\Brain-Dev\Sounds\WON!.wav")))
        self.player.play()
        self.other.close()

    def yeah(self):
        self.player.stop()
        self.close()
