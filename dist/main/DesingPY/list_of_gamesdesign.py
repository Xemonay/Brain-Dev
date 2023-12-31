# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'list_of_games.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(366, 545)
        MainWindow.setMinimumSize(QtCore.QSize(366, 545))
        MainWindow.setMaximumSize(QtCore.QSize(366, 545))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.quick_math_bt = QtWidgets.QPushButton(self.centralwidget)
        self.quick_math_bt.setGeometry(QtCore.QRect(110, 30, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Microsoft Tai Le")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.quick_math_bt.setFont(font)
        self.quick_math_bt.setStyleSheet("background-color:#F44336;\n"
"color:white;\n"
"border-style: outset;\n"
"border-radius:10px;")
        self.quick_math_bt.setObjectName("quick_math_bt")
        self.math_bt = QtWidgets.QPushButton(self.centralwidget)
        self.math_bt.setGeometry(QtCore.QRect(110, 110, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Microsoft Tai Le")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.math_bt.setFont(font)
        self.math_bt.setStyleSheet("background-color:#FFA726;\n"
"color:white;\n"
"border-style: outset;\n"
"border-radius:10px;")
        self.math_bt.setObjectName("math_bt")
        self.attention_bt = QtWidgets.QPushButton(self.centralwidget)
        self.attention_bt.setGeometry(QtCore.QRect(110, 190, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Microsoft Tai Le")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.attention_bt.setFont(font)
        self.attention_bt.setStyleSheet("background-color:#FDD835;\n"
"color:white;\n"
"border-style: outset;\n"
"border-radius:10px;")
        self.attention_bt.setObjectName("attention_bt")
        self.reaction_bt = QtWidgets.QPushButton(self.centralwidget)
        self.reaction_bt.setGeometry(QtCore.QRect(110, 270, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Microsoft Tai Le")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.reaction_bt.setFont(font)
        self.reaction_bt.setStyleSheet("background-color:#8BC34A;\n"
"color:white;\n"
"border-style: outset;\n"
"border-radius:10px;")
        self.reaction_bt.setObjectName("reaction_bt")
        self.spatial_mem_bt = QtWidgets.QPushButton(self.centralwidget)
        self.spatial_mem_bt.setGeometry(QtCore.QRect(110, 350, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Microsoft Tai Le")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.spatial_mem_bt.setFont(font)
        self.spatial_mem_bt.setStyleSheet("background-color:#B2EBF2;\n"
"color:white;\n"
"border-style: outset;\n"
"border-radius:10px;")
        self.spatial_mem_bt.setObjectName("spatial_mem_bt")
        self.unscramble_bt = QtWidgets.QPushButton(self.centralwidget)
        self.unscramble_bt.setGeometry(QtCore.QRect(110, 430, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Microsoft Tai Le")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.unscramble_bt.setFont(font)
        self.unscramble_bt.setStyleSheet("background-color:#3949AB;\n"
"color:white;\n"
"border-style: outset;\n"
"border-radius:10px;")
        self.unscramble_bt.setObjectName("unscramble_bt")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 366, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "List of Games"))
        self.quick_math_bt.setText(_translate("MainWindow", "Quick Math"))
        self.math_bt.setText(_translate("MainWindow", "GOWORD"))
        self.attention_bt.setText(_translate("MainWindow", "Attention"))
        self.reaction_bt.setText(_translate("MainWindow", "Reaction"))
        self.spatial_mem_bt.setText(_translate("MainWindow", "Spatial Mem"))
        self.unscramble_bt.setText(_translate("MainWindow", "Unscramble"))
