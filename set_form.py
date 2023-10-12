from PyQt5 import uic
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QDialog, QFileDialog


class SetMusic(QDialog):
    def __init__(self, main):
        super().__init__()
        uic.loadUi('Design//set.ui', self)
        self.horizontalSliderL.setValue(main.player.volume())
        self.main = main
        self.player = main.player
        self.horizontalSliderL.valueChanged.connect(self.change_vol)
        self.volume_ll.setText("Volume:" + str(self.horizontalSliderL.value()))
        self.next_music.clicked.connect(self.nextmusic)

    def nextmusic(self):
        self.player.setPosition(self.player.position() + 1)

    def change_vol(self):
        self.player.setVolume(self.horizontalSliderL.value())
        self.volume_ll.setText("Volume:" + str(self.horizontalSliderL.value()))


    def change_music(self):
        fname = QFileDialog.getOpenFileName(self, 'Choose wav', '', 'audio (*.wav)')[0]
        self.player.setMedia(QMediaContent(QUrl.fromLocalFile(fname)))
