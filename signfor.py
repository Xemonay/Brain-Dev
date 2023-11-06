import sqlite3
from random import shuffle as sh, choices as chsax, choice as ch

from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QDialog, QLineEdit

from DesingPY.design_login import Ui_Form


class SignFor(QDialog, Ui_Form):
    def __init__(self, main):
        super().__init__()
        self.setupUi(self)
        self.con = sqlite3.connect("DataBases//accounts.sqlite")
        self.c = self.con.cursor()
        self.main = main
        self.okay.clicked.connect(self.okay_6)
        self.name_lal.textChanged.connect(self.clear1)
        self.pass_e.textChanged.connect(self.clear6)
        self.view.pressed.connect(self.check)
        self.view.released.connect(self.check6)
        self.bt_ture.setPixmap(QPixmap("Pictures//eye_closed_icon.png"))

    def check(self):
        self.pass_e.setEchoMode(QLineEdit.EchoMode.Normal)
        self.bt_ture.setPixmap(QPixmap("Pictures//eye_open_icon_1.png"))

    def check6(self):
        self.pass_e.setEchoMode(QLineEdit.EchoMode.Password)
        self.bt_ture.setPixmap(QPixmap("Pictures//eye_closed_icon.png"))

    def clear1(self):
        self.label.setText("")
        self.label_1.setText("")

    def clear6(self):
        self.label_6.setText("")

    def okay_6(self):
        good = True
        if not 2 <= len(self.name_lal.text()) <= 10:
            self.label.setText("Not correct Name")
            good = False
        name = self.name_lal.text()
        self.c.execute("""SELECT name FROM account
                  WHERE name = ?""", (name,))
        a = self.c.fetchall()
        if a:
            self.label_1.setText("The username is already occupied")
            good = False
        if not 6 <= len(self.pass_e.text()) <= 16:
            self.label_6.setText("Password is short")
            good = False
        if good:
            ax = list(chsax("IOASEJFIJSLIEasdaljfhafdvhiuRJGFLSIGHBVJXJXM164235", k=ch((6, 7, 8, 9, 10))))
            sh(ax)
            ax = "".join(ax)
            self.c.execute("""INSERT INTO account VALUES (?, ?, ?)""",
                           (name, "Pictures//Unknown_person01.jpg", "0"))
            self.c.execute("""INSERT INTO pass VALUES (?, ?)""", (name, ax))
            self.c.execute("""INSERT INTO item VALUES (?, ?, ?, ?, ?, ?, ?, ?, '0', '0', '0', '0', '0', 
            '0', ?)""", (name, self.main.money, str(self.main.white_hat), str(self.main.black_hat),
                         str(self.main.ron_va),
                         str(self.main.ron_del), str(self.main.ron_lu), str(self.main.ron_te),
                         self.main.player.volume()))
            self.c.execute("""INSERT INTO testx VALUES (?, ?)""", (name, self.pass_e.text()))
            self.c.execute("""INSERT INTO quickmath VALUES (?, ?, ?, ?, ?, ?)""", (
                name, self.main.lst_won[0] + self.main.lst_lost[0], str(self.main.lst_avgsec[0]), self.main.lst_won[0],
                self.main.lst_lost[0], self.main.lst_mist[0]))
            self.c.execute("""INSERT INTO spatialmem VALUES (?, ?, ?, ?, ?, ?)""", (
                name, self.main.lst_won[5] + self.main.lst_lost[5], str(self.main.lst_avgsec[5]), self.main.lst_won[5],
                self.main.lst_lost[5], self.main.lst_mist[5]))
            self.c.execute("""INSERT INTO unscramble VALUES (?, ?, ?, ?, ?, ?)""", (
                name, self.main.lst_won[4] + self.main.lst_lost[4], str(self.main.lst_avgsec[4]), self.main.lst_won[4],
                self.main.lst_lost[4], self.main.lst_mist[4]))
            self.c.execute("""INSERT INTO reaction VALUES (?, ?, ?, ?, ?, ?)""", (
                name, self.main.lst_won[3] + self.main.lst_lost[3], str(self.main.lst_avgsec[3]), self.main.lst_won[3],
                self.main.lst_lost[3], self.main.lst_mist[3]))
            self.c.execute("""INSERT INTO goword VALUES (?, ?, ?, ?, ?, ?)""", (
                name, self.main.lst_won[1] + self.main.lst_lost[1], str(self.main.lst_avgsec[1]), self.main.lst_won[1],
                self.main.lst_lost[1], self.main.lst_mist[1]))
            self.c.execute("""INSERT INTO attention VALUES (?, ?, ?, ?, ?, ?)""", (
                name, self.main.lst_won[2] + self.main.lst_lost[2], str(self.main.lst_avgsec[2]), self.main.lst_won[2],
                self.main.lst_lost[2], self.main.lst_mist[2]))
            self.c.execute("""INSERT INTO inventory VALUES (?, ?, ?, ?, ?, ?, ?)""",
                           (name, str(self.main.try_white_hat), str(self.main.try_black_hat),
                            str(self.main.try_ron_va), str(self.main.try_ron_del),
                            str(self.main.try_ron_te), str(self.main.try_ron_lu)))
            for x in range(len(self.main.lst_won)):
                if self.main.lst_won[x] > 0:
                    match x:
                        case 0:
                            self.c.execute("""UPDATE item
                                                SET quickmath = '1'
                                                            WHERE name = ?""", (name,))
                        case 1:
                            self.c.execute("""UPDATE item
                                                SET goword = '1'
                                                            WHERE name = ?""", (name,))
                        case 2:
                            self.c.execute("""UPDATE item
                                                SET attention = '1'
                                                            WHERE name = ?""", (name,))
                        case 3:
                            self.c.execute("""UPDATE item
                                                SET reaction = '1'
                                                            WHERE name = ?""", (name,))
                        case 4:
                            self.c.execute("""UPDATE item
                                                SET unscramble = '1'
                                                            WHERE name = ?""", (name,))
                        case 5:
                            self.c.execute("""UPDATE item
                                                SET spatialmem = '1'
                                                            WHERE name = ?""", (name,))
            self.main.login_bt.setText(name)
            self.main.login_bt.setEnabled(False)
            self.main.login_bt_2.hide()
            self.main.change_avatar('123')
            self.main.change_name(name)
            self.main.do_2.setEnabled(True)
            self.main.label.setText('')
            self.main.log = True
            self.main.login_bt_3.show()
            self.close()

    def closeEvent(self, a0):
        self.con.commit()
        self.con.close()
