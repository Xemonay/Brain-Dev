import sqlite3

from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QDialog, QLineEdit

from DesingPY.design_login1 import Ui_Form


class Login(QDialog, Ui_Form):
    def __init__(self, main):
        super().__init__()
        self.setupUi(self)
        self.main = main
        self.okay.clicked.connect(self.okay_6)
        self.name_lal.textChanged.connect(self.clear1)
        self.bt_ture.setPixmap(QPixmap("Pictures//eye_closed_icon.png"))
        self.view.pressed.connect(self.check)
        self.view.released.connect(self.check6)
        self.pass_e.textChanged.connect(self.clear1)
        self.name_lal.setFocus()
        self.con = sqlite3.connect("DataBases//accounts.sqlite")
        self.c = self.con.cursor()

    def check(self):
        self.pass_e.setEchoMode(QLineEdit.EchoMode.Normal)
        self.bt_ture.setPixmap(QPixmap("Pictures//eye_open_icon_1.png"))

    def check6(self):
        self.pass_e.setEchoMode(QLineEdit.EchoMode.Password)
        self.bt_ture.setPixmap(QPixmap("Pictures//eye_closed_icon.png"))

    def clear1(self):
        self.label_1.setText("")

    def okay_6(self):
        name = self.name_lal.text()
        pass_a = self.pass_e.text()
        a = self.c.execute("""SELECT name FROM testx
                    WHERE question = ? AND name = ?""", (pass_a, name,)).fetchone()
        if a:
            self.main.do_2.setEnabled(True)
            self.main.label.setText('')
            self.main.try_white_hat = 0
            self.main.try_black_hat = 0
            self.main.try_ron_va = 0
            self.main.try_ron_del = 0
            self.main.try_ron_te = 0
            self.main.try_ron_lu = 0
            self.main.white_hat = 0
            self.main_black_hat = 0
            self.main.ron_va = 0
            self.main.ron_te = 0
            self.main.ron_del = 0
            self.main.ron_lu = 0
            self.main.money = 0
            self.main.lst_won = [0, 0, 0, 0, 0, 0]
            self.main.lst_lost = [0, 0, 0, 0, 0, 0]
            self.main.lst_mist = [0, 0, 0, 0, 0, 0]
            self.main.lst_avgsec = [0, 0, 0, 0, 0, 0]
            self.main.hat_lal.setPixmap(QPixmap(''))
            self.main.ron_va_lal.setPixmap(QPixmap(''))
            self.main.ron_te_lal.setPixmap(QPixmap(''))
            self.main.ron_lu_lal.setPixmap(QPixmap(''))
            self.main.ron_del_lal.setPixmap(QPixmap(''))
            alpha = {0: self.main.status, 1: self.main.status_2, 2: self.main.status_6, 3: self.main.status_5,
                     5: self.main.status_7, 4: self.main.status_8}
            for x in range(6):
                alpha.get(x).setStyleSheet("background-color:#9E9E9E;color:white;border-style: "
                                           "outset;border-radius:10px;")
            self.main.login_bt.setEnabled(False)
            self.main.login_bt.setText(name)
            self.main.log = True
            self.main.change_name(name)
            self.main.change_avatar(name)
            self.main.change_age(self.c.execute("""SELECT age FROM account
                                            WHERE name = ?""", (name,)).fetchone()[0])
            self.main.login_bt_2.hide()
            a = self.c.execute("""SELECT quickmath, goword, attention, reaction, spatialmem, 
            unscramble FROM item
                                                            WHERE name = ?""", (self.main.username.text(),
                                                                                )).fetchall()[
                0]
            for x in range(len(a)):
                match x:
                    case 0:
                        ac = self.main.qmstyle
                    case 1:
                        ac = self.main.gostyle
                    case 2:
                        ac = self.main.atstyle
                    case 3:
                        ac = self.main.rastyle
                    case 5:
                        ac = self.main.uastyle
                    case 4:
                        ac = self.main.sastyle
                if a[x] == "1":
                    alpha.get(x).setStyleSheet(ac)
            a = self.c.execute('''SELECT white_hat, black_hat, ron_va, ron_del, ron_te, ron_lu FROM inventory
                        WHERE name = ?''', (self.main.username.text(),)).fetchall()[0]
            for x in range(len(a)):
                if a[x] == "1":
                    match x:
                        case 0:
                            self.main.hat_lal.setPixmap(QPixmap('Pictures//dasabucket_sand6.png'))
                        case 1:
                            self.main.hat_lal.setPixmap(QPixmap('Pictures//dasabucket_bla6.png'))
                        case 2:
                            self.main.ron_va_lal.setPixmap(QPixmap('Pictures//ron_va6.png'))
                        case 3:
                            self.main.ron_del_lal.setPixmap(QPixmap('Pictures//ron_del.png'))
                        case 4:
                            self.main.ron_te_lal.setPixmap(QPixmap('Pictures//ron_te.png'))
                        case 5:
                            self.main.ron_lu_lal.setPixmap(QPixmap('Pictures//ron_lu.png'))
            self.main.login_bt_3.show()
            self.close()
        else:
            self.pass_e.setText("")
            self.label_1.setText("Login or Pass isn't correct")

    def closeEvent(self, a0):
        if self.main.log:
            afs = self.con.cursor().execute('''SELECT music FROM item
                                                    WHERE name = ?'''
                                            '', (self.main.username.text(),)).fetchone()[0]
            self.main.player.setVolume(afs)
        self.con.commit()
        self.con.close()
