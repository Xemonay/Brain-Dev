import sqlite3

from PyQt5.QtCore import QUrl
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtWidgets import QMainWindow

from DesingPY.design_shop import Ui_MainWindow


class Shop(QMainWindow, Ui_MainWindow):
    def __init__(self, main):
        super().__init__()
        self.setupUi(self)
        self.main = main
        self.the_money_lal.setText(str(self.main.money))
        self.buy.clicked.connect(self.buy016)
        self.try_white_hat.toggled.connect(self.change)
        self.try_black_hat.toggled.connect(self.change)
        self.try_ron_del.toggled.connect(self.stateChanged)
        self.try_ron_te.toggled.connect(self.stateChanged)
        self.try_ron_va.toggled.connect(self.stateChanged)
        self.try_ron_lu.toggled.connect(self.stateChanged)
        self.player = QMediaPlayer(self)
        self.player.setMedia(QMediaContent(QUrl.fromLocalFile(r'Music\\buying-sound-effect-y2bs.com.wav')))
        self.label_016.setPixmap(QPixmap("Pictures//the_cash.png"))
        for x in range(6):
            if (self.main.white_hat, self.main.black_hat, self.main.ron_va, self.main.ron_del, self.main.ron_lu,
                    self.main.ron_te)[x] == 1:
                match x:
                    case 0:
                        self.take_white_hat.setEnabled(False)
                    case 1:
                        self.take_black_hat.setEnabled(False)
                    case 2:
                        self.take_ron_va.setEnabled(False)
                    case 3:
                        self.take_ron_del.setEnabled(False)
                    case 4:
                        self.take_ron_lu.setEnabled(False)
                    case 5:
                        self.take_ron_te.setEnabled(False)
        if main.log:
            self.con = sqlite3.connect("DataBases//accounts.sqlite")
            self.c = self.con.cursor()
            self.the_money_lal.setText(str(self.c.execute("""SELECT money FROM item
                            WHERE name = ?""", (main.username.text(),)).fetchone()[0]))
            asd = self.c.execute("""SELECT hat1, hat2, ron_va, ron_del, ron_lu, ron_te FROM item
                                    WHERE name = ?""", (self.main.username.text(),)).fetchall()[0]
            for x in range(len(asd)):
                if asd[x] == '1':
                    match x:
                        case 0:
                            self.take_white_hat.setEnabled(False)
                        case 1:
                            self.take_black_hat.setEnabled(False)
                        case 2:
                            self.take_ron_va.setEnabled(False)
                        case 3:
                            self.take_ron_del.setEnabled(False)
                        case 4:
                            self.take_ron_lu.setEnabled(False)
                        case 5:
                            self.take_ron_te.setEnabled(False)

    def buy016(self):
        count = 0
        if 2 == self.take_white_hat.checkState():
            count += 1
        if 2 == self.take_black_hat.checkState():
            count += 1
        if 2 == self.take_ron_va.checkState():
            count += 1
        if 2 == self.take_ron_te.checkState():
            count += 1
        if 2 == self.take_ron_lu.checkState():
            count += 1
        if 2 == self.take_ron_del.checkState():
            count += 1
        if int(self.the_money_lal.text()) - count < 0:
            self.no_money.setText("Not enough money")
        if count == 0:
            self.no_money.setText("Don't you like anything?")
        else:
            self.player.play()
            if self.main.log:
                self.c.execute("""UPDATE item
                                    set money = money - ?
                                    WHERE name = ?""", (count, self.main.username.text()))
                if 2 == self.take_white_hat.checkState():
                    self.c.execute("""UPDATE item
                                        SET hat1 = 1
                                        WHERE name = ?""", (self.main.username.text(),))
                if 2 == self.take_black_hat.checkState():
                    self.c.execute("""UPDATE item
                                                        SET hat2 = 1
                                                        WHERE name = ?""", (self.main.username.text(),))
                if 2 == self.take_ron_va.checkState():
                    self.c.execute("""UPDATE item
                                                        SET ron_va = 1
                                                        WHERE name = ?""", (self.main.username.text(),))
                if 2 == self.take_ron_te.checkState():
                    self.c.execute("""UPDATE item
                                                        SET ron_te = 1
                                                        WHERE name = ?""", (self.main.username.text(),))
                if 2 == self.take_ron_lu.checkState():
                    self.c.execute("""UPDATE item
                                                        SET ron_lu = 1
                                                        WHERE name = ?""", (self.main.username.text(),))
                if 2 == self.take_ron_del.checkState():
                    self.c.execute("""UPDATE item
                                                        SET ron_del = 1
                                                        WHERE name = ?""", (self.main.username.text(),))
            else:
                if 2 == self.take_white_hat.checkState():
                    self.main.white_hat = 1
                if 2 == self.take_black_hat.checkState():
                    self.main.black_hat = 1
                if 2 == self.take_ron_va.checkState():
                    self.main.ron_va = 1
                if 2 == self.take_ron_te.checkState():
                    self.main.ron_te = 1
                if 2 == self.take_ron_lu.checkState():
                    self.main.ron_lu = 1
                if 2 == self.take_ron_del.checkState():
                    self.main.ron_del = 1
            self.no_money.setText("SUCCESSFUL")
            if 2 == self.take_white_hat.checkState():
                self.take_white_hat.setCheckState(Qt.Unchecked)
                self.take_white_hat.setEnabled(False)
            if 2 == self.take_black_hat.checkState():
                self.take_black_hat.setCheckState(Qt.Unchecked)
                self.take_black_hat.setEnabled(False)
            if 2 == self.take_ron_va.checkState():
                self.take_ron_va.setCheckState(Qt.Unchecked)
                self.take_ron_va.setEnabled(False)
            if 2 == self.take_ron_te.checkState():
                self.take_ron_te.setCheckState(Qt.Unchecked)
                self.take_ron_te.setEnabled(False)
            if 2 == self.take_ron_lu.checkState():
                self.take_ron_lu.setCheckState(Qt.Unchecked)
                self.take_ron_lu.setEnabled(False)
            if 2 == self.take_ron_del.checkState():
                self.take_ron_del.setCheckState(Qt.Unchecked)
                self.take_ron_del.setEnabled(False)
            self.main.money -= count
            self.the_money_lal.setText(str(int(self.the_money_lal.text()) - count))

    def change(self):
        if self.try_white_hat.isChecked():
            self.hat_lal.setPixmap(QPixmap("Pictures//dasabucket_sand6.png"))
        else:
            self.hat_lal.setPixmap(QPixmap('Pictures//dasabucket_bla6.png'))

    def stateChanged(self):
        if 2 == self.try_ron_del.checkState():
            self.ron_del_lal.setPixmap(QPixmap("Pictures//ron_del.png"))
        else:
            self.ron_del_lal.setPixmap(QPixmap(""))
        if 2 == self.try_ron_va.checkState():
            self.ron_va_lal.setPixmap(QPixmap("Pictures//ron_va6.png"))
        else:
            self.ron_va_lal.setPixmap(QPixmap(""))
        if 2 == self.try_ron_te.checkState():
            self.ron_te_lal.setPixmap(QPixmap("Pictures//ron_te.png"))
        else:
            self.ron_te_lal.setPixmap(QPixmap(""))
        if 2 == self.try_ron_lu.checkState():
            self.ron_lu_lal.setPixmap(QPixmap("Pictures//ron_lu.png"))
        else:
            self.ron_lu_lal.setPixmap(QPixmap(""))

    def closeEvent(self, a0):
        if self.main.log:
            self.con.commit()
            self.con.close()
