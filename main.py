import sqlite3
import sys
from random import choice as ch

from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtGui import QPixmap, QImage, QTextCursor
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent, QMediaPlaylist
from PyQt5.QtPrintSupport import QPrinter, QPrintDialog, QPrintPreviewDialog
from PyQt5.QtWidgets import QApplication, QMainWindow

from DesingPY.design_main0 import Ui_MainWindow
from changeprofile import ChangeProfileForm
from howtoplay import Choice
from list_of_games import ListOfGames
from login import Login
from questionmark import Creator
from set_form import SetMusic
from shop import Shop
from signfor import SignFor
from stats6 import Sta

if hasattr(Qt, 'AA_EnableHighDpiScaling'):
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)

if hasattr(Qt, 'AA_UseHighDpiPixmaps'):
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps, True)


class BrainDevMain(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.lst_avgsec = [0, 0, 0, 0, 0, 0]
        self.lst_mist = [0, 0, 0, 0, 0, 0]
        self.lst_won = [0, 0, 0, 0, 0, 0]
        self.lst_lost = [0, 0, 0, 0, 0, 0]
        self.white_hat = 0
        self.black_hat = 0
        self.ron_va = 0
        self.ron_del = 0
        self.ron_te = 0
        self.ron_lu = 0
        self.try_white_hat = 0
        self.try_black_hat = 0
        self.try_ron_va = 0
        self.try_ron_del = 0
        self.try_ron_te = 0
        self.try_ron_lu = 0
        self.money = 0
        self.log = False
        self.qmstyle = "background-color:#F44336;color:white;border-style: outset;border-radius:10px;"
        self.gostyle = "background-color:#FFA726;color:white;border-style: outset;border-radius:10px;"
        self.atstyle = "background-color:#FDD835;color:white;border-style: outset;border-radius:10px;"
        self.rastyle = "background-color:#8BC34A;color:white;border-style: outset;border-radius:10px;"
        self.uastyle = "background-color:#B2EBF2;color:white;border-style: outset;border-radius:10px;"
        self.sastyle = "background-color:#3949AB;color:white;border-style: outset;border-radius:10px;"
        self.list_of_games_bt.clicked.connect(self.list_of_games_window)
        self.training_bt.clicked.connect(self.training)
        self.edit_profile_bt.clicked.connect(self.change_profile_form)
        self.what_is_that.clicked.connect(self.mystery_bt)
        self.music_lst1 = QMediaPlaylist(self)
        self.music_lst1.addMedia([QMediaContent(QUrl.fromLocalFile(
            r"Music\c418-haggstrom-minecraft-volume-alpha-savefrom.com.wav")),
            QMediaContent(QUrl.fromLocalFile(
                r"Music\c418-wet-hands-minecraft-volume-alpha-savefrom.com.wav")),
            QMediaContent(QUrl.fromLocalFile(
                r"Music\c418-droopy-likes-your-face-minecraft-volume-alpha-savefrom.live.wav")),
            QMediaContent(QUrl.fromLocalFile(
                r"Music\c418-subwoofer-lullaby-minecraft-volume-alpha-savefrom.live.wav")),
            QMediaContent(QUrl.fromLocalFile(
                r"Music\c418-sweden-minecraft-volume-alpha-savefrom.live.wav")),
            QMediaContent(QUrl.fromLocalFile(
                r"Music\c418-equinoxe-minecraft-volume-alpha-savefrom.live.wav"))])
        self.player = QMediaPlayer(self)
        self.music_lst1.setPlaybackMode(QMediaPlaylist.Loop)
        self.player.setPlaylist(self.music_lst1)
        self.player.play()
        self.shop_bt.clicked.connect(self.shop016)
        self.music_bt.clicked.connect(self.setting)
        self.edit_profile_bt.clicked.connect(self.change_profile_form)
        self.what_is_that.clicked.connect(self.mystery_bt)
        self.login_bt.clicked.connect(self.logx5)
        self.do_2.clicked.connect(self.do6)
        self.prep_t.clicked.connect(self.print_pre_d)
        self.pr_t.clicked.connect(self.pr)
        self.login_bt_2.clicked.connect(self.logx6)
        self.login_bt_3.hide()
        self.login_bt_3.clicked.connect(self.logout)
        self.status.clicked.connect(self.sta)
        self.status_8.clicked.connect(self.sta)
        self.status_2.clicked.connect(self.sta)
        self.status_6.clicked.connect(self.sta)
        self.status_5.clicked.connect(self.sta)
        self.status_7.clicked.connect(self.sta)

    def sta(self):
        self.TA = Sta(self)
        self.TA.show()

    def logout(self):
        self.log = False
        self.change_avatar("123")
        self.change_age("")
        self.login_bt_3.hide()
        self.login_bt_2.show()
        alpha = {0: self.status, 1: self.status_2, 2: self.status_6, 3: self.status_5, 5: self.status_7,
                 4: self.status_8}
        for x in range(6):
            alpha.get(x).setStyleSheet("background-color:#9E9E9E;color:white;border-style: "
                                       "outset;border-radius:10px;")
        self.change_name("User")
        self.login_bt.setText("Login")
        self.login_bt.setEnabled(True)
        self.lst_won = [0, 0, 0, 0, 0, 0]
        self.lst_lost = [0, 0, 0, 0, 0, 0]
        self.lst_mist = [0, 0, 0, 0, 0, 0]
        self.lst_avgsec = [0, 0, 0, 0, 0, 0]
        self.white_hat = 0
        self.black_hat = 0
        self.ron_va = 0
        self.ron_del = 0
        self.ron_te = 0
        self.ron_lu = 0
        self.do_2.setEnabled(False)
        self.prep_t.setEnabled(False)
        self.pr_t.setEnabled(False)
        self.textEdit.clear()
        self.label.setText('Please login to do')
        self.hat_lal.setPixmap(QPixmap(''))
        self.ron_va_lal.setPixmap(QPixmap(''))
        self.ron_te_lal.setPixmap(QPixmap(''))
        self.ron_lu_lal.setPixmap(QPixmap(''))
        self.ron_del_lal.setPixmap(QPixmap(''))
        self.try_white_hat = 0
        self.try_black_hat = 0
        self.try_ron_va = 0
        self.try_ron_del = 0
        self.try_ron_te = 0
        self.try_ron_lu = 0
        self.money = 0

    def do6(self):
        self.textEdit.clear()
        document = self.textEdit.document()
        cursor = QTextCursor(document)
        con = sqlite3.connect('DataBases//accounts.sqlite')
        c = con.cursor()
        a = c.execute('''SELECT avatar FROM account
                        WHERE name = ?''', (self.username.text(),)).fetchone()[0]
        cursor.insertImage(a)
        cursor.insertText('\t' + self.username.text())
        cursor.insertText('\t\tITEMS:\t\t')
        a = c.execute('''SELECT hat1, hat2, ron_va, ron_del, ron_lu, ron_te FROM item
                        WHERE name = ?''', (self.username.text(),)).fetchall()[0]
        for x in range(len(a)):
            if a[x] == '1':
                match x:
                    case 0:
                        cursor.insertImage('Pictures//dasabucket_sand6.png')
                    case 1:
                        cursor.insertImage('Pictures//dasabucket_bla6.png')
                    case 2:
                        cursor.insertImage('Pictures//ron_va6.png')
                    case 3:
                        cursor.insertImage('Pictures//ron_del.png')
                    case 4:
                        cursor.insertImage('Pictures//ron_lu.png')
                    case 5:
                        cursor.insertImage('Pictures//ron_te.png')
        lst_won6 = []
        lst_mist6 = []
        lst_lost6 = []
        lst_avgsec6 = []
        a = c.execute('''SELECT avgsec, won, lost, mistakes FROM quickmath
                            WHERE name = ?''', (self.username.text(),)).fetchall()[0]
        lst_won6.append(a[1])
        lst_mist6.append(a[3])
        lst_lost6.append(a[2])
        lst_avgsec6.append(a[0])
        a = c.execute('''SELECT avgsec, won, lost, mistakes FROM goword
                                    WHERE name = ?''', (self.username.text(),)).fetchall()[0]
        lst_won6.append(a[1])
        lst_mist6.append(a[3])
        lst_lost6.append(a[2])
        lst_avgsec6.append(a[0])
        a = c.execute('''SELECT avgsec, won, lost, mistakes FROM attention
                                    WHERE name = ?''', (self.username.text(),)).fetchall()[0]
        lst_won6.append(a[1])
        lst_mist6.append(a[3])
        lst_lost6.append(a[2])
        lst_avgsec6.append(a[0])
        a = c.execute('''SELECT avgsec, won, lost, mistakes FROM reaction
                                    WHERE name = ?''', (self.username.text(),)).fetchall()[0]
        lst_won6.append(a[1])
        lst_mist6.append(a[3])
        lst_lost6.append(a[2])
        lst_avgsec6.append(a[0])
        a = c.execute('''SELECT avgsec, won, lost, mistakes FROM unscramble
                                    WHERE name = ?''', (self.username.text(),)).fetchall()[0]
        lst_won6.append(a[1])
        lst_mist6.append(a[3])
        lst_lost6.append(a[2])
        lst_avgsec6.append(a[0])
        a = c.execute('''SELECT avgsec, won, lost, mistakes FROM spatialmem
                                    WHERE name = ?''', (self.username.text(),)).fetchall()[0]
        lst_won6.append(a[1])
        lst_mist6.append(a[3])
        lst_lost6.append(a[2])
        lst_avgsec6.append(a[0])
        cursor.insertText(f'\n\nQuickmath: \n\tWon: {lst_won6[0]}\n\tLost: {lst_lost6[0]}\n\tPlayed: '
                          f'{lst_won6[0] + lst_lost6[0]}\n\tAv Time: {lst_avgsec6[0]}\n\tMistakes:'
                          f'{lst_mist6[0]}\t')
        cursor.insertText(f'\nGOWORD: \n\tWon: {lst_won6[1]}\n\tLost: {lst_lost6[1]}\n\tPlayed: '
                          f'{lst_won6[1] + lst_lost6[1]}\n\tAv Time: {lst_avgsec6[1]}\n\tMistakes:'
                          f'{lst_mist6[1]}\t')
        cursor.insertText(f'\nAttention: \n\tWon: {lst_won6[2]}\n\tLost: {lst_lost6[2]}\n\tPlayed: '
                          f'{lst_won6[2] + lst_lost6[2]}\n\tAv Time: {lst_avgsec6[2]}\n\tMistakes:'
                          f'{lst_mist6[2]}\t')
        cursor.insertText(f'\nReaction: \n\tWon: {lst_won6[3]}\n\tLost: {lst_lost6[3]}\n\tPlayed: '
                          f'{lst_won6[3] + lst_lost6[3]}\n\tAv Time: {lst_avgsec6[3]}\n\tMistakes:'
                          f'{lst_mist6[3]}\t')
        cursor.insertText(f'\nSpatialMemory: \n\tWon: {lst_won6[5]}\n\tLost: {lst_lost6[5]}\n\tPlayed: '
                          f'{lst_won6[5] + lst_lost6[5]}\n\tAv Time: {lst_avgsec6[5]}\n\tMistakes:'
                          f'{lst_mist6[5]}\t')
        cursor.insertText(f'\nUnscramble: \n\tWon: {lst_won6[4]}\n\tLost: {lst_lost6[4]}\n\tPlayed: '
                          f'{lst_won6[4] + lst_lost6[4]}\n\tAv Time: {lst_avgsec6[4]}\n\tMistakes:'
                          f'{lst_mist6[4]}\t')
        self.prep_t.setEnabled(True)
        self.pr_t.setEnabled(True)
        con.close()

    def pr(self):
        printer = QPrinter(QPrinter.HighResolution)
        dialog = QPrintDialog(printer, self)
        if dialog.exec_() == QPrintDialog.Accepted:
            self.textEdit.print_(printer)

    def shop016(self):
        self.shop = Shop(self)
        self.shop.show()

    def logx5(self):
        self.logx = Login(self)
        self.logx.show()

    def logx6(self):
        self.logx = SignFor(self)
        self.logx.show()

    def print_pre(self, printer):
        self.textEdit.print_(printer)

    def print_pre_d(self):
        printer = QPrinter(QPrinter.HighResolution)
        prev_de = QPrintPreviewDialog(printer, self)
        prev_de.paintRequested.connect(self.print_pre)
        prev_de.exec_()

    def change_avatar(self, a):
        corr = sqlite3.connect("DataBases//accounts.sqlite")
        c = corr.cursor()
        fname = c.execute("""SELECT avatar FROM account
                            WHERE name = ?""", (a,)).fetchall()[0][0]
        img = QImage(185, 205, QImage.Format_ARGB32)
        img.load(fname)
        self.avatar.setPixmap(QPixmap(img))
        corr.commit()
        corr.close()

    def change_name(self, a):
        self.username.setText(a)

    def change_age(self, a):
        self.age.setText(a)

    def change_profile_form(self):
        self.change_form = ChangeProfileForm(self)
        self.change_form.show()

    def list_of_games_window(self):
        self.list_of_games = ListOfGames(self)
        self.list_of_games.show()

    def setting(self):
        self.set = SetMusic(self)
        self.set.show()

    def training(self):
        eval(ch(["self.quick_math()", "self.goword()", "self.attention()", "self.reaction()", "self.spatial_mem()",
                 "self.unscramble()"]))

    def quick_math(self):
        self.how = Choice(self, "QuickMath")

    def goword(self):
        self.how = Choice(self, "GOWORD")

    def attention(self):
        self.how = Choice(self, "Attention")

    def reaction(self):
        self.how = Choice(self, "Reaction")

    def spatial_mem(self):
        self.how = Choice(self, "SpatialMem")

    def unscramble(self):
        self.how = Choice(self, "Unscramble")

    def mystery_bt(self):
        self.questionmark = Creator()
        self.questionmark.show()

    def closeEvent(self, a0):
        if self.log:
            self.logout()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = BrainDevMain()
    ex.show()
    sys.exit(app.exec_())
