# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PokazSchet.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


def ui_win_head(Win_app):
    label_month_year = label("", Win_app, 45, 10, 710, 30)
    font = QtGui.QFont()
    font.setPointSize(14)
    label_month_year.setFont(font)
    label_month_year.setStyleSheet("border-radius: 4px; \n font-weight: 700;\n color: rgb(255,255,216);\n "
                                   "border: 1px solid rgba(50, 50, 50, 240);\n "
                                   "background-color: rgb(162, 162, 162);")

    btn_Left = btn("L", Win_app, 10, 10, 30, 30)
    btn_Right = btn("R", Win_app, 760, 10, 30, 30)

    label_OK = label("", Win_app, 45, 5, 70, 40)
    label_OK.setStyleSheet("image: url(:/img/galochka.png);")
    label_OK.setStyleSheet("background-color: rgba(255, 255, 255, 0); \n border: 0px solid;")
    return label_month_year, btn_Left, btn_Right, label_OK


def ui_win_combobox(Win_app):
    comboBox_month = combo_box(Win_app, 10, 360, 130, 30)  # выбор месяца
    comboBox_year = combo_box(Win_app, 150, 360, 90, 30)  # выбор года

    # поле вывода сообщения об ОШИБКЕ
    label_ERROR = label("", Win_app, 250, 360, 300, 30)
    font = QtGui.QFont()
    font.setPointSize(12)
    label_ERROR.setFont(font)
    label_ERROR.setStyleSheet("font-weight: 700;\n color: rgb(209, 209, 217);\n padding: .4em 1em; \n "
                              "color: rgb(255, 0, 0);")

    # переключатель положения РЕДАКТИРОВАНИЯ полей
    checkBox_Edit = QtWidgets.QCheckBox("Редактирование", Win_app)
    checkBox_Edit.setGeometry(QtCore.QRect(420, 360, 130, 30))
    font = QtGui.QFont()
    font.setPointSize(9)
    checkBox_Edit.setFont(font)
    checkBox_Edit.setStyleSheet("font-weight: 600; \n color: rgb(209, 209, 217); \n border: 0px;")
    checkBox_Edit.setLayoutDirection(QtCore.Qt.RightToLeft)
    checkBox_Edit.setObjectName("checkBox")

    # кнопка СОХРАНЕНИЯ данных в базу данных
    pushButton_Save = btn("Сохранить", Win_app, 560, 360, 110, 30)
    pushButton_Save.setStyleSheet("font-weight: 700;\n color: rgb(209, 209, 217);\n padding: .5em 1em;")

    pushButton_Cancel = btn("Отмена", Win_app, 680, 360, 110, 30)
    pushButton_Cancel.setStyleSheet("font-weight: 700;\n color: rgb(209, 209, 217);\n padding: .5em 1em;")
    return comboBox_month, comboBox_year, label_ERROR, checkBox_Edit, pushButton_Save, pushButton_Cancel


def btn(btn_name, group, x, y, xl, yl):
    btn_push = QtWidgets.QPushButton(btn_name, group)
    btn_push.setGeometry(QtCore.QRect(x, y, xl, yl))
    font = QtGui.QFont()
    font.setPointSize(10)
    btn_push.setFont(font)
    btn_push.setStyleSheet("color: rgb(209, 209, 217);")
    btn_push.setObjectName("btn")
    return btn_push


def label(label_name, group, x, y, xl, yl):
    label_str = QtWidgets.QLabel(label_name, group)
    label_str.setGeometry(QtCore.QRect(x, y, xl, yl))
    font = QtGui.QFont()
    font.setPointSize(10)
    label_str.setFont(font)
    label_str.setStyleSheet("font-weight: 600; \n color: rgb(209, 209, 217); \n padding: .3em; \n border: 0px;")
    label_str.setAlignment(QtCore.Qt.AlignCenter)
    label_str.setObjectName("label_name")
    return label_str


def label_place(place, group, x, y, xl, yl, color):
    label_place_str = QtWidgets.QLabel(place, group)
    label_place_str.setGeometry(QtCore.QRect(x, y, xl, yl))
    font = QtGui.QFont()
    font.setPointSize(10)
    label_place_str.setFont(font)
    label_place_str.setStyleSheet("color: rgb" + color + "; \n padding: .0em; \n border: 0px;")
    label_place_str.setScaledContents(False)
    label_place_str.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
    label_place_str.setObjectName("label_place")
    return label_place_str


def line_edit_pokaz(group, x, y, xl, yl, color, grad_1, grad_2):
    lineEdit_pokaz = QtWidgets.QLineEdit(group)
    lineEdit_pokaz.setGeometry(QtCore.QRect(x, y, xl, yl))
    font = QtGui.QFont()
    font.setPointSize(12)
    font.setWeight(75)
    lineEdit_pokaz.setFont(font)
    lineEdit_pokaz.setStyleSheet(
        "border-radius: 4px; \n color: rgb" + color + "; \n border: 1px solid rgba(50, 50, 50, 240); \n "
        "background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(125, 126, 131, 255), "
        "stop:0.01 rgba" + grad_1 + ", stop:0.99 rgba" + grad_2 + ", stop:1 rgba(125, 126, 131, 255));")
    lineEdit_pokaz.setAlignment(QtCore.Qt.AlignCenter)
    lineEdit_pokaz.setReadOnly(True)
    lineEdit_pokaz.setObjectName("lineEdit_pokaz")
    return lineEdit_pokaz


def label_month_ras(name, group, x, y, xl, yl, color, grad_1, grad_2):
    label_str_month_ras = QtWidgets.QLabel(name, group)
    label_str_month_ras.setGeometry(QtCore.QRect(x, y, xl, yl))
    font = QtGui.QFont()
    font.setPointSize(12)
    font.setWeight(75)
    label_str_month_ras.setFont(font)
    label_str_month_ras.setStyleSheet(
        "border-radius: 4px; \n color: rgb" + color + "; \n border: 1px solid rgba(50, 50, 50, 240); \n "
        "background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(125, 126, 131, 255), "
        "stop:0.02 rgba" + grad_1 + ", stop:0.98 rgba" + grad_2 + ", stop:1 rgba(125, 126, 131, 255));")
    label_str_month_ras.setAlignment(QtCore.Qt.AlignCenter)
    label_str_month_ras.setObjectName("label_month_ras")
    return label_str_month_ras


def combo_box(group, x, y, xl, yl):
    c_box = QtWidgets.QComboBox(group)
    c_box.setGeometry(QtCore.QRect(x, y, xl, yl))
    font = QtGui.QFont()
    font.setPointSize(11)
    c_box.setFont(font)
    c_box.setStyleSheet("font-size: 50%;\n font-weight: 700;\n color: rgb(209, 209, 217);")
    c_box.setObjectName("comboBox")
    return c_box


def widget_plateg(group, x, y, xl, yl):
    widget_plat = QtWidgets.QWidget(group)
    widget_plat.setGeometry(QtCore.QRect(x, y, xl, yl))
    widget_plat.setObjectName("widget_plat")
    return widget_plat


def label_plateg(label_name, group, x, y, xl, yl):
    label_plat = QtWidgets.QLabel(label_name, group)
    label_plat.setGeometry(QtCore.QRect(x, y, xl, yl))
    font = QtGui.QFont()
    font.setPointSize(12)
    font.setBold(True)
    font.setWeight(87)
    label_plat.setFont(font)
    label_plat.setStyleSheet("font-weight: 700;\n color: rgb(209, 209, 217);\n padding: .0em;\n border: 0px solid;")
    label_plat.setObjectName("label_plat")
    return label_plat


def btn_check_plateg(group, x, y, xl, yl):
    btn_check = QtWidgets.QPushButton(group)
    btn_check.setGeometry(QtCore.QRect(x, y, xl, yl))
    btn_check.setStyleSheet("border: 0px solid;")
    icon = QtGui.QIcon()
    icon.addPixmap(QtGui.QPixmap("Resource/img/icon_checked_n.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    icon.addPixmap(QtGui.QPixmap("Resource/img/icon_checked_o.png"), QtGui.QIcon.Active, QtGui.QIcon.On)
    btn_check.setIcon(icon)
    btn_check.setIconSize(QtCore.QSize(30, 30))
    btn_check.setCheckable(True)
    btn_check.setObjectName("btn_check")
    return btn_check