# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PokazSchet.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5.QtGui import QIcon
from UI_CLASS_KOMM import *


class UiWinPokazanya(object):
    def setupUi_PS(self, WinPokazanya):
        self.WinPokazanya = WinPokazanya
        self.WinPokazanya.setObjectName("PokazanyaSchet")
        self.WinPokazanya.setWindowModality(QtCore.Qt.ApplicationModal)
        self.WinPokazanya.resize(800, 400)
        self.WinPokazanya.setGeometry(QtCore.QRect(560, 200, 800, 400))
        self.WinPokazanya.setMinimumSize(QtCore.QSize(800, 400))
        self.WinPokazanya.setMaximumSize(QtCore.QSize(800, 400))
        self.WinPokazanya.setWindowTitle('ПОКАЗАНИЯ СЧЕТЧИКОВ')
        self.WinPokazanya.setWindowIcon(QIcon('Resource/img/euro.png'))
        self.WinPokazanya.setStyleSheet("background-color: rgb(78, 79, 84);")

        self.label_month_year_PS, self.btn_Left_PS, self.btn_Right_PS, self.label_OK_PS = ui_win_head(WinPokazanya)
        self.comboBox_month_PS, self.comboBox_year_PS, self.label_ERROR_PS, self.checkBox_Edit_PS, \
        self.pushButton_Save_PS, self.pushButton_Cancel_PS = ui_win_combobox(WinPokazanya)

        self.groupPowerBox = QtWidgets.QGroupBox("Электроэнергия", self.WinPokazanya)
        self.groupPowerBox.setGeometry(QtCore.QRect(10, 50, 230, 300))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.groupPowerBox.setFont(font)
        self.groupPowerBox.setStyleSheet("font-weight: 700;\n color: rgb(209, 209, 217);\n padding: .5em 1em; \n "
                                         "border-radius: 5px; \n border: 1px solid rgba(209, 209, 217, 240);")
        self.groupPowerBox.setAlignment(QtCore.Qt.AlignCenter)
        self.groupPowerBox.setObjectName("groupPowerBox")

        self.label_raschet_schet_P = label("Р/С 171 269 - 5", self.groupPowerBox, 10, 30, 210, 25)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_raschet_schet_P.setFont(font)
        self.label_raschet_schet_P.setStyleSheet("color: rgb(80, 80, 80); \n background-color: rgb(255, 255, 0); \n "
                                                 "font-weight: 700; \n padding: .4em; \n "
                                                 "border: 1px solid rgba(50, 50, 50, 240); \n border-radius: 4px; \n ")

        label("предыдущие", self.groupPowerBox, 10, 55, 100, 25)
        label("последние", self.groupPowerBox, 120, 55, 100, 25)
        label("месячный расход", self.groupPowerBox, 10, 235, 210, 25)

        color = "(0, 160, 0)"
        grad_1 = "(91, 92, 96, 255)"
        grad_2 = "(108, 109, 114, 255)"

        self.lineEdit_pred_pokaz_P = line_edit_pokaz(self.groupPowerBox, 10, 80, 100, 150, color, grad_1, grad_2)
        self.lineEdit_post_pokaz_P = line_edit_pokaz(self.groupPowerBox, 120, 80, 100, 150, color, grad_2, grad_1)
        self.lineEdit_post_pokaz_P.setReadOnly(False)

        self.label_month_ras_P = label_month_ras("", self.groupPowerBox, 10, 260, 210, 30, color, grad_1, grad_2)

        self.groupWaterBox = QtWidgets.QGroupBox("Вода", self.WinPokazanya)
        self.groupWaterBox.setGeometry(QtCore.QRect(250, 50, 300, 300))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.groupWaterBox.setFont(font)
        self.groupWaterBox.setStyleSheet("font-weight: 700;\n color: rgb(209, 209, 217);\n padding: .5em 1em; \n "
                                         "border-radius: 5px; \n border: 1px solid rgba(209, 209, 217, 240);")
        self.groupWaterBox.setAlignment(QtCore.Qt.AlignCenter)
        self.groupWaterBox.setObjectName("groupWaterBox")

        self.label_raschet_schet_W = label("Р/С 300 046 056 19", self.groupWaterBox, 10, 30, 280, 25)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_raschet_schet_W.setFont(font)
        self.label_raschet_schet_W.setStyleSheet("color: rgb(80, 80, 80); \n background-color: rgb(85, 170, 255); \n "
                                                 "font-weight: 700; \n padding: .4em; \n "
                                                 "border: 1px solid rgba(50, 50, 50, 240); \n border-radius: 4px; \n ")

        label("счетчик", self.groupWaterBox, 10, 55, 100, 25)
        label("предыдущие", self.groupWaterBox, 110, 55, 100, 25)
        label("последние", self.groupWaterBox, 210, 55, 80, 25)
        label("месячный расход", self.groupWaterBox, 10, 235, 280, 25)

        self.number_1 = label("№1", self.groupWaterBox, 10, 80, 25, 30)
        self.number_1.setStyleSheet("font-weight: 600; \n color: rgb(209, 209, 217); \n padding: .1em; \n border: 0px;")
        self.number_2 = label("№2", self.groupWaterBox, 10, 120, 25, 30)
        self.number_2.setStyleSheet("font-weight: 600; \n color: rgb(209, 209, 217); \n padding: .1em; \n border: 0px;")
        self.number_3 = label("№3", self.groupWaterBox, 10, 160, 25, 30)
        self.number_3.setStyleSheet("font-weight: 600; \n color: rgb(209, 209, 217); \n padding: .1em; \n border: 0px;")
        self.number_4 = label("№4", self.groupWaterBox, 10, 200, 25, 30)
        self.number_4.setStyleSheet("font-weight: 600; \n color: rgb(209, 209, 217); \n padding: .1em; \n border: 0px;")

        label_place("Туалет (хл)", self.groupWaterBox, 40, 80, 80, 30, "(0, 170, 255)")
        label_place("Туалет (гр)", self.groupWaterBox, 40, 120, 80, 30, "(255, 140, 0)")
        label_place("Кухня (хл)", self.groupWaterBox, 40, 160, 80, 30, "(0, 170, 255)")
        label_place("Кухня (гр)", self.groupWaterBox, 40, 200, 80, 30, "(255, 140, 0)")

        color_1 = "(0, 170, 255)"
        color_2 = "(255, 140, 0)"

        grad_1 = "(91, 92, 96, 255)"
        grad_2 = "(108, 109, 114, 255)"

        self.lineEdit_pred_pokaz_W1 = line_edit_pokaz(self.groupWaterBox, 120, 80, 80, 30, color_1, grad_1, grad_2)
        self.lineEdit_pred_pokaz_W2 = line_edit_pokaz(self.groupWaterBox, 120, 120, 80, 30, color_2, grad_1, grad_2)
        self.lineEdit_pred_pokaz_W3 = line_edit_pokaz(self.groupWaterBox, 120, 160, 80, 30, color_1, grad_1, grad_2)
        self.lineEdit_pred_pokaz_W4 = line_edit_pokaz(self.groupWaterBox, 120, 200, 80, 30, color_2, grad_1, grad_2)

        self.lineEdit_post_pokaz_W1 = line_edit_pokaz(self.groupWaterBox, 210, 80, 80, 30, color_1, grad_2, grad_1)
        self.lineEdit_post_pokaz_W1.setReadOnly(False)
        self.lineEdit_post_pokaz_W2 = line_edit_pokaz(self.groupWaterBox, 210, 120, 80, 30, color_2, grad_2, grad_1)
        self.lineEdit_post_pokaz_W2.setReadOnly(False)
        self.lineEdit_post_pokaz_W3 = line_edit_pokaz(self.groupWaterBox, 210, 160, 80, 30, color_1, grad_2, grad_1)
        self.lineEdit_post_pokaz_W3.setReadOnly(False)
        self.lineEdit_post_pokaz_W4 = line_edit_pokaz(self.groupWaterBox, 210, 200, 80, 30, color_2, grad_2, grad_1)
        self.lineEdit_post_pokaz_W4.setReadOnly(False)

        self.label_month_ras_WC = label_month_ras("", self.groupWaterBox, 10, 260, 80, 30, color, grad_1, grad_2)

        self.label_month_ras_PLUS = label_month_ras('+', self.groupWaterBox, 95, 260, 10, 30, color, grad_1, grad_2)
        self.label_month_ras_PLUS.setStyleSheet("font-weight: 600; \n color: rgb(209, 209, 217); \n border: 0px;")

        self.label_month_ras_WH = label_month_ras("", self.groupWaterBox, 110, 260, 80, 30, color_2, grad_1, grad_2)

        self.label_month_ras_SUMM = label_month_ras('=', self.groupWaterBox, 195, 260, 10, 30, color, grad_1, grad_2)
        self.label_month_ras_SUMM.setStyleSheet("font-weight: 600; \n color: rgb(209, 209, 217); \n border: 0px;")

        self.label_month_ras = label_month_ras("", self.groupWaterBox, 210, 260, 80, 30, "(40, 40, 40)", grad_1, grad_2)

        self.groupGazBox = QtWidgets.QGroupBox("Газ", self.WinPokazanya)
        self.groupGazBox.setGeometry(QtCore.QRect(560, 50, 230, 300))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.groupGazBox.setFont(font)
        self.groupGazBox.setStyleSheet("font-weight: 700;\n color: rgb(209, 209, 217);\n padding: .5em 1em; \n "
                                       "border-radius: 5px; \n border: 1px solid rgba(209, 209, 217, 240);")
        self.groupGazBox.setAlignment(QtCore.Qt.AlignCenter)
        self.groupGazBox.setObjectName("groupGazBox")

        self.label_raschet_schet_G = label("Р/С 171 269 - 5", self.groupGazBox, 10, 30, 210, 25)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_raschet_schet_G.setFont(font)
        self.label_raschet_schet_G.setStyleSheet("color: rgb(80, 80, 80); \n background-color: rgb(255, 85, 255); \n "
                                                 "font-weight: 700; \n padding: .4em; \n "
                                                 "border: 1px solid rgba(50, 50, 50, 240); \n border-radius: 4px; \n ")

        label("предыдущие", self.groupGazBox, 10, 55, 100, 25)
        label("последние", self.groupGazBox, 120, 55, 100, 25)
        label("месячный расход", self.groupGazBox, 10, 235, 210, 25)

        color = "(150, 0, 150)"
        grad_1 = "(91, 92, 96, 255)"
        grad_2 = "(108, 109, 114, 255)"

        self.lineEdit_pred_pokaz_G = line_edit_pokaz(self.groupGazBox, 10, 80, 100, 150, color, grad_1, grad_2)
        self.lineEdit_post_pokaz_G = line_edit_pokaz(self.groupGazBox, 120, 80, 100, 150, color, grad_2, grad_1)
        self.lineEdit_post_pokaz_G.setReadOnly(False)

        self.label_month_ras_G = label_month_ras("", self.groupGazBox, 10, 260, 210, 30, color, grad_1, grad_2)

        QtCore.QMetaObject.connectSlotsByName(self.WinPokazanya)
        self.WinPokazanya.setTabOrder(self.lineEdit_post_pokaz_P, self.lineEdit_post_pokaz_W1)
        self.WinPokazanya.setTabOrder(self.lineEdit_post_pokaz_W1, self.lineEdit_post_pokaz_W2)
        self.WinPokazanya.setTabOrder(self.lineEdit_post_pokaz_W2, self.lineEdit_post_pokaz_W3)
        self.WinPokazanya.setTabOrder(self.lineEdit_post_pokaz_W3, self.lineEdit_post_pokaz_W4)
        self.WinPokazanya.setTabOrder(self.lineEdit_post_pokaz_W4, self.lineEdit_post_pokaz_G)
        self.WinPokazanya.setTabOrder(self.lineEdit_post_pokaz_G, self.pushButton_Save_PS)
        self.WinPokazanya.setTabOrder(self.pushButton_Save_PS, self.pushButton_Cancel_PS)
        self.WinPokazanya.setTabOrder(self.pushButton_Cancel_PS, self.checkBox_Edit_PS)
        self.WinPokazanya.setTabOrder(self.checkBox_Edit_PS, self.comboBox_month_PS)
        self.WinPokazanya.setTabOrder(self.comboBox_month_PS, self.comboBox_year_PS)
        self.WinPokazanya.setTabOrder(self.comboBox_year_PS, self.lineEdit_pred_pokaz_P)
        self.WinPokazanya.setTabOrder(self.lineEdit_pred_pokaz_P, self.lineEdit_pred_pokaz_W1)
        self.WinPokazanya.setTabOrder(self.lineEdit_pred_pokaz_W1, self.lineEdit_pred_pokaz_W2)
        self.WinPokazanya.setTabOrder(self.lineEdit_pred_pokaz_W2, self.lineEdit_pred_pokaz_W3)
        self.WinPokazanya.setTabOrder(self.lineEdit_pred_pokaz_W3, self.lineEdit_pred_pokaz_W4)
        self.WinPokazanya.setTabOrder(self.lineEdit_pred_pokaz_W4, self.lineEdit_pred_pokaz_G)
