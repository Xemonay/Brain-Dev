import sqlite3

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QDialog, QFileDialog

from DesingPY.design_changeform import Ui_Dialog


class ChangeProfileForm(QDialog, Ui_Dialog):
    def __init__(self, main):
        super().__init__()
        self.main = main
        self.setupUi(self)
        self.unwear.clicked.connect(self.unwear26)
        self.change_avatar_bt.clicked.connect(self.change_avatar)
        self.okay_name_bt.clicked.connect(self.change_name)
        self.okay_age_bt.clicked.connect(self.change_age)
        self.try_white_hat.toggled.connect(self.wear)
        self.try_black_hat.toggled.connect(self.wear)
        self.try_ron_del.toggled.connect(self.wear)
        self.try_ron_te.toggled.connect(self.wear)
        self.try_ron_va.toggled.connect(self.wear)
        self.try_ron_lu.toggled.connect(self.wear)
        self.try_white_hat.setEnabled(False)
        self.try_black_hat.setEnabled(False)
        self.try_ron_va.setEnabled(False)
        self.try_ron_te.setEnabled(False)
        self.try_ron_del.setEnabled(False)
        self.try_ron_lu.setEnabled(False)
        if main.log:
            con = sqlite3.connect('DataBases//accounts.sqlite')
            c = con.cursor()
            a = c.execute('''SELECT hat1, hat2, ron_va, ron_del, ron_lu, ron_te FROM item
                                WHERE name = ?''', (main.username.text(),)).fetchall()[0]
            for x in range(len(a)):
                if a[x] == "1":
                    match x:
                        case 0:
                            self.try_white_hat.setEnabled(True)
                        case 1:
                            self.try_black_hat.setEnabled(True)
                        case 2:
                            self.try_ron_va.setEnabled(True)
                        case 3:
                            self.try_ron_del.setEnabled(True)
                        case 4:
                            self.try_ron_lu.setEnabled(True)
                        case 5:
                            self.try_ron_te.setEnabled(True)
            a = c.execute('''SELECT white_hat, black_hat, ron_va, ron_del, ron_te, ron_lu FROM inventory
                                            WHERE name = ?''', (self.main.username.text(),)).fetchall()[0]
            con.commit()
            con.close()
            for x in range(len(a)):
                if a[x] == "1":
                    match x:
                        case 0:
                            self.try_white_hat.setChecked(Qt.Checked)
                        case 1:
                            self.try_black_hat.setChecked(Qt.Checked)
                        case 2:
                            self.try_ron_va.setChecked(Qt.Checked)
                        case 3:
                            self.try_ron_del.setChecked(Qt.Checked)
                        case 4:
                            self.try_ron_te.setChecked(Qt.Checked)
                        case 5:
                            self.try_ron_lu.setChecked(Qt.Checked)
        else:
            if self.main.try_white_hat:
                self.try_white_hat.setChecked(Qt.Checked)
            if self.main.try_black_hat:
                self.try_black_hat.setChecked(Qt.Checked)
            if self.main.try_ron_va:
                self.try_ron_va.setChecked(Qt.Checked)
            if self.main.try_ron_del:
                self.try_ron_del.setChecked(Qt.Checked)
            if self.main.try_ron_te:
                self.try_ron_te.setChecked(Qt.Checked)
            if self.main.try_ron_lu:
                self.try_ron_lu.setChecked(Qt.Checked)
            if main.white_hat == 1:
                self.try_white_hat.setEnabled(True)
            if main.black_hat == 1:
                self.try_black_hat.setEnabled(True)
            if main.ron_va == 1:
                self.try_ron_va.setEnabled(True)
            if main.ron_te == 1:
                self.try_ron_te.setEnabled(True)
            if main.ron_del == 1:
                self.try_ron_del.setEnabled(True)
            if main.ron_lu == 1:
                self.try_ron_lu.setEnabled(True)

    def wear(self):
        if self.try_white_hat.isChecked():
            self.main.hat_lal.setPixmap(QPixmap("Pictures//dasabucket_sand6.png"))
            self.main.try_white_hat = 1
            self.main.try_black_hat = 0
        elif self.try_black_hat.isChecked():
            self.main.hat_lal.setPixmap(QPixmap('Pictures//dasabucket_bla6.png'))
            self.main.try_black_hat = 1
            self.main.try_white_hat = 0
        if self.try_ron_va.isChecked():
            self.main.ron_va_lal.setPixmap(QPixmap('Pictures//ron_va6.png'))
            self.main.try_ron_va = 1
        else:
            self.main.ron_va_lal.setPixmap(QPixmap(''))
            self.main.try_ron_va = 0
        if self.try_ron_del.isChecked():
            self.main.ron_del_lal.setPixmap(QPixmap('Pictures//ron_del.png'))
            self.main.try_ron_del = 1
        else:
            self.main.ron_del_lal.setPixmap(QPixmap(''))
            self.main.try_ron_del = 0
        if self.try_ron_te.isChecked():
            self.main.ron_te_lal.setPixmap(QPixmap('Pictures//ron_te.png'))
            self.main.try_ron_te = 1
        else:
            self.main.ron_te_lal.setPixmap(QPixmap(''))
            self.main.try_ron_te = 0
        if self.try_ron_lu.isChecked():
            self.main.ron_lu_lal.setPixmap(QPixmap('Pictures//ron_lu.png'))
            self.main.try_ron_lu = 1
        else:
            self.main.ron_lu_lal.setPixmap(QPixmap(''))
            self.main.try_ron_lu = 0
        if self.main.log:
            con = sqlite3.connect('DataBases//accounts.sqlite')
            c = con.cursor()
            if self.main.try_white_hat:
                c.execute('''UPDATE inventory
                                SET white_hat = "1"
                                    WHERE name = ?''', (self.main.username.text(),))
            else:
                c.execute('''UPDATE inventory
                                                SET white_hat = "0"
                                                    WHERE name = ?''', (self.main.username.text(),))
            if self.main.try_black_hat:
                c.execute('''UPDATE inventory
                                SET black_hat = "1"
                                    WHERE name = ?''', (self.main.username.text(),))
            else:
                c.execute('''UPDATE inventory
                                                SET black_hat = "0"
                                                    WHERE name = ?''', (self.main.username.text(),))
            if self.main.try_ron_va:
                c.execute('''UPDATE inventory
                                SET ron_va = "1"
                                    WHERE name = ?''', (self.main.username.text(),))
            else:
                c.execute('''UPDATE inventory
                                                SET ron_va = "0"
                                                    WHERE name = ?''', (self.main.username.text(),))
            if self.main.try_ron_del:
                c.execute('''UPDATE inventory
                                SET ron_del = "1"
                                    WHERE name = ?''', (self.main.username.text(),))
            else:
                c.execute('''UPDATE inventory
                                                SET ron_del = "0"
                                                    WHERE name = ?''', (self.main.username.text(),))
            if self.main.try_ron_lu:
                c.execute('''UPDATE inventory
                                SET ron_lu = "1"
                                    WHERE name = ?''', (self.main.username.text(),))
            else:
                c.execute('''UPDATE inventory
                                                SET ron_lu = "0"
                                                    WHERE name = ?''', (self.main.username.text(),))
            if self.main.try_ron_te:
                c.execute('''UPDATE inventory
                                SET ron_te = "1"
                                    WHERE name = ?''', (self.main.username.text(),))
            else:
                c.execute('''UPDATE inventory
                                                SET ron_te = "0"
                                                    WHERE name = ?''', (self.main.username.text(),))
            con.commit()
            con.close()

    def unwear26(self):
        self.main.hat_lal.setPixmap(QPixmap(''))
        self.try_white_hat.setChecked(False)
        self.try_black_hat.setChecked(False)

    def change_avatar(self):
        fname = QFileDialog.getOpenFileName(self, 'Choose png', '')[0]
        img = QImage(185, 205, QImage.Format_ARGB32)
        if fname == '':
            fname = 'Pictures//Unknown_person01.jpg'
        img.load(fname)
        self.file_name_label.setText(fname)
        self.main.avatar.setPixmap(QPixmap(img))
        if self.main.log:
            con = sqlite3.connect('DataBases//accounts.sqlite')
            c = con.cursor()
            c.execute("""UPDATE account
                        SET avatar = ?
                        WHERE name = ?""", (fname, self.main.username.text()))
            con.commit()
            con.close()

    def change_name(self):
        if self.main.log:
            con = sqlite3.connect('DataBases//accounts.sqlite')
            c = con.cursor()
            c.execute("""UPDATE account
                        SET name = ?
                        WHERE name = ?""", (self.change_name_edt.text(), self.main.username.text()))
            c.execute("""UPDATE item
                                    SET name = ?
                                    WHERE name = ?""", (self.change_name_edt.text(),
                                                        self.main.username.text()))
            c.execute("""UPDATE testx
                                    SET name = ?
                                    WHERE name = ?""", (self.change_name_edt.text(),
                                                        self.main.username.text()))
            c.execute("""UPDATE pass
                                    SET name = ?
                                    WHERE name = ?""", (self.change_name_edt.text(),
                                                        self.main.username.text()))
            self.main.login_bt.setText(self.change_name_edt.text())
            con.commit()
            con.close()
        self.main.username.setText(self.change_name_edt.text())

    def change_age(self):
        try:
            self.main.age.setText("Age = " + str(int(self.change_age_edt.text())))
            self.not_correct_age_label.setText("")
            if self.main.log:
                con = sqlite3.connect('DataBases//accounts.sqlite')
                c = con.cursor()
                c.execute("""UPDATE account
                                    SET age = ?
                                    WHERE name = ?""", (self.main.age.text(), self.main.username.text()))
                con.commit()
                con.close()

        except ValueError:
            self.not_correct_age_label.setText("Not correct age entered")
