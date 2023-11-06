import sqlite3

from PyQt5.QtCore import QUrl
from PyQt5.QtMultimedia import QMediaContent, QMediaPlaylist
from PyQt5.QtWidgets import QDialog, QFileDialog

from DesingPY.setdesign import Ui_Form


class SetMusic(QDialog, Ui_Form):
    def __init__(self, main):
        super().__init__()
        self.setupUi(self)
        self.horizontalSliderL.setValue(main.player.volume())
        self.main = main
        self.player = main.player
        self.horizontalSliderL.valueChanged.connect(self.change_vol)
        self.volume_ll.setText("Volume:" + str(self.horizontalSliderL.value()))
        self.next_music.clicked.connect(self.nextmusic)
        if self.main.log:
            self.con = sqlite3.connect('DataBases//accounts.sqlite')
            afs = self.con.cursor().execute('''SELECT music FROM item
                                                WHERE name = ?'''
                                            '', (self.main.username.text(),)).fetchone()[0]
            self.horizontalSliderL.setValue(afs)
        self.pre_music.clicked.connect(self.prevmusic)
        self.change_msc_0.clicked.connect(self.changetodefault)
        self.change_msc.clicked.connect(self.change_music)

    def nextmusic(self):
        self.main.music_lst1.next()

    def prevmusic(self):
        self.main.music_lst1.previous()

    def change_vol(self):
        self.player.setVolume(self.horizontalSliderL.value())
        self.volume_ll.setText("Volume:" + str(self.horizontalSliderL.value()))

    def changetodefault(self):
        self.player.setPlaylist(self.main.music_lst1)
        self.player.play()

    def change_music(self):
        fname = QFileDialog.getOpenFileName(self, 'Choose wav', '', 'audio (*.wav)')[0]
        playlist = QMediaPlaylist(self)
        playlist.addMedia(QMediaContent(QUrl.fromLocalFile(fname)))
        playlist.setPlaybackMode(QMediaPlaylist.Loop)
        self.player.setPlaylist(playlist)
        self.player.play()

    def closeEvent(self, a0):
        if self.main.log:
            self.con.cursor().execute('''UPDATE item
                            set music = ?
                            WHERE name = ?''', (self.main.player.volume(), self.main.username.text()))
            self.con.commit()
            self.con.close()
