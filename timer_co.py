from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import QTimer


class Timer(QMainWindow):
    def __init__(self, obj, spatialmem=False, unscramble=False, goword=False):
        super().__init__()
        self.spatialmem = spatialmem
        self.unscramble = unscramble
        self.goword = goword
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.showtime)
        self.obj = obj
        self.seconds = 0
        self.yes = True
        self.look, self.look6 = True, False

    def showtime(self):
        if self.yes:
            self.seconds += 1
            if self.spatialmem:
                if self.seconds == 10 and self.look:
                    self.obj.do1()
                    self.look = False
                    self.seconds = 0
                if self.look6 and self.seconds == 6:
                    self.look = True
                    self.look6 = False
                    self.seconds = 0
                    self.obj.do()
            elif self.unscramble:
                if self.seconds == 2 and self.look6:
                    self.seconds = 0
                    self.look6 = False
                    self.obj.do1()
                if self.seconds == 20:
                    self.obj.not_good()
            elif self.goword:
                self.obj.label_T.setText("")
                if self.seconds == 16:
                    self.obj.do1()
            else:
                if self.seconds == 10:
                    self.yes = False
                    self.obj.not_good()
            self.obj.timer.setText(f"00:{str(self.seconds).rjust(2, '0')}")
