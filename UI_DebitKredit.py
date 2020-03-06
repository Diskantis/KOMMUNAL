# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PokazSchet.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5.QtGui import QIcon
# from PyQt5.QtWidgets import QCompleter

from Resource.UI_CLASS_KOMM import *


# окно приложения "ДОХОДЫ/РАСХОДЫ"
class UiWinDebitKredit(object):
    def setupUi_DK(self, WinDebKred):
        self.WinDebKred = WinDebKred
        self.WinDebKred.setObjectName("DebitKredit")
        self.WinDebKred.setWindowModality(QtCore.Qt.ApplicationModal)
        self.WinDebKred.resize(800, 400)
        self.WinDebKred.setGeometry(QtCore.QRect(560, 200, 800, 400))
        self.WinDebKred.setMinimumSize(QtCore.QSize(800, 400))
        self.WinDebKred.setFixedWidth(800)
        self.WinDebKred.setWindowTitle("ДОХОДЫ/РАСХОДЫ")
        self.WinDebKred.setWindowIcon(QIcon('Resource/img/dollar.png'))
        self.WinDebKred.setStyleSheet("background-color: rgb(78, 79, 84);")

        self.verticalLayout = QtWidgets.QVBoxLayout(self.WinDebKred)
        self.verticalLayout.setObjectName("verticalLayout")

        # виджет с кнопками прокрутки периода и заголовком
        self.Label_DK = QtWidgets.QWidget(self.WinDebKred)
        self.Label_DK.setMaximumSize(QtCore.QSize(800, 34))
        self.Label_DK.setObjectName("Label_DK")

        self.label_month_year_DK, self.btn_Left_DK, self.btn_Right_DK, self.label_OK_DK = ui_win_head(self.Label_DK)

        self.label_month_year_DK.setGeometry(QtCore.QRect(35, 0, 710, 30))
        self.btn_Left_DK.setGeometry(QtCore.QRect(0, 0, 30, 30))
        self.btn_Right_DK.setGeometry(QtCore.QRect(749, 0, 30, 30))
        self.label_OK_DK.setGeometry(QtCore.QRect(35, 0, 70, 30))

        self.verticalLayout.addWidget(self.Label_DK)

        self.frame = QtWidgets.QFrame(self.WinDebKred)
        self.frame.setMinimumSize(QtCore.QSize(780, 0))
        self.frame.setStyleSheet("border-radius: 5px;\n border: 1px solid rgba(209, 209, 217, 240);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

        self.verticalLayout.addWidget(self.frame)

        self.frame_PWG_DK = QtWidgets.QWidget(self.WinDebKred)
        self.frame_PWG_DK.setGeometry(QtCore.QRect(20, 52, 760, 210))
        self.frame_PWG_DK.setObjectName("frame_PWG_DK")

        self.label_Debit = label("ДОХОДЫ", self.frame_PWG_DK, 0, 2, 760, 30)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_Debit.setFont(font)
        self.label_Debit.setStyleSheet("font-weight: 700; \n color: rgb(209, 209, 217); \n padding: .1em;")

        # разделитель между ДОХОДАМИ и РАСХОДАМИ
        self.LINE_RAZDEL = QtWidgets.QFrame(self.frame_PWG_DK)
        self.LINE_RAZDEL.setGeometry(QtCore.QRect(0, 101, 760, 10))
        self.LINE_RAZDEL.setAutoFillBackground(False)
        self.LINE_RAZDEL.setStyleSheet("")
        self.LINE_RAZDEL.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.LINE_RAZDEL.setLineWidth(1)
        self.LINE_RAZDEL.setMidLineWidth(1)
        self.LINE_RAZDEL.setFrameShape(QtWidgets.QFrame.HLine)
        self.LINE_RAZDEL.setObjectName("LINE_RAZDEL")

        self.label_Kredit = label("РАСХОДЫ", self.frame_PWG_DK, 0, 107, 760, 30)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_Kredit.setFont(font)
        self.label_Kredit.setStyleSheet("font-weight: 700; \n color: rgb(209, 209, 217); \n padding: .1em;")

        # кнопка вызова метода для внесения значений ДОХОДОВ/РАСХОДОВ
        self.pushButton_add_Plateg_DK = btn("Добавить доход или расход", self.frame_PWG_DK, 10, 0, 780, 30)
        self.pushButton_add_Plateg_DK.setStyleSheet("font-weight: 700;\n color: rgb(209, 209, 217);\n "
                                                    "padding: .5em 1em;")

        self.verticalLayout.addWidget(self.pushButton_add_Plateg_DK)

        # виджет с полями для ДОХОДОВ
        self.frame_Debit = QtWidgets.QFrame(self.WinDebKred)
        self.frame_Debit.setGeometry(QtCore.QRect(20, 55, 760, 0))
        self.frame_Debit.setObjectName("frame_Plategi_KP")

        self.gLayout_Debit = QtWidgets.QGridLayout(self.frame_Debit)
        self.gLayout_Debit.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gLayout_Debit.setVerticalSpacing(1)
        self.gLayout_Debit.setContentsMargins(0, 0, 0, 0)
        self.gLayout_Debit.setObjectName("gLayout_Debit")

        # виджет с полями для РАСХОДОВ
        self.frame_Kredit = QtWidgets.QFrame(self.WinDebKred)
        self.frame_Kredit.setGeometry(QtCore.QRect(20, 140, 760, 0))
        self.frame_Kredit.setObjectName("frame_Kredit")

        self.gLayout_Kredit = QtWidgets.QGridLayout(self.frame_Kredit)
        self.gLayout_Kredit.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gLayout_Kredit.setVerticalSpacing(1)
        self.gLayout_Kredit.setContentsMargins(0, 0, 0, 0)
        self.gLayout_Kredit.setObjectName("gLayout_Kredit")

        # виджет с полем ИТОГОВОЙ СУММЫ
        self.Itog_DK = QtWidgets.QWidget(self.WinDebKred)
        self.Itog_DK.setMinimumSize(QtCore.QSize(780, 40))
        self.Itog_DK.setMaximumSize(QtCore.QSize(780, 40))
        self.Itog_DK.setObjectName("Itog_KP")

        self.frame_Itog_DK = QtWidgets.QFrame(self.Itog_DK)
        self.frame_Itog_DK.setGeometry(QtCore.QRect(0, 0, 780, 40))
        self.frame_Itog_DK.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_Itog_DK.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_Itog_DK.setStyleSheet("border-radius: 5px; \n border: 1px solid rgba(209, 209, 217, 240);")
        self.frame_Itog_DK.setObjectName("frame_Itog_KP")

        self.label_Itog_Debit = label("Итого ДОХОДОВ :", self.Itog_DK, 18, 5, 170, 30)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_Itog_Debit.setFont(font)
        self.label_Itog_Debit.setStyleSheet("font-weight: 700; \n color: rgb(209, 209, 217); \n padding: .1em;")
        self.label_Itog_Debit.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)

        color = "(255, 170, 0)"
        grad_1 = "(91, 92, 96, 255)"
        grad_2 = "(108, 109, 114, 255)"

        self.lineEdit_IS_D_sum = line_edit_pokaz(self.Itog_DK, 188, 5, 200, 30, color, grad_1, grad_2)

        self.label_Itog_Kredit = label(": Итого РАСХОДОВ", self.Itog_DK, 592, 5, 170, 30)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_Itog_Kredit.setFont(font)
        self.label_Itog_Kredit.setStyleSheet("font-weight: 700; \n color: rgb(209, 209, 217); \n padding: .1em;")
        self.label_Itog_Kredit.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)

        self.lineEdit_IS_K_sum = line_edit_pokaz(self.Itog_DK, 392, 5, 200, 30, color, grad_1, grad_2)

        self.verticalLayout.addWidget(self.Itog_DK)

        # виджет с кнопками выбора периода и сохранения
        self.Button_DK = QtWidgets.QWidget(self.WinDebKred)
        self.Button_DK.setMinimumSize(QtCore.QSize(780, 35))
        self.Button_DK.setMaximumSize(QtCore.QSize(780, 35))
        self.Button_DK.setObjectName("Button_DK")

        self.comboBox_month_DK, self.comboBox_year_DK, self.label_ERROR_DK, self.checkBox_Edit_DK, \
        self.pushButton_Save_DK, self.pushButton_Cancel_DK = ui_win_combobox(self.Button_DK)

        self.verticalLayout.addWidget(self.Button_DK)

        # выбор месяца
        self.comboBox_month_DK.setGeometry(QtCore.QRect(0, 5, 130, 30))
        # выбор года
        self.comboBox_year_DK.setGeometry(QtCore.QRect(140, 5, 90, 30))
        # поле вывода сообщения об ОШИБКЕ
        self.label_ERROR_DK.setGeometry(QtCore.QRect(230, 5, 320, 30))
        # переключатель положения РЕДАКТИРОВАНИЯ полей
        self.checkBox_Edit_DK.setGeometry(QtCore.QRect(410, 5, 130, 30))
        # кнопка СОХРАНЕНИЯ данных в базу данных
        self.pushButton_Save_DK.setGeometry(QtCore.QRect(550, 5, 110, 30))
        # кнопка ЗАКРЫТИЯ окна
        self.pushButton_Cancel_DK.setGeometry(QtCore.QRect(670, 5, 110, 30))

    def frame_plateg(self, frame_plateg, name, gLayout, position):
        self.widget_Plat = widget_plateg(frame_plateg, 10, 0, 760, 32)
        self.label_Plat = label_plateg(name, self.widget_Plat, 40, 1, 130, 30)
        self.btn_check_Plat = btn_check_plateg(self.widget_Plat, 0, 1, 30, 30)

        color = "(209, 209, 217)"
        grad_1 = "(91, 92, 96, 255)"
        grad_2 = "(108, 109, 114, 255)"

        self.lineEdit_sum_Plat = line_edit_pokaz(self.widget_Plat, 180, 1, 170, 30, color, grad_2, grad_1)
        self.lineEdit_sum_Plat.setReadOnly(False)

        self.btn_del_Plat = btn_check_plateg(self.widget_Plat, 720, 2, 30, 30)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Resource/img/icon_delete.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_del_Plat.setIcon(icon)

        gLayout.addWidget(self.widget_Plat, position, 0, 1, 1)