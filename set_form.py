from PyQt5 import uic
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QDialog, QFileDialog


class SetMusic(QDialog):
    def __init__(self, main):
        super().__init__()
        uic.loadUi('Design//set.ui', self)
        self.main = main
        self.player = QMediaPlayer(self)
        self.player.play()

    def change_music(self):
        fname = QFileDialog.getOpenFileName(self, 'Choose wav', '', 'audio (*.wav)')[0]
        self.player.setMedia(QMediaContent(QUrl.fromLocalFile(fname)))
