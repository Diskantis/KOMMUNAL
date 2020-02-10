# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PokazSchet.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon


class UiWinPokazanya(object):
    def setupUi_PS(self, WinPokazanya):
        self.WinPokazanya = WinPokazanya
        self.WinPokazanya.setObjectName("PokazanyaSchet")
        self.WinPokazanya.setWindowModality(QtCore.Qt.ApplicationModal)
        self.WinPokazanya.resize(800, 400)
        self.WinPokazanya.setMinimumSize(QtCore.QSize(800, 400))
        self.WinPokazanya.setMaximumSize(QtCore.QSize(800, 400))
        self.WinPokazanya.setWindowTitle('Показания счетчиков')
        self.WinPokazanya.setWindowIcon(QIcon('Resource/img/euro.png'))
        self.WinPokazanya.setStyleSheet("background-color: rgb(78, 79, 84);")

        self.label_month_year_PS = QtWidgets.QLabel(self.WinPokazanya)
        self.label_month_year_PS.setGeometry(QtCore.QRect(45, 10, 710, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_month_year_PS.setFont(font)
        self.label_month_year_PS.setAutoFillBackground(False)
        self.label_month_year_PS.setStyleSheet("border-radius: 4px; \n font-weight: 700;\n color: rgb(255,255,216);\n "
                                               "border: 1px solid rgba(50, 50, 50, 240);\n "
                                               "background-color: rgb(162, 162, 162);")
        self.label_month_year_PS.setAlignment(QtCore.Qt.AlignCenter)
        self.label_month_year_PS.setObjectName("label_month_year")

        self.btn_Left = QtWidgets.QPushButton("L", self.WinPokazanya)
        self.btn_Left.setGeometry(QtCore.QRect(10, 10, 30, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_Left.setFont(font)
        self.btn_Left.setStyleSheet("color: rgb(209, 209, 217);")
        self.btn_Left.setObjectName("btn_Left")

        self.btn_Right = QtWidgets.QPushButton("R", self.WinPokazanya)
        self.btn_Right.setGeometry(QtCore.QRect(760, 10, 30, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_Right.setFont(font)
        self.btn_Right.setStyleSheet("color: rgb(209, 209, 217);")
        self.btn_Right.setObjectName("btn_Right")

        self.label_OK_1 = QtWidgets.QLabel(self.WinPokazanya)
        self.label_OK_1.setGeometry(QtCore.QRect(45, 5, 70, 40))
        self.label_OK_1.setStyleSheet("image: url(:/img/galochka.png);")
        self.label_OK_1.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_OK_1.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_OK_1.setText("")
        self.label_OK_1.setStyleSheet("background-color: rgba(255, 255, 255, 0); \n border: 0px solid;")
        self.label_OK_1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_OK_1.setObjectName("label_OK_1")

        self.groupPowerBox = QtWidgets.QGroupBox("Электроэнергия", self.WinPokazanya)
        self.groupPowerBox.setGeometry(QtCore.QRect(10, 50, 230, 300))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.groupPowerBox.setFont(font)
        self.groupPowerBox.setStyleSheet("font-weight: 700;\n color: rgb(209, 209, 217);\n padding: .5em 1em; \n "
                                         "border-radius: 5px; \n border: 1px solid rgba(209, 209, 217, 240);")
        self.groupPowerBox.setAlignment(QtCore.Qt.AlignCenter)
        self.groupPowerBox.setObjectName("groupPowerBox")

        self.label_P1 = QtWidgets.QLabel("Р/С 181 820 562", self.groupPowerBox)
        self.label_P1.setGeometry(QtCore.QRect(10, 30, 210, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_P1.setFont(font)
        self.label_P1.setStyleSheet("color: rgb(80, 80, 80); \n background-color: rgb(255, 255, 0); \n "
                                    "font-weight: 700; \n padding: .4em; \n "
                                    "border: 1px solid rgba(50, 50, 50, 240); \n border-radius: 4px; \n ")
        self.label_P1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_P1.setObjectName("label_P1")

        self.label_P2 = QtWidgets.QLabel("предыдущие", self.groupPowerBox)
        self.label_P2.setGeometry(QtCore.QRect(10, 55, 100, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_P2.setFont(font)
        self.label_P2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_P2.setStyleSheet("font-weight: 600; \n color: rgb(209, 209, 217); \n padding: .3em; \n border: 0px;")
        self.label_P2.setObjectName("label_P2")

        self.label_P3 = QtWidgets.QLabel("последние", self.groupPowerBox)
        self.label_P3.setGeometry(QtCore.QRect(120, 55, 100, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_P3.setFont(font)
        self.label_P3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_P3.setStyleSheet("font-weight: 600; \n color: rgb(209, 209, 217); \n padding: .3em; \n border: 0px;")
        self.label_P3.setObjectName("label_P3")

        self.lineEdit_pokaz_P1 = QtWidgets.QLineEdit(self.groupPowerBox)
        self.lineEdit_pokaz_P1.setGeometry(QtCore.QRect(10, 80, 100, 150))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        self.lineEdit_pokaz_P1.setFont(font)
        self.lineEdit_pokaz_P1.setStyleSheet("border-radius: 4px; \n color: rgb(0, 160, 0); \n "
                                             "border: 1px solid rgba(50, 50, 50, 240); \n "
                                             "background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, "
                                             "stop:0 rgba(125, 126, 131, 255), stop:0.01 rgba(91, 92, 96, 255), "
                                             "stop:0.99 rgba(108, 109, 114, 255), stop:1 rgba(125, 126, 131, 255));")
        self.lineEdit_pokaz_P1.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_pokaz_P1.setReadOnly(True)
        self.lineEdit_pokaz_P1.setObjectName("label_pokaz_P1")

        self.lineEdit_P1 = QtWidgets.QLineEdit(self.groupPowerBox)
        self.lineEdit_P1.setGeometry(QtCore.QRect(120, 80, 100, 150))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        self.lineEdit_P1.setFont(font)
        self.lineEdit_P1.setMaxLength(5)
        self.lineEdit_P1.setStyleSheet("border-radius: 4px; \n color: rgb(0, 160, 0); \n "
                                       "border: 1px solid rgba(50, 50, 50, 240); \n "
                                       "background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, "
                                       "stop:0 rgba(125, 126, 131, 255), stop:0.01 rgba(108, 109, 114, 255), "
                                       "stop:0.99 rgba(91, 92, 96, 255), stop:1 rgba(125, 126, 131, 255));")
        self.lineEdit_P1.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_P1.setObjectName("lineEdit_P1")

        self.label_PM_1 = QtWidgets.QLabel("месячный расход", self.groupPowerBox)
        self.label_PM_1.setGeometry(QtCore.QRect(10, 235, 210, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_PM_1.setFont(font)
        self.label_PM_1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_PM_1.setStyleSheet("font-weight: 600; \n color: rgb(209, 209, 217); \n "
                                      "padding: .3em; \n border: 0px;")
        self.label_PM_1.setObjectName("label_PM_1")

        self.label_PM_2 = QtWidgets.QLabel(self.groupPowerBox)
        self.label_PM_2.setGeometry(QtCore.QRect(10, 260, 210, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        self.label_PM_2.setFont(font)
        self.label_PM_2.setStyleSheet("border-radius: 4px; \n color: rgb(0, 160, 0); \n "
                                      "border: 1px solid rgba(50, 50, 50, 240); \n "
                                      "background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, "
                                      "stop:0 rgba(125, 126, 131, 255), stop:0.02 rgba(91, 92, 96, 255), "
                                      "stop:0.98 rgba(108, 109, 114, 255), stop:1 rgba(125, 126, 131, 255));")
        self.label_PM_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_PM_2.setObjectName("label_PM_2")

        self.groupWaterBox = QtWidgets.QGroupBox("Вода", self.WinPokazanya)
        self.groupWaterBox.setGeometry(QtCore.QRect(250, 50, 300, 300))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.groupWaterBox.setFont(font)
        self.groupWaterBox.setStyleSheet("font-weight: 700;\n color: rgb(209, 209, 217);\n padding: .5em 1em; \n "
                                         "border-radius: 5px; \n border: 1px solid rgba(209, 209, 217, 240);")
        self.groupWaterBox.setAlignment(QtCore.Qt.AlignCenter)
        self.groupWaterBox.setObjectName("groupWaterBox")

        self.label_W1 = QtWidgets.QLabel("Р/С 300 046 056 19", self.groupWaterBox)
        self.label_W1.setGeometry(QtCore.QRect(10, 30, 280, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_W1.setFont(font)
        self.label_W1.setStyleSheet("color: rgb(80, 80, 80); \n background-color: rgb(85, 170, 255); \n "
                                    "font-weight: 700; \n padding: .4em; \n "
                                    "border: 1px solid rgba(50, 50, 50, 240); \n border-radius: 4px; \n ")
        self.label_W1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_W1.setObjectName("label_W1")

        self.label_W2 = QtWidgets.QLabel("счетчик", self.groupWaterBox)
        self.label_W2.setGeometry(QtCore.QRect(10, 55, 100, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_W2.setFont(font)
        self.label_W2.setStyleSheet("font-weight: 600; \n color: rgb(209, 209, 217); \n padding: .3em; \n border: 0px;")
        self.label_W2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_W2.setObjectName("label_W2")

        self.label_W3 = QtWidgets.QLabel("предыдущие", self.groupWaterBox)
        self.label_W3.setGeometry(QtCore.QRect(110, 55, 100, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_W3.setFont(font)
        self.label_W3.setStyleSheet("font-weight: 600; \n color: rgb(209, 209, 217); \n padding: .3em; \n border: 0px;")
        self.label_W3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_W3.setObjectName("label_W3")

        self.label_W4 = QtWidgets.QLabel("последние", self.groupWaterBox)
        self.label_W4.setGeometry(QtCore.QRect(210, 55, 80, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_W4.setFont(font)
        self.label_W4.setStyleSheet("font-weight: 600; \n color: rgb(209, 209, 217); \n "
                                    "padding: .3em; \n border: 0px;")
        self.label_W4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_W4.setObjectName("label_W4")

        self.label_W5_1 = QtWidgets.QLabel("№1", self.groupWaterBox)
        self.label_W5_1.setGeometry(QtCore.QRect(10, 80, 25, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_W5_1.setFont(font)
        self.label_W5_1.setStyleSheet("font-weight: 600; \n color: rgb(209, 209, 217); \n "
                                      "padding: .1em; \n border: 0px;")
        self.label_W5_1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_W5_1.setObjectName("label_W5_1")

        self.label_W5_2 = QtWidgets.QLabel("Туалет (хл)", self.groupWaterBox)
        self.label_W5_2.setGeometry(QtCore.QRect(40, 80, 80, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_W5_2.setFont(font)
        self.label_W5_2.setStyleSheet("color: rgb(0, 170, 255); \n padding: .0em; \n border: 0px;")
        self.label_W5_2.setScaledContents(False)
        self.label_W5_2.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label_W5_2.setObjectName("label_W5_2")

        self.label_W6_1 = QtWidgets.QLabel("№2", self.groupWaterBox)
        self.label_W6_1.setGeometry(QtCore.QRect(10, 120, 25, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_W6_1.setFont(font)
        self.label_W6_1.setStyleSheet("font-weight: 600; \n color: rgb(209, 209, 217); \n "
                                      "padding: .1em; \n border: 0px;")
        self.label_W6_1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_W6_1.setObjectName("label_W6_1")

        self.label_W6_2 = QtWidgets.QLabel("Туалет (гр)", self.groupWaterBox)
        self.label_W6_2.setGeometry(QtCore.QRect(40, 120, 80, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_W6_2.setFont(font)
        self.label_W6_2.setStyleSheet("color: rgb(255, 140, 0); \n padding: .0em; \n border: 0px;")
        self.label_W6_2.setScaledContents(False)
        self.label_W6_2.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label_W6_2.setObjectName("label_W6_2")

        self.label_W7_1 = QtWidgets.QLabel("№3", self.groupWaterBox)
        self.label_W7_1.setGeometry(QtCore.QRect(10, 160, 25, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_W7_1.setFont(font)
        self.label_W7_1.setStyleSheet("font-weight: 600; \n color: rgb(209, 209, 217); \n "
                                      "padding: .1em; \n border: 0px;")
        self.label_W7_1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_W7_1.setObjectName("label_W7_1")

        self.label_W7_2 = QtWidgets.QLabel("Кухня (хл)", self.groupWaterBox)
        self.label_W7_2.setGeometry(QtCore.QRect(40, 160, 80, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_W7_2.setFont(font)
        self.label_W7_2.setStyleSheet("color: rgb(0, 170, 255); \n padding: .0em; \n border: 0px;")
        self.label_W7_2.setScaledContents(False)
        self.label_W7_2.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label_W7_2.setObjectName("label_W7_2")

        self.label_W8_1 = QtWidgets.QLabel("№4", self.groupWaterBox)
        self.label_W8_1.setGeometry(QtCore.QRect(10, 200, 25, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_W8_1.setFont(font)
        self.label_W8_1.setStyleSheet("font-weight: 600; \n color: rgb(209, 209, 217); \n "
                                      "padding: .1em; \n border: 0px;")
        self.label_W8_1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_W8_1.setObjectName("label_W8_1")

        self.label_W8_2 = QtWidgets.QLabel("Кухня (гр)", self.groupWaterBox)
        self.label_W8_2.setGeometry(QtCore.QRect(40, 200, 80, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_W8_2.setFont(font)
        self.label_W8_2.setStyleSheet("color: rgb(255, 140, 0); \n padding: .0em; \n border: 0px;")
        self.label_W8_2.setScaledContents(False)
        self.label_W8_2.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label_W8_2.setObjectName("label_W8_2")

        self.lineEdit_pokaz_W1 = QtWidgets.QLineEdit(self.groupWaterBox)
        self.lineEdit_pokaz_W1.setGeometry(QtCore.QRect(120, 80, 80, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        self.lineEdit_pokaz_W1.setFont(font)
        self.lineEdit_pokaz_W1.setStyleSheet("border-radius: 4px; \n color: rgb(0, 170, 255); \n "
                                             "border: 1px solid rgba(50, 50, 50, 240); \n "
                                             "background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, "
                                             "stop:0 rgba(125, 126, 131, 255), stop:0.01 rgba(91, 92, 96, 255), "
                                             "stop:0.99 rgba(108, 109, 114, 255), stop:1 rgba(125, 126, 131, 255));")
        self.lineEdit_pokaz_W1.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_pokaz_W1.setReadOnly(True)
        self.lineEdit_pokaz_W1.setObjectName("label_pokaz_W1")

        self.lineEdit_pokaz_W2 = QtWidgets.QLineEdit(self.groupWaterBox)
        self.lineEdit_pokaz_W2.setGeometry(QtCore.QRect(120, 120, 80, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        self.lineEdit_pokaz_W2.setFont(font)
        self.lineEdit_pokaz_W2.setStyleSheet("border-radius: 4px; \n color: rgb(255, 140, 0); \n "
                                             "border: 1px solid rgba(50, 50, 50, 240); \n "
                                             "background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, "
                                             "stop:0 rgba(125, 126, 131, 255), stop:0.01 rgba(91, 92, 96, 255), "
                                             "stop:0.99 rgba(108, 109, 114, 255), stop:1 rgba(125, 126, 131, 255));")
        self.lineEdit_pokaz_W2.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_pokaz_W2.setReadOnly(True)
        self.lineEdit_pokaz_W2.setObjectName("label_pokaz_W2")

        self.lineEdit_pokaz_W3 = QtWidgets.QLineEdit(self.groupWaterBox)
        self.lineEdit_pokaz_W3.setGeometry(QtCore.QRect(120, 160, 80, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        self.lineEdit_pokaz_W3.setFont(font)
        self.lineEdit_pokaz_W3.setStyleSheet("border-radius: 4px; \n color: rgb(0, 170, 255); \n "
                                             "border: 1px solid rgba(50, 50, 50, 240); \n "
                                             "background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, "
                                             "stop:0 rgba(125, 126, 131, 255), stop:0.01 rgba(91, 92, 96, 255), "
                                             "stop:0.99 rgba(108, 109, 114, 255), stop:1 rgba(125, 126, 131, 255));")
        self.lineEdit_pokaz_W3.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_pokaz_W3.setReadOnly(True)
        self.lineEdit_pokaz_W3.setObjectName("label_pokaz_W3")

        self.lineEdit_pokaz_W4 = QtWidgets.QLineEdit(self.groupWaterBox)
        self.lineEdit_pokaz_W4.setGeometry(QtCore.QRect(120, 200, 80, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        self.lineEdit_pokaz_W4.setFont(font)
        self.lineEdit_pokaz_W4.setStyleSheet("border-radius: 4px; \n color: rgb(255, 140, 0); \n "
                                             "border: 1px solid rgba(50, 50, 50, 240); \n "
                                             "background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, "
                                             "stop:0 rgba(125, 126, 131, 255), stop:0.01 rgba(91, 92, 96, 255), "
                                             "stop:0.99 rgba(108, 109, 114, 255), stop:1 rgba(125, 126, 131, 255));")
        self.lineEdit_pokaz_W4.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_pokaz_W4.setReadOnly(True)
        self.lineEdit_pokaz_W4.setObjectName("label_pokaz_W4")

        self.lineEdit_W1 = QtWidgets.QLineEdit(self.groupWaterBox)
        self.lineEdit_W1.setGeometry(QtCore.QRect(210, 80, 80, 30))
        self.lineEdit_W1.setAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        self.lineEdit_W1.setFont(font)
        self.lineEdit_W1.setMaxLength(3)
        self.lineEdit_W1.setStyleSheet("border-radius: 4px; \n color: rgb(0, 170, 255); \n "
                                       "border: 1px solid rgba(50, 50, 50, 240); \n "
                                       "background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, "
                                       "stop:0 rgba(125, 126, 131, 255), stop:0.01 rgba(108, 109, 114, 255), "
                                       "stop:0.99 rgba(91, 92, 96, 255), stop:1 rgba(125, 126, 131, 255));")
        self.lineEdit_W1.setObjectName("lineEdit_W1")

        self.lineEdit_W2 = QtWidgets.QLineEdit(self.groupWaterBox)
        self.lineEdit_W2.setGeometry(QtCore.QRect(210, 120, 80, 30))
        self.lineEdit_W2.setAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        self.lineEdit_W2.setFont(font)
        self.lineEdit_W2.setMaxLength(3)
        self.lineEdit_W2.setStyleSheet("border-radius: 4px; \n color: rgb(255, 140, 0); \n "
                                       "border: 1px solid rgba(50, 50, 50, 240); \n "
                                       "background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, "
                                       "stop:0 rgba(125, 126, 131, 255), stop:0.01 rgba(108, 109, 114, 255), "
                                       "stop:0.99 rgba(91, 92, 96, 255), stop:1 rgba(125, 126, 131, 255));")
        self.lineEdit_W2.setObjectName("lineEdit_W2")

        self.lineEdit_W3 = QtWidgets.QLineEdit(self.groupWaterBox)
        self.lineEdit_W3.setGeometry(QtCore.QRect(210, 160, 80, 30))
        self.lineEdit_W3.setAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        self.lineEdit_W3.setFont(font)
        self.lineEdit_W3.setMaxLength(3)
        self.lineEdit_W3.setStyleSheet("border-radius: 4px; \n color: rgb(0, 170, 255); \n "
                                       "border: 1px solid rgba(50, 50, 50, 240); \n "
                                       "background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, "
                                       "stop:0 rgba(125, 126, 131, 255), stop:0.01 rgba(108, 109, 114, 255), "
                                       "stop:0.99 rgba(91, 92, 96, 255), stop:1 rgba(125, 126, 131, 255));")
        self.lineEdit_W3.setObjectName("lineEdit_W3")

        self.lineEdit_W4 = QtWidgets.QLineEdit(self.groupWaterBox)
        self.lineEdit_W4.setGeometry(QtCore.QRect(210, 200, 80, 30))
        self.lineEdit_W4.setAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        self.lineEdit_W4.setFont(font)
        self.lineEdit_W4.setMaxLength(3)
        self.lineEdit_W4.setStyleSheet("border-radius: 4px; \n color: rgb(255, 140, 0); \n "
                                       "border: 1px solid rgba(50, 50, 50, 240); \n "
                                       "background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, "
                                       "stop:0 rgba(125, 126, 131, 255), stop:0.01 rgba(108, 109, 114, 255), "
                                       "stop:0.99 rgba(91, 92, 96, 255), stop:1 rgba(125, 126, 131, 255));")
        self.lineEdit_W4.setObjectName("lineEdit_W4")

        self.horizontalLayoutWidget = QtWidgets.QWidget(self.groupWaterBox)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 260, 280, 30))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayoutWidget.setStyleSheet("border: 0px;")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.label_WM_1 = QtWidgets.QLabel("месячный расход", self.groupWaterBox)
        self.label_WM_1.setGeometry(QtCore.QRect(10, 235, 280, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_WM_1.setFont(font)
        self.label_WM_1.setStyleSheet("font-weight: 600; \n color: rgb(209, 209, 217); \n "
                                      "padding: .3em; \n border: 0px;")
        self.label_WM_1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_WM_1.setObjectName("label_WM_1")

        self.label_WM_2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_WM_2.setMaximumSize(QtCore.QSize(90, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        self.label_WM_2.setFont(font)
        self.label_WM_2.setStyleSheet("border-radius: 4px; \n color: rgb(0, 170, 255); \n "
                                      "border: 1px solid rgba(50, 50, 50, 240); \n "
                                      "background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, "
                                      "stop:0 rgba(125, 126, 131, 255), stop:0.02 rgba(91, 92, 96, 255), "
                                      "stop:0.98 rgba(108, 109, 114, 255), stop:1 rgba(125, 126, 131, 255));")
        self.label_WM_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_WM_2.setObjectName("label_WM_2")
        self.horizontalLayout.addWidget(self.label_WM_2)

        self.label_WM_3 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_WM_3.setMaximumSize(QtCore.QSize(10, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(75)
        self.label_WM_3.setFont(font)
        self.label_WM_3.setStyleSheet("font-weight: 600; \n color: rgb(209, 209, 217); \n border: 0px;")
        self.label_WM_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_WM_3.setText('+')
        self.label_WM_3.setObjectName("label_WM_3")
        self.horizontalLayout.addWidget(self.label_WM_3)

        self.label_WM_4 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_WM_4.setMaximumSize(QtCore.QSize(90, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        self.label_WM_4.setFont(font)
        self.label_WM_4.setStyleSheet("border-radius: 4px; \n color: rgb(255, 140, 0); \n "
                                      "border: 1px solid rgba(50, 50, 50, 240); \n "
                                      "background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, "
                                      "stop:0 rgba(125, 126, 131, 255), stop:0.02 rgba(91, 92, 96, 255), "
                                      "stop:0.98 rgba(108, 109, 114, 255), stop:1 rgba(125, 126, 131, 255));")
        self.label_WM_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_WM_4.setObjectName("label_WM_4")
        self.horizontalLayout.addWidget(self.label_WM_4)

        self.label_WM_5 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_WM_5.setMaximumSize(QtCore.QSize(10, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(75)
        self.label_WM_5.setFont(font)
        self.label_WM_5.setStyleSheet("font-weight: 600; \n color: rgb(209, 209, 217); \n border: 0px;")
        self.label_WM_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_WM_5.setText('=')
        self.label_WM_5.setObjectName("label_WM_5")
        self.horizontalLayout.addWidget(self.label_WM_5)

        self.label_WM_6 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_WM_6.setMaximumSize(QtCore.QSize(90, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        self.label_WM_6.setFont(font)
        self.label_WM_6.setStyleSheet("border-radius: 4px; \n color: rgb(40, 40, 40); \n "
                                      "border: 1px solid rgba(50, 50, 50, 240); \n "
                                      "background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, "
                                      "stop:0 rgba(125, 126, 131, 255), stop:0.02 rgba(91, 92, 96, 255), "
                                      "stop:0.98 rgba(108, 109, 114, 255), stop:1 rgba(125, 126, 131, 255));")
        self.label_WM_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_WM_6.setObjectName("label_WM_6")
        self.horizontalLayout.addWidget(self.label_WM_6)

        self.groupGazBox = QtWidgets.QGroupBox("Газ", self.WinPokazanya)
        self.groupGazBox.setGeometry(QtCore.QRect(560, 50, 230, 300))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.groupGazBox.setFont(font)
        self.groupGazBox.setStyleSheet("font-weight: 700;\n color: rgb(209, 209, 217);\n padding: .5em 1em; \n "
                                       "border-radius: 5px; \n border: 1px solid rgba(209, 209, 217, 240);")
        self.groupGazBox.setAlignment(QtCore.Qt.AlignCenter)
        self.groupGazBox.setObjectName("groupGazBox")

        self.label_G1 = QtWidgets.QLabel("Р/С 171 269 - 5", self.groupGazBox)
        self.label_G1.setGeometry(QtCore.QRect(10, 30, 210, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_G1.setFont(font)
        self.label_G1.setStyleSheet("color: rgb(80, 80, 80); \n background-color: rgb(255, 85, 255); \n "
                                    "font-weight: 700; \n padding: .4em; \n "
                                    "border: 1px solid rgba(50, 50, 50, 240); \n border-radius: 4px; \n ")
        self.label_G1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_G1.setObjectName("label_G1")

        self.label_G2 = QtWidgets.QLabel("предыдущие", self.groupGazBox)
        self.label_G2.setGeometry(QtCore.QRect(10, 55, 100, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_G2.setFont(font)
        self.label_G2.setStyleSheet("font-weight: 600; \n color: rgb(209, 209, 217); \n padding: .3em; \n border: 0px;")
        self.label_G2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_G2.setObjectName("label_G2")

        self.label_G3 = QtWidgets.QLabel("последние", self.groupGazBox)
        self.label_G3.setGeometry(QtCore.QRect(120, 55, 100, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_G3.setFont(font)
        self.label_G3.setStyleSheet("font-weight: 600; \n color: rgb(209, 209, 217); \n padding: .3em; \n border: 0px;")
        self.label_G3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_G3.setObjectName("label_G3")

        self.lineEdit_pokaz_G1 = QtWidgets.QLineEdit(self.groupGazBox)
        self.lineEdit_pokaz_G1.setGeometry(QtCore.QRect(10, 80, 100, 150))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        self.lineEdit_pokaz_G1.setFont(font)
        self.lineEdit_pokaz_G1.setStyleSheet("border-radius: 4px; \n color: rgb(150, 0, 150); \n "
                                             "border: 1px solid rgba(50, 50, 50, 240); \n "
                                             "background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, "
                                             "stop:0 rgba(125, 126, 131, 255), stop:0.01 rgba(91, 92, 96, 255), "
                                             "stop:0.99 rgba(108, 109, 114, 255), stop:1 rgba(125, 126, 131, 255));")
        self.lineEdit_pokaz_G1.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_pokaz_G1.setReadOnly(True)
        self.lineEdit_pokaz_G1.setObjectName("label_pokaz_G1")

        self.lineEdit_G1 = QtWidgets.QLineEdit(self.groupGazBox)
        self.lineEdit_G1.setGeometry(QtCore.QRect(120, 80, 100, 150))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        self.lineEdit_G1.setFont(font)
        self.lineEdit_G1.setMaxLength(4)
        self.lineEdit_G1.setStyleSheet("border-radius: 4px; \n color: rgb(150, 0, 150); \n "
                                       "border: 1px solid rgba(50, 50, 50, 240); \n "
                                       "background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, "
                                       "stop:0 rgba(125, 126, 131, 255), stop:0.01 rgba(108, 109, 114, 255), "
                                       "stop:0.99 rgba(91, 92, 96, 255), stop:1 rgba(125, 126, 131, 255));")
        self.lineEdit_G1.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_G1.setObjectName("lineEdit_G1")

        self.label_GM_1 = QtWidgets.QLabel("месячный расход", self.groupGazBox)
        self.label_GM_1.setGeometry(QtCore.QRect(10, 235, 210, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_GM_1.setFont(font)
        self.label_GM_1.setStyleSheet("font-weight: 600; \n color: rgb(209, 209, 217); \n "
                                      "padding: .3em; \n border: 0px;")
        self.label_GM_1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_GM_1.setObjectName("label_GM_1")

        self.label_GM_2 = QtWidgets.QLabel(self.groupGazBox)
        self.label_GM_2.setGeometry(QtCore.QRect(10, 260, 210, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        self.label_GM_2.setFont(font)
        self.label_GM_2.setStyleSheet("border-radius: 4px; \n color: rgb(150, 0, 150); \n "
                                      "border: 1px solid rgba(50, 50, 50, 240); \n "
                                      "background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, "
                                      "stop:0 rgba(125, 126, 131, 255), stop:0.02 rgba(91, 92, 96, 255), "
                                      "stop:0.98 rgba(108, 109, 114, 255), stop:1 rgba(125, 126, 131, 255));")
        self.label_GM_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_GM_2.setObjectName("label_GM_2")

        # выбор месяца
        self.comboBox_month_PS = QtWidgets.QComboBox(self.WinPokazanya)
        self.comboBox_month_PS.setGeometry(QtCore.QRect(10, 360, 130, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.comboBox_month_PS.setFont(font)
        self.comboBox_month_PS.setStyleSheet("font-size: 50%;\n font-weight: 700;\n color: rgb(209, 209, 217);")
        self.comboBox_month_PS.setObjectName("comboBox_month")

        # выбор года
        self.comboBox_year_PS = QtWidgets.QComboBox(self.WinPokazanya)
        self.comboBox_year_PS.setGeometry(QtCore.QRect(150, 360, 90, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.comboBox_year_PS.setFont(font)
        self.comboBox_year_PS.setStyleSheet("font-size: 50%;\n font-weight: 700;\n color: rgb(209, 209, 217);")
        self.comboBox_year_PS.setObjectName("comboBox_year")

        # поле вывода сообщения об ОШИБКЕ
        self.label_ERROR = QtWidgets.QLabel(self.WinPokazanya)
        self.label_ERROR.setGeometry(QtCore.QRect(250, 360, 300, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        self.label_ERROR.setFont(font)
        self.label_ERROR.setStyleSheet("font-weight: 700;\n color: rgb(209, 209, 217);\n padding: .4em 1em; \n "
                                       "color: rgb(255, 0, 0);")
        self.label_ERROR.setAlignment(QtCore.Qt.AlignCenter)
        self.label_ERROR.setObjectName("label_ERROR")

        # переключатель положения РЕДАКТИРОВАНИЯ полей
        self.checkBox_Edit_PS = QtWidgets.QCheckBox("Редактирование", self.WinPokazanya)
        self.checkBox_Edit_PS.setGeometry(QtCore.QRect(420, 360, 130, 30))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.checkBox_Edit_PS.setFont(font)
        self.checkBox_Edit_PS.setStyleSheet("font-weight: 600; \n color: rgb(209, 209, 217); \n border: 0px;")
        self.checkBox_Edit_PS.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.checkBox_Edit_PS.setObjectName("checkBox")

        # кнопка СОХРАНЕНИЯ данных в базу данных
        self.pushButton_Save_PS = QtWidgets.QPushButton("Сохранить", self.WinPokazanya)
        self.pushButton_Save_PS.setGeometry(QtCore.QRect(560, 360, 110, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_Save_PS.setFont(font)
        self.pushButton_Save_PS.setStyleSheet("font-weight: 700;\n color: rgb(209, 209, 217);\n padding: .5em 1em;")
        self.pushButton_Save_PS.setObjectName("pushButton_Save")

        # кнопка ЗАКРЫТИЯ окна
        self.pushButton_Cancel_PS = QtWidgets.QPushButton("Cancel", self.WinPokazanya)
        self.pushButton_Cancel_PS.setGeometry(QtCore.QRect(680, 360, 110, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_Cancel_PS.setFont(font)
        self.pushButton_Cancel_PS.setStyleSheet("font-weight: 700;\n color: rgb(209, 209, 217);\n padding: .5em 1em;")
        self.pushButton_Cancel_PS.setObjectName("pushButton_Cancel")

        QtCore.QMetaObject.connectSlotsByName(self.WinPokazanya)
        self.WinPokazanya.setTabOrder(self.lineEdit_P1, self.lineEdit_W1)
        self.WinPokazanya.setTabOrder(self.lineEdit_W1, self.lineEdit_W2)
        self.WinPokazanya.setTabOrder(self.lineEdit_W2, self.lineEdit_W3)
        self.WinPokazanya.setTabOrder(self.lineEdit_W3, self.lineEdit_W4)
        self.WinPokazanya.setTabOrder(self.lineEdit_W4, self.lineEdit_G1)
        self.WinPokazanya.setTabOrder(self.lineEdit_G1, self.pushButton_Save_PS)
        self.WinPokazanya.setTabOrder(self.pushButton_Save_PS, self.pushButton_Cancel_PS)
        self.WinPokazanya.setTabOrder(self.pushButton_Cancel_PS, self.checkBox_Edit_PS)
        self.WinPokazanya.setTabOrder(self.checkBox_Edit_PS, self.comboBox_month_PS)
        self.WinPokazanya.setTabOrder(self.comboBox_month_PS, self.comboBox_year_PS)
        self.WinPokazanya.setTabOrder(self.comboBox_year_PS, self.lineEdit_pokaz_P1)
        self.WinPokazanya.setTabOrder(self.lineEdit_pokaz_P1, self.lineEdit_pokaz_W1)
        self.WinPokazanya.setTabOrder(self.lineEdit_pokaz_W1, self.lineEdit_pokaz_W2)
        self.WinPokazanya.setTabOrder(self.lineEdit_pokaz_W2, self.lineEdit_pokaz_W3)
        self.WinPokazanya.setTabOrder(self.lineEdit_pokaz_W3, self.lineEdit_pokaz_W4)
        self.WinPokazanya.setTabOrder(self.lineEdit_pokaz_W4, self.lineEdit_pokaz_G1)
