from PyQt5.QtCore import QThread, pyqtSignal


class TimerThread(QThread):
    time_signal = pyqtSignal(str)

    def __init__(self, parent=None):
        QThread.__init__(self, parent)

    def run(self):
        for x in range(11):
            self.sleep(1)
            self.time_signal.emit("16")
