from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QDialog
from DesingPY.oh_noodesign import Ui_Dialog
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent

class OhNo(QDialog, Ui_Dialog):
    def __init__(self, other, main, other1):
        super().__init__()
        self.setupUi(self)
        self.try_again_bt.clicked.connect(self.again)
        self.how = other1
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
