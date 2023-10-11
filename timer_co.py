from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import QTimer


class Timer(QMainWindow):
    def __init__(self, obj):
        super().__init__()
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.showtime)
        self.obj = obj
        self.seconds = 0
        self.yes = True

    def showtime(self):
        if self.yes:
            self.seconds += 1
            self.obj.timer.setText(f"00:{str(self.seconds).rjust(2, '0')}")
            if self.seconds == 10:
                self.yes = False
                self.obj.not_good()
