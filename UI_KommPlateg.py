# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PokazSchet.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5.QtGui import QIcon
from Resource.UI_CLASS_KOMM import *


# окно приложения "ПЛАТЕЖИ"
class UiWinPlateg(object):
    def setupUi_KP(self, WinPlateg):
        self.WinPlateg = WinPlateg
        self.WinPlateg.setObjectName("KommunPlateg")
        self.WinPlateg.setWindowModality(QtCore.Qt.ApplicationModal)
        self.WinPlateg.resize(800, 365)
        self.WinPlateg.setGeometry(QtCore.QRect(560, 200, 800, 365))
        self.WinPlateg.setMinimumSize(QtCore.QSize(800, 365))
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
        self.frame_PWG_KP.setGeometry(QtCore.QRect(20, 52, 760, 167))
        self.frame_PWG_KP.setObjectName("frame_PWG_KP")

        self.label_Plategi_KP = label("Комунальные платежи", self.frame_PWG_KP, 0, 0, 760, 30)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_Plategi_KP.setFont(font)
        self.label_Plategi_KP.setStyleSheet("font-weight: 700; \n color: rgb(209, 209, 217); \n padding: .1em;")

        self.label_sum = label("сумма", self.frame_PWG_KP, 180, 35, 190, 25)
        self.label_kol = label("количество", self.frame_PWG_KP, 375, 35, 190, 25)
        self.label_trf = label("тариф", self.frame_PWG_KP, 570, 35, 190, 25)

        # ЭЛЕКТРИЧЕСТВО создаем виджет с полями
        self.widget_Power = widget_plateg(self.frame_PWG_KP, 0, 60, 760, 34)
        self.label_Power = label_plateg("Электричество", self.widget_Power, 40, 0, 130, 30)
        self.btn_check_Power = btn_check_plateg(self.widget_Power, 0, 0, 30, 30)

        color = "(0, 160, 0)"
        grad_1 = "(91, 92, 96, 255)"
        grad_2 = "(108, 109, 114, 255)"

        self.lineEdit_sum_Power = line_edit_pokaz(self.widget_Power, 180, 0, 190, 30, color, grad_1, grad_2)
        self.lineEdit_kol_Power = line_edit_pokaz(self.widget_Power, 375, 0, 190, 30, color, grad_1, grad_2)
        self.lineEdit_trf_Power = line_edit_pokaz(self.widget_Power, 570, 0, 190, 30, color, grad_2, grad_1)

        # ВОДА создаем виджет с полями
        self.widget_Water = widget_plateg(self.frame_PWG_KP, 0, 94, 760, 34)
        self.label_Water = label_plateg("Вода", self.widget_Water, 40, 0, 130, 30)
        self.btn_check_Water = btn_check_plateg(self.widget_Water, 0, 0, 30, 30)

        color = "(0, 170, 255)"

        self.lineEdit_sum_Water = line_edit_pokaz(self.widget_Water, 180, 0, 190, 30, color, grad_1, grad_2)
        self.lineEdit_kol_Water = line_edit_pokaz(self.widget_Water, 375, 0, 190, 30, color, grad_1, grad_2)
        self.lineEdit_trf_Water = line_edit_pokaz(self.widget_Water, 570, 0, 190, 30, color, grad_2, grad_1)

        # ГАЗ создаем виджет с полями
        self.widget_Gaz = widget_plateg(self.frame_PWG_KP, 0, 128, 760, 34)
        self.label_Gaz = label_plateg("Газ", self.widget_Gaz, 40, 0, 130, 30)
        self.btn_check_Gaz = btn_check_plateg(self.widget_Gaz, 0, 0, 30, 30)

        color = "(160, 0, 160)"

        self.lineEdit_sum_Gaz = line_edit_pokaz(self.widget_Gaz, 180, 0, 190, 30, color, grad_1, grad_2)
        self.lineEdit_kol_Gaz = line_edit_pokaz(self.widget_Gaz, 375, 0, 190, 30, color, grad_1, grad_2)
        self.lineEdit_trf_Gaz = line_edit_pokaz(self.widget_Gaz, 570, 0, 190, 30, color, grad_2, grad_1)

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
        self.pushButton_add_Plateg_KP = btn("Добавить платеж", self.frame_PWG_KP, 10, 0, 780, 30)
        self.pushButton_add_Plateg_KP.setStyleSheet("font-weight: 700;\n color: rgb(209, 209, 217);\n "
                                                    "padding: .5em 1em;")

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

        self.label_Itog_KP = label("Итого:", self.Itog_KP, 5, 5, 180, 30)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_Itog_KP.setFont(font)
        self.label_Itog_KP.setStyleSheet("font-weight: 700; \n color: rgb(209, 209, 217); \n padding: .1em;")
        self.label_Itog_KP.setAlignment(QtCore.Qt.AlignRight)

        self.lineEdit_IS_sum = line_edit_pokaz(self.Itog_KP, 190, 5, 530, 30, "(255, 170, 0)", grad_1, grad_2)

        self.verticalLayout.addWidget(self.Itog_KP)

        # виджет с кнопками выбора периода и сохранения
        self.Button_KP = QtWidgets.QWidget(self.WinPlateg)
        self.Button_KP.setMinimumSize(QtCore.QSize(780, 35))
        self.Button_KP.setMaximumSize(QtCore.QSize(780, 35))
        self.Button_KP.setObjectName("Button_KP")

        self.comboBox_month_KP, self.comboBox_year_KP, self.label_ERROR_KP, self.checkBox_Edit_KP, \
        self.pushButton_Save_KP, self.pushButton_Cancel_KP = ui_win_combobox(self.Button_KP)

        self.verticalLayout.addWidget(self.Button_KP)

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

        QtCore.QMetaObject.connectSlotsByName(self.WinPlateg)
        self.WinPlateg.setTabOrder(self.lineEdit_trf_Power, self.lineEdit_trf_Water)
        self.WinPlateg.setTabOrder(self.lineEdit_trf_Water, self.lineEdit_trf_Gaz)
        self.WinPlateg.setTabOrder(self.lineEdit_trf_Gaz, self.pushButton_add_Plateg_KP)
        self.WinPlateg.setTabOrder(self.pushButton_add_Plateg_KP, self.pushButton_Save_KP)
        self.WinPlateg.setTabOrder(self.pushButton_Save_KP, self.pushButton_Cancel_KP)
        self.WinPlateg.setTabOrder(self.pushButton_Cancel_KP, self.comboBox_month_KP)
        self.WinPlateg.setTabOrder(self.comboBox_month_KP, self.comboBox_year_KP)
