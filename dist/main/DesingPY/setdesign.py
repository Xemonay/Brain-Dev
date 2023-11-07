# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'set.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        Form.setStyleSheet("background-color: black;\n"
"")
        self.volume_ll = QtWidgets.QLabel(Form)
        self.volume_ll.setGeometry(QtCore.QRect(130, 20, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft Tai Le")
        font.setPointSize(16)
        self.volume_ll.setFont(font)
        self.volume_ll.setStyleSheet("color: white;\n"
"background-color: #FFC107;\n"
"")
        self.volume_ll.setObjectName("volume_ll")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(30, 130, 221, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft Tai Le")
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: white;\n"
"background-color: #FFC107;\n"
"")
        self.label_2.setObjectName("label_2")
        self.change_msc = QtWidgets.QPushButton(Form)
        self.change_msc.setGeometry(QtCore.QRect(280, 130, 75, 23))
        self.change_msc.setStyleSheet("color: white;\n"
"background-color: #FFC107;\n"
"")
        self.change_msc.setObjectName("change_msc")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(100, 170, 71, 16))
        self.label_3.setStyleSheet("color: white;\n"
"background-color: #FFC107;\n"
"")
        self.label_3.setObjectName("label_3")
        self.horizontalSliderL = QtWidgets.QSlider(Form)
        self.horizontalSliderL.setGeometry(QtCore.QRect(29, 80, 341, 22))
        self.horizontalSliderL.setStyleSheet("color: white;\n"
"background-color: #616161;\n"
"")
        self.horizontalSliderL.setMaximum(100)
        self.horizontalSliderL.setProperty("value", 100)
        self.horizontalSliderL.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSliderL.setObjectName("horizontalSliderL")
        self.next_music = QtWidgets.QPushButton(Form)
        self.next_music.setGeometry(QtCore.QRect(280, 20, 75, 23))
        self.next_music.setStyleSheet("color: white;\n"
"background-color: #FF9800;\n"
"")
        self.next_music.setObjectName("next_music")
        self.pre_music = QtWidgets.QPushButton(Form)
        self.pre_music.setGeometry(QtCore.QRect(30, 20, 75, 23))
        self.pre_music.setStyleSheet("color: white;\n"
"background-color: #FF9800;\n"
"")
        self.pre_music.setObjectName("pre_music")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(30, 220, 261, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft Tai Le")
        font.setPointSize(16)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: white;\n"
"background-color: #FFC107;\n"
"")
        self.label_4.setObjectName("label_4")
        self.change_msc_0 = QtWidgets.QPushButton(Form)
        self.change_msc_0.setGeometry(QtCore.QRect(310, 220, 75, 23))
        self.change_msc_0.setStyleSheet("color: white;\n"
"background-color: #FFC107;\n"
"")
        self.change_msc_0.setObjectName("change_msc_0")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Set"))
        self.volume_ll.setText(_translate("Form", "    Volume:"))
        self.label_2.setText(_translate("Form", "Change to YOUR Music"))
        self.change_msc.setText(_translate("Form", "CHANGE"))
        self.label_3.setText(_translate("Form", "WAV FORMAT"))
        self.next_music.setText(_translate("Form", "NEXT"))
        self.pre_music.setText(_translate("Form", "PREV"))
        self.label_4.setText(_translate("Form", "Change to DEFAULT MUSIC"))
        self.change_msc_0.setText(_translate("Form", "CHANGE"))