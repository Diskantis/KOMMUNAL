# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PokazSchet.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5.QtGui import QIcon
from UI_CLASS_KOMM import *


class UiWinPlateg(object):
    def setupUi_KP(self, WinPlateg):
        self.WinPlateg = WinPlateg
        self.WinPlateg.setObjectName("KommunPlateg")
        self.WinPlateg.setWindowModality(QtCore.Qt.ApplicationModal)
        self.WinPlateg.resize(800, 400)
        self.WinPlateg.setGeometry(QtCore.QRect(560, 200, 800, 400))
        self.WinPlateg.setMinimumSize(QtCore.QSize(800, 400))
        self.WinPlateg.setFixedWidth(800)
        self.WinPlateg.setWindowTitle('ПЛАТЕЖИ')
        self.WinPlateg.setWindowIcon(QIcon('Resource/img/dollar.png'))
        self.WinPlateg.setStyleSheet("background-color: rgb(78, 79, 84);")

        self.verticalLayout = QtWidgets.QVBoxLayout(self.WinPlateg)
        self.verticalLayout.setObjectName("verticalLayout")

        # виджет с кнопками прокрутки периода и заголовком
        self.Label_KP = QtWidgets.QWidget(self.WinPlateg)
        self.Label_KP.setMaximumSize(QtCore.QSize(800, 34))
        self.Label_KP.setObjectName("Label_KP")

        self.label_month_year_KP, self.btn_Left_KP, self.btn_Right_KP, self.label_OK_KP = ui_win_head(self.Label_KP)

        self.label_month_year_KP.setGeometry(QtCore.QRect(35, 0, 710, 30))
        self.btn_Left_KP.setGeometry(QtCore.QRect(0, 0, 30, 30))
        self.btn_Right_KP.setGeometry(QtCore.QRect(749, 0, 30, 30))
        self.label_OK_KP.setGeometry(QtCore.QRect(35, 0, 70, 30))

        self.verticalLayout.addWidget(self.Label_KP)

        self.frame = QtWidgets.QFrame(self.WinPlateg)
        self.frame.setMinimumSize(QtCore.QSize(780, 0))
        self.frame.setStyleSheet("border-radius: 5px;\n border: 1px solid rgba(209, 209, 217, 240);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

        self.verticalLayout.addWidget(self.frame)

        self.frame_PWG_KP = QtWidgets.QWidget(self.WinPlateg)
        self.frame_PWG_KP.setGeometry(QtCore.QRect(20, 52, 760, 210))
        self.frame_PWG_KP.setObjectName("frame_PWG_KP")

        self.label_Plategi_KP = label("Комунальные платежи", self.frame_PWG_KP, 0, 0, 760, 30)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_Plategi_KP.setFont(font)
        self.label_Plategi_KP.setStyleSheet("font-weight: 700; \n color: rgb(209, 209, 217); \n padding: .1em;")

        self.label_sum = label("сумма", self.frame_PWG_KP, 180, 35, 170, 25)
        self.label_kol = label("количество", self.frame_PWG_KP, 360, 35, 170, 25)
        self.label_trf = label("тариф", self.frame_PWG_KP, 540, 35, 170, 25)

        # ЭЛЕКТРИЧЕСТВО создаем виджет с полями
        self.widget_Power = widget_plateg(self.frame_PWG_KP, 0, 60, 760, 34)
        self.label_Power = label_plateg("Электричество", self.widget_Power, 40, 0, 130, 30)
        self.btn_check_Power = btn_check_plateg(self.widget_Power, 0, 0, 30, 30)

        color = "(0, 160, 0)"
        grad_1 = "(91, 92, 96, 255)"
        grad_2 = "(108, 109, 114, 255)"

        self.lineEdit_sum_Power = line_edit_pokaz(self.widget_Power, 180, 0, 170, 30, color, grad_1, grad_2)
        self.lineEdit_kol_Power = line_edit_pokaz(self.widget_Power, 360, 0, 170, 30, color, grad_1, grad_2)
        self.lineEdit_trf_Power = line_edit_pokaz(self.widget_Power, 540, 0, 170, 30, color, grad_2, grad_1)

        # self.widget_Power = QtWidgets.QWidget(self.frame_PWG_KP)
        # self.widget_Power.setGeometry(QtCore.QRect(0, 60, 760, 34))
        # self.widget_Power.setObjectName("widget_Power")

        # self.label_Power = QtWidgets.QLabel("Электричество", self.widget_Power)
        # self.label_Power.setGeometry(QtCore.QRect(40, 0, 130, 30))
        # font = QtGui.QFont()
        # font.setPointSize(12)
        # font.setBold(True)
        # font.setWeight(87)
        # self.label_Power.setFont(font)
        # self.label_Power.setStyleSheet("font-weight: 700;\n color: rgb(209, 209, 217);\n padding: .0em;\n "
        #                                "border: 0px solid;")
        # self.label_Power.setObjectName("label_Power")

        # self.btn_P_check = QtWidgets.QPushButton(self.widget_Power)
        # self.btn_P_check.setGeometry(QtCore.QRect(0, 0, 30, 30))
        # self.btn_P_check.setStyleSheet("border: 0px solid;")
        # icon = QtGui.QIcon()
        # icon.addPixmap(QtGui.QPixmap("Resource/img/icon_checked_n.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        # icon.addPixmap(QtGui.QPixmap("Resource/img/icon_checked_o.png"), QtGui.QIcon.Active, QtGui.QIcon.On)
        # self.btn_P_check.setIcon(icon)
        # self.btn_P_check.setIconSize(QtCore.QSize(30, 30))
        # self.btn_P_check.setCheckable(True)
        # self.btn_P_check.setObjectName("btn_P_check")

        # self.lineEdit_P_sum = QtWidgets.QLineEdit(self.widget_Power)
        # self.lineEdit_P_sum.setGeometry(QtCore.QRect(180, 0, 170, 30))
        # font = QtGui.QFont()
        # font.setPointSize(12)
        # font.setWeight(75)
        # self.lineEdit_P_sum.setFont(font)
        # self.lineEdit_P_sum.setAlignment(QtCore.Qt.AlignCenter)
        # self.lineEdit_P_sum.setReadOnly(True)
        # self.lineEdit_P_sum.setStyleSheet("border-radius: 4px;\n color: rgb(0, 160, 0);\n "
        #                                   "border: 1px solid rgba(50, 50, 50, 240);\n "
        #                                   "background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, "
        #                                   "stop:0 rgba(125, 126, 131, 255), stop:0.01 rgba(91, 92, 96, 255), "
        #                                   "stop:0.99 rgba(108, 109, 114, 255), stop:1 rgba(125, 126, 131, 255));")
        # self.lineEdit_P_sum.setObjectName("lineEdit_P_sum")

        # self.lineEdit_P_kol = QtWidgets.QLineEdit(self.widget_Power)
        # self.lineEdit_P_kol.setGeometry(QtCore.QRect(360, 0, 170, 30))
        # font = QtGui.QFont()
        # font.setPointSize(12)
        # font.setWeight(75)
        # self.lineEdit_P_kol.setFont(font)
        # self.lineEdit_P_kol.setAlignment(QtCore.Qt.AlignCenter)
        # self.lineEdit_P_kol.setReadOnly(True)
        # self.lineEdit_P_kol.setStyleSheet("border-radius: 4px;\n color: rgb(0, 160, 0);\n "
        #                                   "border: 1px solid rgba(50, 50, 50, 240);\n "
        #                                   "background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, "
        #                                   "stop:0 rgba(125, 126, 131, 255), stop:0.01 rgba(91, 92, 96, 255), "
        #                                   "stop:0.99 rgba(108, 109, 114, 255), stop:1 rgba(125, 126, 131, 255));")
        # self.lineEdit_P_kol.setObjectName("lineEdit_P_kol")

        # self.lineEdit_P_trf = QtWidgets.QLineEdit(self.widget_Power)
        # self.lineEdit_P_trf.setGeometry(QtCore.QRect(540, 0, 170, 30))
        # font = QtGui.QFont()
        # font.setPointSize(12)
        # font.setWeight(75)
        # self.lineEdit_P_trf.setFont(font)
        # self.lineEdit_P_trf.setAlignment(QtCore.Qt.AlignCenter)
        # self.lineEdit_P_trf.setReadOnly(True)
        # self.lineEdit_P_trf.setStyleSheet("border-radius: 4px; \n color: rgb(209, 209, 217); \n "
        #                                   "border: 1px solid rgba(50, 50, 50, 240); \n "
        #                                   "background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, "
        #                                   "stop:0 rgba(125, 126, 131, 255), stop:0.01 rgba(108, 109, 114, 255), "
        #                                   "stop:0.99 rgba(91, 92, 96, 255), stop:1 rgba(125, 126, 131, 255));")
        # self.lineEdit_P_trf.setObjectName("lineEdit_P_trf")

        # self.btn_P_pdf = QtWidgets.QPushButton(self.widget_Power)
        # self.btn_P_pdf.setGeometry(QtCore.QRect(720, 0, 30, 30))
        # self.btn_P_pdf.setStyleSheet("border: 0px solid;")
        # icon = QtGui.QIcon()
        # icon.addPixmap(QtGui.QPixmap("Resource/img/PDF_D3.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        # icon.addPixmap(QtGui.QPixmap("Resource/img/PDF_O2.png"), QtGui.QIcon.Active, QtGui.QIcon.On)
        # self.btn_P_pdf.setIcon(icon)
        # self.btn_P_pdf.setIconSize(QtCore.QSize(30, 30))
        # # self.btn_P_pdf.setCheckable(True)
        # self.btn_P_pdf.setObjectName("btn_P_pdf")

        # ВОДА создаем виджет с полями
        self.widget_Water = widget_plateg(self.frame_PWG_KP, 0, 94, 760, 34)
        self.label_Water = label_plateg("Вода", self.widget_Water, 40, 0, 130, 30)
        self.btn_check_Water = btn_check_plateg(self.widget_Water, 0, 0, 30, 30)

        color = "(0, 170, 255)"
        grad_1 = "(91, 92, 96, 255)"
        grad_2 = "(108, 109, 114, 255)"

        self.lineEdit_sum_Water = line_edit_pokaz(self.widget_Water, 180, 0, 170, 30, color, grad_1, grad_2)
        self.lineEdit_kol_Water = line_edit_pokaz(self.widget_Water, 360, 0, 170, 30, color, grad_1, grad_2)
        self.lineEdit_trf_Water = line_edit_pokaz(self.widget_Water, 540, 0, 170, 30, color, grad_2, grad_1)

        # self.widget_Water = QtWidgets.QWidget(self.frame_PWG_KP)
        # self.widget_Water.setGeometry(QtCore.QRect(0, 94, 760, 34))
        # sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        # sizePolicy.setHorizontalStretch(0)
        # sizePolicy.setVerticalStretch(0)
        # sizePolicy.setHeightForWidth(self.widget_Water.sizePolicy().hasHeightForWidth())
        # self.widget_Water.setSizePolicy(sizePolicy)
        # self.widget_Water.setObjectName("widget_Water")

        # self.label_Water = QtWidgets.QLabel("Вода", self.widget_Water)
        # self.label_Water.setGeometry(QtCore.QRect(40, 0, 130, 30))
        # font = QtGui.QFont()
        # font.setPointSize(12)
        # font.setBold(True)
        # font.setWeight(87)
        # self.label_Water.setFont(font)
        # self.label_Water.setStyleSheet("font-weight: 700;\n color: rgb(209, 209, 217);\n padding: .0em;\n "
        #                                "border: 0px solid;")
        # self.label_Water.setObjectName("label_Water")

        # self.btn_W_check = QtWidgets.QPushButton(self.widget_Water)
        # self.btn_W_check.setGeometry(QtCore.QRect(0, 0, 30, 30))
        # self.btn_W_check.setStyleSheet("border: 0px solid;")
        # icon = QtGui.QIcon()
        # icon.addPixmap(QtGui.QPixmap("Resource/img/icon_checked_n.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        # icon.addPixmap(QtGui.QPixmap("Resource/img/icon_checked_o.png"), QtGui.QIcon.Active, QtGui.QIcon.On)
        # self.btn_W_check.setIcon(icon)
        # self.btn_W_check.setIconSize(QtCore.QSize(30, 30))
        # self.btn_W_check.setCheckable(True)
        # self.btn_W_check.setObjectName("btn_W_check")

        # self.lineEdit_W_sum = QtWidgets.QLineEdit(self.widget_Water)
        # self.lineEdit_W_sum.setGeometry(QtCore.QRect(180, 0, 170, 30))
        # font = QtGui.QFont()
        # font.setPointSize(12)
        # font.setWeight(75)
        # self.lineEdit_W_sum.setFont(font)
        # self.lineEdit_W_sum.setAlignment(QtCore.Qt.AlignCenter)
        # self.lineEdit_W_sum.setReadOnly(True)
        # self.lineEdit_W_sum.setStyleSheet("border-radius: 4px;\n color: rgb(0, 170, 255);\n "
        #                                   "border: 1px solid rgba(50, 50, 50, 240);\n"
        #                                   "background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, "
        #                                   "stop:0 rgba(125, 126, 131, 255), stop:0.01 rgba(91, 92, 96, 255), "
        #                                   "stop:0.99 rgba(108, 109, 114, 255), stop:1 rgba(125, 126, 131, 255));")
        # self.lineEdit_W_sum.setObjectName("lineEdit_W_sum")
        #
        # self.lineEdit_W_kol = QtWidgets.QLineEdit(self.widget_Water)
        # self.lineEdit_W_kol.setGeometry(QtCore.QRect(360, 0, 170, 30))
        # font = QtGui.QFont()
        # font.setPointSize(12)
        # font.setWeight(75)
        # self.lineEdit_W_kol.setFont(font)
        # self.lineEdit_W_kol.setAlignment(QtCore.Qt.AlignCenter)
        # self.lineEdit_W_kol.setReadOnly(True)
        # self.lineEdit_W_kol.setStyleSheet("border-radius: 4px;\n color: rgb(0, 170, 255);\n"
        #                                   "border: 1px solid rgba(50, 50, 50, 240);\n"
        #                                   "background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, "
        #                                   "stop:0 rgba(125, 126, 131, 255), stop:0.01 rgba(91, 92, 96, 255), "
        #                                   "stop:0.99 rgba(108, 109, 114, 255), stop:1 rgba(125, 126, 131, 255));")
        # self.lineEdit_W_kol.setObjectName("lineEdit_W_kol")
        #
        # self.lineEdit_W_trf = QtWidgets.QLineEdit(self.widget_Water)
        # self.lineEdit_W_trf.setGeometry(QtCore.QRect(540, 0, 170, 30))
        # font = QtGui.QFont()
        # font.setPointSize(12)
        # font.setWeight(75)
        # self.lineEdit_W_trf.setFont(font)
        # self.lineEdit_W_trf.setAlignment(QtCore.Qt.AlignCenter)
        # self.lineEdit_W_trf.setReadOnly(True)
        # self.lineEdit_W_trf.setStyleSheet("border-radius: 4px; \n color: rgb(209, 209, 217); \n "
        #                                   "border: 1px solid rgba(50, 50, 50, 240); \n "
        #                                   "background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, "
        #                                   "stop:0 rgba(125, 126, 131, 255), stop:0.01 rgba(108, 109, 114, 255), "
        #                                   "stop:0.99 rgba(91, 92, 96, 255), stop:1 rgba(125, 126, 131, 255));")
        # self.lineEdit_W_trf.setObjectName("lineEdit_W_trf")

        # self.btn_W_pdf = QtWidgets.QPushButton(self.widget_Water)
        # self.btn_W_pdf.setGeometry(QtCore.QRect(720, 0, 30, 30))
        # self.btn_W_pdf.setStyleSheet("border: 0px solid;")
        # icon = QtGui.QIcon()
        # icon.addPixmap(QtGui.QPixmap("Resource/img/PDF_D3.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        # icon.addPixmap(QtGui.QPixmap("Resource/img/PDF_O2.png"), QtGui.QIcon.Active, QtGui.QIcon.On)
        # self.btn_W_pdf.setIcon(icon)
        # self.btn_W_pdf.setIconSize(QtCore.QSize(30, 30))
        # self.btn_W_pdf.setCheckable(True)
        # self.btn_W_pdf.setObjectName("btn_W_pdf")

        # ГАЗ создаем виджет с полями
        self.widget_Gaz = widget_plateg(self.frame_PWG_KP, 0, 128, 760, 34)
        self.label_Gaz = label_plateg("Газ", self.widget_Gaz, 40, 0, 130, 30)
        self.btn_check_Gaz = btn_check_plateg(self.widget_Gaz, 0, 0, 30, 30)

        color = "(160, 0, 160)"
        grad_1 = "(91, 92, 96, 255)"
        grad_2 = "(108, 109, 114, 255)"

        self.lineEdit_sum_Gaz = line_edit_pokaz(self.widget_Gaz, 180, 0, 170, 30, color, grad_1, grad_2)
        self.lineEdit_kol_Gaz = line_edit_pokaz(self.widget_Gaz, 360, 0, 170, 30, color, grad_1, grad_2)
        self.lineEdit_trf_Gaz = line_edit_pokaz(self.widget_Gaz, 540, 0, 170, 30, color, grad_2, grad_1)

        # self.widget_Gaz = QtWidgets.QWidget(self.frame_PWG_KP)
        # self.widget_Gaz.setGeometry(QtCore.QRect(0, 128, 760, 34))
        # sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        # sizePolicy.setHorizontalStretch(0)
        # sizePolicy.setVerticalStretch(0)
        # sizePolicy.setHeightForWidth(self.widget_Gaz.sizePolicy().hasHeightForWidth())
        # self.widget_Gaz.setSizePolicy(sizePolicy)
        # self.widget_Gaz.setObjectName("widget_Gaz")

        # self.label_Gaz = QtWidgets.QLabel("Газ", self.widget_Gaz)
        # self.label_Gaz.setGeometry(QtCore.QRect(40, 0, 130, 30))
        # font = QtGui.QFont()
        # font.setPointSize(12)
        # font.setBold(True)
        # font.setWeight(87)
        # self.label_Gaz.setFont(font)
        # self.label_Gaz.setStyleSheet("font-weight: 700;\n color: rgb(209, 209, 217);\n padding: .0em;\n "
        #                              "border: 0px solid;")
        # self.label_Gaz.setObjectName("label_Gaz")

        # self.btn_G_check = QtWidgets.QPushButton(self.widget_Gaz)
        # self.btn_G_check.setGeometry(QtCore.QRect(0, 0, 30, 30))
        # self.btn_G_check.setStyleSheet("border: 0px solid;")
        # icon = QtGui.QIcon()
        # icon.addPixmap(QtGui.QPixmap("Resource/img/icon_checked_n.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        # icon.addPixmap(QtGui.QPixmap("Resource/img/icon_checked_o.png"), QtGui.QIcon.Active, QtGui.QIcon.On)
        # self.btn_G_check.setIcon(icon)
        # self.btn_G_check.setIconSize(QtCore.QSize(30, 30))
        # self.btn_G_check.setCheckable(True)
        # self.btn_G_check.setObjectName("btn_G_check")

        # self.lineEdit_G_sum = QtWidgets.QLineEdit(self.widget_Gaz)
        # self.lineEdit_G_sum.setGeometry(QtCore.QRect(180, 0, 170, 30))
        # font = QtGui.QFont()
        # font.setPointSize(12)
        # font.setWeight(75)
        # self.lineEdit_G_sum.setFont(font)
        # self.lineEdit_G_sum.setAlignment(QtCore.Qt.AlignCenter)
        # self.lineEdit_G_sum.setReadOnly(True)
        # self.lineEdit_G_sum.setStyleSheet("border-radius: 4px;\n color: rgb(160, 0, 160);\n"
        #                                   "border: 1px solid rgba(50, 50, 50, 240);\n"
        #                                   "background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, "
        #                                   "stop:0 rgba(125, 126, 131, 255), stop:0.01 rgba(91, 92, 96, 255), "
        #                                   "stop:0.99 rgba(108, 109, 114, 255), stop:1 rgba(125, 126, 131, 255));")
        # self.lineEdit_G_sum.setObjectName("lineEdit_G_sum")
        #
        # self.lineEdit_G_kol = QtWidgets.QLineEdit(self.widget_Gaz)
        # self.lineEdit_G_kol.setGeometry(QtCore.QRect(360, 0, 170, 30))
        # font = QtGui.QFont()
        # font.setPointSize(12)
        # font.setWeight(75)
        # self.lineEdit_G_kol.setFont(font)
        # self.lineEdit_G_kol.setAlignment(QtCore.Qt.AlignCenter)
        # self.lineEdit_G_kol.setReadOnly(True)
        # self.lineEdit_G_kol.setStyleSheet("border-radius: 4px;\n color: rgb(160, 0, 160);\n"
        #                                   "border: 1px solid rgba(50, 50, 50, 240);\n"
        #                                   "background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, "
        #                                   "stop:0 rgba(125, 126, 131, 255), stop:0.01 rgba(91, 92, 96, 255), "
        #                                   "stop:0.99 rgba(108, 109, 114, 255), stop:1 rgba(125, 126, 131, 255));")
        # self.lineEdit_G_kol.setObjectName("lineEdit_G_kol")
        #
        # self.lineEdit_G_trf = QtWidgets.QLineEdit(self.widget_Gaz)
        # self.lineEdit_G_trf.setGeometry(QtCore.QRect(540, 0, 170, 30))
        # font = QtGui.QFont()
        # font.setPointSize(12)
        # font.setWeight(75)
        # self.lineEdit_G_trf.setFont(font)
        # self.lineEdit_G_trf.setAlignment(QtCore.Qt.AlignCenter)
        # self.lineEdit_G_trf.setReadOnly(True)
        # self.lineEdit_G_trf.setStyleSheet("border-radius: 4px; \n color: rgb(209, 209, 217); \n "
        #                                   "border: 1px solid rgba(50, 50, 50, 240); \n "
        #                                   "background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, "
        #                                   "stop:0 rgba(125, 126, 131, 255), stop:0.01 rgba(108, 109, 114, 255), "
        #                                   "stop:0.99 rgba(91, 92, 96, 255), stop:1 rgba(125, 126, 131, 255));")
        # self.lineEdit_G_trf.setObjectName("lineEdit_G_trf")

        # self.btn_G_pdf = QtWidgets.QPushButton(self.widget_Gaz)
        # self.btn_G_pdf.setGeometry(QtCore.QRect(720, 0, 30, 30))
        # self.btn_G_pdf.setStyleSheet("border: 0px solid;")
        # icon = QtGui.QIcon()
        # icon.addPixmap(QtGui.QPixmap("Resource/img/PDF_D3.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        # icon.addPixmap(QtGui.QPixmap("Resource/img/PDF_O2.png"), QtGui.QIcon.Active, QtGui.QIcon.On)
        # self.btn_G_pdf.setIcon(icon)
        # self.btn_G_pdf.setIconSize(QtCore.QSize(30, 30))
        # self.btn_G_pdf.setCheckable(True)
        # self.btn_G_pdf.setObjectName("btn_G_pdf")

        # РАЗДЕЛИТЕЛЬ между основными и дополнительными платежами
        self.LINE_RAZDEL = QtWidgets.QFrame(self.frame_PWG_KP)
        self.LINE_RAZDEL.setGeometry(QtCore.QRect(0, 160, 760, 10))
        self.LINE_RAZDEL.setAutoFillBackground(False)
        self.LINE_RAZDEL.setStyleSheet("")
        self.LINE_RAZDEL.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.LINE_RAZDEL.setLineWidth(1)
        self.LINE_RAZDEL.setMidLineWidth(1)
        self.LINE_RAZDEL.setFrameShape(QtWidgets.QFrame.HLine)
        self.LINE_RAZDEL.setObjectName("LINE_RAZDEL")

        # виджет с полями для ДОЛНИТЕЛЬНЫХ ПЛАТЕЖЕЙ
        self.frame_plategi_KP = QtWidgets.QFrame(self.WinPlateg)
        self.frame_plategi_KP.setGeometry(QtCore.QRect(20, 225, 760, 0))
        self.frame_plategi_KP.setObjectName("frame_Plategi_KP")

        self.gridLayout = QtWidgets.QGridLayout(self.frame_plategi_KP)
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout.setVerticalSpacing(1)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")

        # кнопка вызова метода создания ДОЛНИТЕЛЬНЫХ ПЛАТЕЖЕЙ
        self.pushButton_add_Plateg_KP = QtWidgets.QPushButton("Добавить платеж", self.frame_PWG_KP)
        self.pushButton_add_Plateg_KP.setGeometry(QtCore.QRect(10, 0, 780, 30))
        self.pushButton_add_Plateg_KP.setAutoDefault(True)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_add_Plateg_KP.setFont(font)
        self.pushButton_add_Plateg_KP.setStyleSheet("font-weight: 700;\n color: rgb(209, 209, 217);\n "
                                                    "padding: .5em 1em;")
        self.pushButton_add_Plateg_KP.setObjectName("pushButton_add_Plateg_KP")

        self.verticalLayout.addWidget(self.pushButton_add_Plateg_KP)

        # виджет с полем ИТОГОВОЙ СУММЫ
        self.Itog_KP = QtWidgets.QWidget(self.WinPlateg)
        self.Itog_KP.setMinimumSize(QtCore.QSize(780, 40))
        self.Itog_KP.setMaximumSize(QtCore.QSize(780, 40))
        self.Itog_KP.setObjectName("Itog_KP")

        self.frame_Itog_KP = QtWidgets.QFrame(self.Itog_KP)
        self.frame_Itog_KP.setGeometry(QtCore.QRect(0, 0, 780, 40))
        self.frame_Itog_KP.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_Itog_KP.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_Itog_KP.setStyleSheet("border-radius: 5px; \n border: 1px solid rgba(209, 209, 217, 240);")
        self.frame_Itog_KP.setObjectName("frame_Itog_KP")

        self.label_Itog_KP = QtWidgets.QLabel("Итого:", self.Itog_KP)
        self.label_Itog_KP.setGeometry(QtCore.QRect(5, 5, 180, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_Itog_KP.setFont(font)
        self.label_Itog_KP.setStyleSheet("font-weight: 700; \n color: rgb(209, 209, 217); \n padding: .1em; \n "
                                         "border: 1px;")
        self.label_Itog_KP.setAlignment(QtCore.Qt.AlignRight)
        self.label_Itog_KP.setObjectName("label_Itog_KP")

        self.lineEdit_IS_sum = QtWidgets.QLineEdit(self.Itog_KP)
        self.lineEdit_IS_sum.setGeometry(QtCore.QRect(190, 5, 530, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        self.lineEdit_IS_sum.setFont(font)
        self.lineEdit_IS_sum.setStyleSheet("border-radius: 4px; \n color: rgb(255, 170, 0); \n "
                                           "border: 1px solid rgba(50, 50, 50, 240); \n "
                                           "background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, "
                                           "stop:0 rgba(125, 126, 131, 255), stop:0.01 rgba(91, 92, 96, 255), "
                                           "stop:0.99 rgba(108, 109, 114, 255), stop:1 rgba(125, 126, 131, 255));")
        self.lineEdit_IS_sum.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_IS_sum.setReadOnly(True)
        self.lineEdit_IS_sum.setObjectName("lineEdit_IS_sum")

        self.verticalLayout.addWidget(self.Itog_KP)

        # виджет с кнопками выбора периода и сохранения
        self.Button_KP = QtWidgets.QWidget(self.WinPlateg)
        self.Button_KP.setMinimumSize(QtCore.QSize(780, 35))
        self.Button_KP.setMaximumSize(QtCore.QSize(780, 35))
        self.Button_KP.setObjectName("Button_KP")

        self.comboBox_month_KP, self.comboBox_year_KP, self.label_ERROR_KP, self.checkBox_Edit_KP, \
        self.pushButton_Save_KP, self.pushButton_Cancel_KP = ui_win_combobox(self.Button_KP)

        # выбор месяца
        self.comboBox_month_KP.setGeometry(QtCore.QRect(0, 5, 130, 30))
        # выбор года
        self.comboBox_year_KP.setGeometry(QtCore.QRect(140, 5, 90, 30))
        # поле вывода сообщения об ОШИБКЕ
        self.label_ERROR_KP.setGeometry(QtCore.QRect(230, 5, 320, 30))
        # переключатель положения РЕДАКТИРОВАНИЯ полей
        self.checkBox_Edit_KP.setGeometry(QtCore.QRect(410, 5, 130, 30))
        # кнопка СОХРАНЕНИЯ данных в базу данных
        self.pushButton_Save_KP.setGeometry(QtCore.QRect(550, 5, 110, 30))
        # кнопка ЗАКРЫТИЯ окна
        self.pushButton_Cancel_KP.setGeometry(QtCore.QRect(670, 5, 110, 30))

        self.verticalLayout.addWidget(self.Button_KP)

        # # выбор месяца
        # self.comboBox_month_KP = QtWidgets.QComboBox(self.Button_KP)
        # self.comboBox_month_KP.setGeometry(QtCore.QRect(0, 5, 130, 30))
        # font = QtGui.QFont()
        # font.setPointSize(11)
        # self.comboBox_month_KP.setFont(font)
        # self.comboBox_month_KP.setStyleSheet("font-size: 50%;\n font-weight: 700;\n color: rgb(209, 209, 217);")
        # self.comboBox_month_KP.setObjectName("comboBox_month")
        #
        # # выбор года
        # self.comboBox_year_KP = QtWidgets.QComboBox(self.Button_KP)
        # self.comboBox_year_KP.setGeometry(QtCore.QRect(140, 5, 90, 30))
        # font = QtGui.QFont()
        # font.setPointSize(11)
        # self.comboBox_year_KP.setFont(font)
        # self.comboBox_year_KP.setStyleSheet("font-size: 50%;\n font-weight: 700;\n color: rgb(209, 209, 217);")
        # self.comboBox_year_KP.setObjectName("comboBox_year")
        #
        # # поле вывода сообщения об ОШИБКЕ
        # self.label_ERROR = QtWidgets.QLabel(self.Button_KP)
        # self.label_ERROR.setGeometry(QtCore.QRect(230, 5, 320, 30))
        # font = QtGui.QFont()
        # font.setPointSize(12)
        # font.setWeight(75)
        # self.label_ERROR.setFont(font)
        # self.label_ERROR.setStyleSheet("font-weight: 700;\n color: rgb(0, 170, 255);\n padding: .4em 1em;")
        # self.label_ERROR.setAlignment(QtCore.Qt.AlignCenter)
        # self.label_ERROR.setObjectName("label_ERROR")
        #
        # # переключатель положения РЕДАКТИРОВАНИЯ полей
        # self.checkBox_Edit_KP = QtWidgets.QCheckBox("Редактирование", self.Button_KP)
        # self.checkBox_Edit_KP.setGeometry(QtCore.QRect(410, 5, 130, 30))
        # font = QtGui.QFont()
        # font.setPointSize(9)
        # self.checkBox_Edit_KP.setFont(font)
        # self.checkBox_Edit_KP.setLayoutDirection(QtCore.Qt.RightToLeft)
        # self.checkBox_Edit_KP.setStyleSheet("font-weight: 600; \n color: rgb(209, 209, 217); \n border: 0px;")
        # self.checkBox_Edit_KP.setChecked(False)
        # self.checkBox_Edit_KP.setObjectName("checkBox_Edit_KP")
        #
        # # кнопка СОХРАНЕНИЯ данных в базу данных
        # self.pushButton_Save_KP = QtWidgets.QPushButton("Сохранить", self.Button_KP)
        # self.pushButton_Save_KP.setGeometry(QtCore.QRect(550, 5, 110, 30))
        # self.pushButton_Save_KP.setAutoDefault(True)
        # font = QtGui.QFont()
        # font.setPointSize(10)
        # self.pushButton_Save_KP.setFont(font)
        # self.pushButton_Save_KP.setStyleSheet("font-weight: 700;\n color: rgb(209, 209, 217);\n padding: .5em 1em;")
        # self.pushButton_Save_KP.setObjectName("pushButton_Save_KP")
        #
        # # кнопка ЗАКРЫТИЯ окна
        # self.pushButton_Cancel_KP = QtWidgets.QPushButton("Cancel", self.Button_KP)
        # self.pushButton_Cancel_KP.setGeometry(QtCore.QRect(670, 5, 110, 30))
        # self.pushButton_Cancel_KP.setAutoDefault(True)
        # font = QtGui.QFont()
        # font.setPointSize(10)
        # self.pushButton_Cancel_KP.setFont(font)
        # self.pushButton_Cancel_KP.setStyleSheet("font-weight: 700;\n color: rgb(209, 209, 217);\n padding: .5em 1em;")
        # self.pushButton_Cancel_KP.setObjectName("pushButton_Cancel_KP")

        QtCore.QMetaObject.connectSlotsByName(self.WinPlateg)
        self.WinPlateg.setTabOrder(self.lineEdit_trf_Power, self.lineEdit_trf_Water)
        self.WinPlateg.setTabOrder(self.lineEdit_trf_Water, self.lineEdit_trf_Gaz)
        self.WinPlateg.setTabOrder(self.lineEdit_trf_Gaz, self.pushButton_add_Plateg_KP)
        self.WinPlateg.setTabOrder(self.pushButton_add_Plateg_KP, self.pushButton_Save_KP)
        self.WinPlateg.setTabOrder(self.pushButton_Save_KP, self.pushButton_Cancel_KP)
        self.WinPlateg.setTabOrder(self.pushButton_Cancel_KP, self.comboBox_month_KP)
        self.WinPlateg.setTabOrder(self.comboBox_month_KP, self.comboBox_year_KP)


def frame_plateg(self, name, position):
    self.widget_Plat = QtWidgets.QWidget(self.frame_plategi_KP)
    self.widget_Plat.setGeometry(QtCore.QRect(10, 0, 760, 32))
    sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.widget_Plat.sizePolicy().hasHeightForWidth())
    self.widget_Plat.setSizePolicy(sizePolicy)
    self.widget_Plat.setObjectName("widget_Plat")

    self.label_Plat = QtWidgets.QLabel(name, self.widget_Plat)
    self.label_Plat.setGeometry(QtCore.QRect(40, 1, 130, 30))
    font = QtGui.QFont()
    font.setPointSize(12)
    font.setBold(True)
    font.setWeight(87)
    self.label_Plat.setFont(font)
    self.label_Plat.setStyleSheet("font-weight: 700;\n color: rgb(209, 209, 217);\n padding: .0em;\n "
                                  "border: 0px solid;")
    self.label_Plat.setObjectName("label_Plat")

    self.btn_Pl_check = QtWidgets.QPushButton(self.widget_Plat)  # QPushButton
    self.btn_Pl_check.setGeometry(QtCore.QRect(0, 1, 30, 30))
    self.btn_Pl_check.setStyleSheet("border: 0px solid;")
    icon = QtGui.QIcon()
    icon.addPixmap(QtGui.QPixmap("Resource/img/icon_checked_n.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    icon.addPixmap(QtGui.QPixmap("Resource/img/icon_checked_o.png"), QtGui.QIcon.Active, QtGui.QIcon.On)
    self.btn_Pl_check.setIcon(icon)
    self.btn_Pl_check.setIconSize(QtCore.QSize(30, 30))
    self.btn_Pl_check.setCheckable(True)
    self.btn_Pl_check.setObjectName("btn_Pl_check")

    self.lineEdit_Pl_sum = QtWidgets.QLineEdit(self.widget_Plat)
    self.lineEdit_Pl_sum.setGeometry(QtCore.QRect(180, 1, 170, 30))
    font = QtGui.QFont()
    font.setPointSize(12)
    font.setWeight(75)
    self.lineEdit_Pl_sum.setFont(font)
    self.lineEdit_Pl_sum.setAlignment(QtCore.Qt.AlignCenter)
    self.lineEdit_Pl_sum.setReadOnly(False)
    self.lineEdit_Pl_sum.setStyleSheet("border-radius: 4px; \n color: rgb(209, 209, 217); \n "
                                       "border: 1px solid rgba(50, 50, 50, 240); \n "
                                       "background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, "
                                       "stop:0 rgba(125, 126, 131, 255), stop:0.01 rgba(108, 109, 114, 255), "
                                       "stop:0.99 rgba(91, 92, 96, 255), stop:1 rgba(125, 126, 131, 255));")
    self.lineEdit_Pl_sum.setObjectName("lineEdit_Pl_sum")

    self.btn_Pl_pdf = QtWidgets.QPushButton(self.widget_Plat)
    self.btn_Pl_pdf.setGeometry(QtCore.QRect(720, 2, 30, 30))
    self.btn_Pl_pdf.setStyleSheet("border: 0px solid;")
    icon = QtGui.QIcon()
    icon.addPixmap(QtGui.QPixmap("Resource/img/icon_delete.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    # icon.addPixmap(QtGui.QPixmap("Resource/img/PDF_O2.png"), QtGui.QIcon.Active, QtGui.QIcon.On)
    self.btn_Pl_pdf.setIcon(icon)
    self.btn_Pl_pdf.setIconSize(QtCore.QSize(30, 30))
    # self.btn_Pl_pdf.setCheckable(True)
    self.btn_Pl_pdf.setObjectName("btn_Pl_pdf")

    self.gridLayout.addWidget(self.widget_Plat, position, 0, 1, 1)
