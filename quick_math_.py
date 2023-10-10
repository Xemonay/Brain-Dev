from random import choice as ch

from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow
from quick_math_won import WonGame
from timer_co import TimerThread
from oh_no import OhNo


class QuickMath(QMainWindow):
    def __init__(self, other):
        super().__init__()
        uic.loadUi('Design//quickmath.ui', self)
        self.main = other
        self.lsta = []
        self.nx = tuple(range(-20, 21))
        self.sign = ("+", "-", "*")
        self.count = 0
        self.seq = f"{ch(self.nx)} {ch(self.sign)} {ch(self.nx)} = ?"
        self.seconds = 0
        self.sequance.setText(self.seq)
        self.correct = str(eval(self.seq[:-4]))
        self.timerthread = TimerThread()
        self.timerthread.start()
        self.timerthread.time_signal.connect(self.update_timer)
        self.timerthread.finished.connect(self.pass_that)
        self.bt_0.clicked.connect(self.addx)
        self.bt_1.clicked.connect(self.addx)
        self.bt_2.clicked.connect(self.addx)
        self.bt_3.clicked.connect(self.addx)
        self.bt_4.clicked.connect(self.addx)
        self.bt_5.clicked.connect(self.addx)
        self.bt_6.clicked.connect(self.addx)
        self.bt_7.clicked.connect(self.addx)
        self.bt_8.clicked.connect(self.addx)
        self.bt_9.clicked.connect(self.addx)
        self.back_bt.clicked.connect(self.backb)
        self.minus_bt.clicked.connect(self.addx)

    def addx(self):
        if ((self.sender().text() != "0" and self.sender().text() != "-") or
                (self.sender().text() == "0" and self.answer.text() != "0") or
                (self.sender().text() == "-" and self.answer.text() == "")):
            self.answer.setText(self.answer.text() + self.sender().text())
        self.check_corr()

    def backb(self):
        if self.answer.text() != "":
            self.answer.setText(self.answer.text()[:-1])

    def update_timer(self):
        self.timer.setText(f"00:{str(self.seconds).rjust(2, '0')}")
        self.seconds += 1
        if self.seconds == 11:
            self.not_good()

    def not_good(self):
        self.timerthread.quit()
        self.ohno = OhNo(self, self.main)
        self.ohno.show()

    def pass_that(self):
        pass

    def check_corr(self):
        if self.answer.text() == self.correct:
            self.lsta.append(self.seconds)
            self.seq = f"{ch(self.nx)} {ch(self.sign)} {ch(self.nx)} = ?"
            self.seconds = 0
            self.timerthread.start()
            self.sequance.setText(self.seq)
            self.correct = str(eval(self.seq[:-4]))
            self.answer.setText("")
            self.count += 1
            self.count_seq.setText(str(self.count))
            self.timerthread.start()
            if self.count == 10:
                self.timerthread.quit()
                self.won = WonGame(self, self.main)
                self.won.show()
