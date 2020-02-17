# -*- coding: utf-8 -*-

import datetime
import sqlite3
import re

from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QDesktopWidget, QWidget

dt_day = datetime.datetime.now().strftime("%d")  # Текущий день (str "30")
dt_month = datetime.datetime.now().strftime("%m")  # Текущий месяц (str "01")
dt_year = datetime.datetime.now().strftime("%Y")  # Текущий год (str "2020")

month = ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь',
         'Декабрь']


def denominacia(year, cash):
    year_in = int(year)
    if year_in <= 2016:  # and self.comboBox_month_KP.currentIndex() + 1 < 6:
        den_cash = str(int(round(cash, 0)))
        den_cash = text_convert(den_cash)
    else:
        den_cash = str(round(cash, 2))
        den_cash = text_convert(den_cash)
    return den_cash


def clear_layout(layout):
    if layout is not None:
        while layout.count():
            child = layout.takeAt(0)
            if child.widget() is not None:
                child.widget().deleteLater()
            elif child.layout() is not None:
                clear_layout(child.layout())


def center(a):
    qr = a.geometry()
    cp = QDesktopWidget().availableGeometry().center()
    qr.moveCenter(cp)
    a.move(qr.topLeft())


def convert_month(input_month, a=1):  # Конвертирует текущий месяц из строки "01" в "Январь"
    out_month = int(input_month)  # "01" = 1
    for i in range(1, len(month) + 1):
        if i == out_month:
            out_month = month[i - a]
    return out_month  # "Январь"


def selected_period(combo_m, combo_y):
    combo_m.clear()
    combo_m.addItems(month)  # Выбор месяц в comboBox_month_KP

    combo_y.clear()
    for year_num in range(2006, 2025):  # Выбор года в comboBox_year_KP
        combo_y.addItem('%d' % year_num)


def text_convert(string):
    res = re.sub(r'\d(?=(?:\d{3})+(?!\d))', r'\g<0> ', string)
    return res


def data_convert(data):
    a = data[1]
    b = a.split()
    c = b[1]
    return c


def chek_pokaz(a):
    for n in range(0, 11, 2):
        for i in range(len(a) - 1):
            if a[i + 1][n + 2] != a[i][n + 3]:
                print(a[i + 1][1], a[i + 1][n + 2], end="\t ")
                print(a[i][1], a[i][n + 3], end="\t ")
                print('bad', end='\n')


# class SQLite3_Data_Base():
def sqlite3_create_db(data_base, table, heading):
    """метод для создания базы данных"""

    con = sqlite3.connect(data_base)  # соеденяемся с базой данных
    cur = con.cursor()  # создаем объект курсора

    # создаем таблицу в базе данных если таблицы не существует
    cur.execute('CREATE TABLE IF NOT EXISTS ' + table + '(' + heading + ')')

    con.commit()  # подтверждаем изменения
    cur.close()  # удаляем курсор
    con.close()  # разрываем соеденение с базой


def sqlite3_insert_tbl(data_base, table, data):
    """метод для создания записи в таблице"""

    con = sqlite3.connect(data_base)  # соеденяемся с базой данных
    cur = con.cursor()  # создаем объект курсора

    a = table
    b = '?, ' * (len(data) - 1) + '?'

    cur.execute('INSERT INTO ' + a + ' VALUES(' + b + ')', data)

    con.commit()  # подтверждаем изменения
    cur.close()  # удаляем курсор
    con.close()  # разрываем соеденение с базой


def sqlite3_read_db(data_base, table, col_name=None):
    """метод для чтения данных из таблицы (или колонок)"""

    con = sqlite3.connect(data_base)  # соеденяемся с базой данных
    cur = con.cursor()  # создаем объект курсора

    query_columns = 'pragma table_info(' + table + ')'
    cur.execute(query_columns)
    columns_description = cur.fetchall()
    columns_names = []

    for column in columns_description:
        columns_names.append(column[1])

    if col_name is None:
        query = 'SELECT * FROM ' + table
        cur.execute(query)
        data = cur.fetchall()

    else:
        query = 'SELECT ' + col_name + ' FROM ' + table
        cur.execute(query)
        data = cur.fetchall()
        new_data = []
        for element in data:
            new_data.append(element[0])
        data = new_data
        del new_data

    # print(columns_names)
    res = ()
    for line in data:
        res += (line, '')
    #     print(line)
    # print('Количество записей в таблице составляет: ' + str(len(data)))
    quantity = 'Количество записей в таблице составляет: ' + str(len(data))

    cur.close()  # удаляем курсор
    con.close()  # разрываем соеденение с базой

    return data, quantity


def sqlite3_read_sort(data_base, table, cols_name, sort_col):
    """метод для чтения из таблицы выбранной базы данных с сортировкой по имени колонки"""

    con = sqlite3.connect(data_base)  # соеденяемся с базой данных
    cur = con.cursor()  # создаем объект курсора

    # делаем запрос к базе данных
    query = 'SELECT ' + cols_name + ' FROM ' + table + ' ORDER BY ' + sort_col
    # print(query)
    cur.execute(query)
    data = cur.fetchall()  # помещаем считаные записи из запроса в переменную data

    cur.close()  # удаляем курсор
    con.close()  # разрываем соеденение с базой

    return data


def sqlite3_delete_table(data_base, table):
    """функция для удаления таблицы из базы данных по имени таблицы"""

    con = sqlite3.connect(data_base)  # соеденяемся с базой данных
    cur = con.cursor()  # создаем объект курсора

    query = 'DROP TABLE IF EXIST ' + table
    print(query)
    cur.execute(query)

    cur.close()  # удаляем курсор
    con.close()  # разрываем соеденение с базой


def sqlite3_delete_record(data_base, table, col_name, row_record):
    """функция для удаления записи в указанной таблице, указанной базы данных
    по названию колонки (id_column) и заначению ячейки (record_id) в указанной колонке"""

    con = sqlite3.connect(data_base)  # соеденяемся с базой данных
    cur = con.cursor()  # создаем объект курсора

    # создаем запрос на удаление записи по ключу record_id из колонки ключей id_column
    query = 'DELETE FROM ' + table + ' WHERE ' + col_name + ' = ' + "'" + row_record + "'"
    cur.execute(query)

    con.commit()  # подтверждаем изменения
    cur.close()  # удаляем курсор
    con.close()  # разрываем соеденение с базой


def sqlite3_update_record(data_base, table, col_name, row_record, param_col, param_val):
    """функция для обнавления значения/записи в указанной таблице, указанной базы данных
    в таблице (table) в записи ((col_name) колонка (row_record) запись) ROW заменить значение в (param_col) COL
    на значение (param_val)"""

    con = sqlite3.connect(data_base)  # соеденяемся с базой данных
    cur = con.cursor()  # создаем объект курсора

    # создаем запрос на обнавление значения/записи
    query = 'UPDATE ' + table + ' SET ' + param_col + ' = ' + str(param_val) + ' WHERE ' + col_name + ' = ' + \
            "'" + str(row_record) + "'"
    print(query)
    cur.execute(query)

    con.commit()  # подтверждаем изменения
    cur.close()  # удаляем курсор
    con.close()  # разрываем соеденение с базой


# data_base = 'Komunal.db'
# table = 'year_2018'
# heading = ('id integer primary key , month_year text, Pred_PW integer, Actual_PW integer, Pred_WA_1 integer, '
#                    'Actual_WA_1 integer, Pred_WA_2 integer, Actual_WA_2 integer, Pred_WA_3 integer, '
#                    'Actual_WA_3 integer, Pred_WA_4 integer, Actual_WA_4 integer, Pred_GZ integer, Actual_GZ integer')
#
# cols_name = 'id, Actual_PW, Actual_WA_1, Actual_WA_2, Actual_WA_3, Actual_WA_4, Actual_GZ'
# col_name = 'id'  # Имя колонки
# row_record = '2'  # Имя записи
# param_col = 'Actual_PW'
# param_val = 0
# sort_col = 'id'
# data_1 = [2, 'Февраль 2019', 815, 950, 291, 297, 216, 221, 134, 136, 171, 174, 990, 1000]
# data_2 = [3, 'Март 2019', 950, 0, 297, 0, 221, 0, 136, 0, 174, 0, 1000, 0]

# sqlite3_create_db(data_base, table, heading)
# sqlite3_insert_tbl(data_base, table, data_2)
# sqlite3_read_db(data_base, table)
# sqlite3_read_db(data_base, table, col_name)
# sqlite3_read_sort(data_base, table, cols_name, sort_col)
# sqlite3_delete_table(data_base, table)
# sqlite3_delete_record(data_base, table, col_name, row_record)
# sqlite3_insert_tbl(data_base, table, data)
# sqlite3_update_record(data_base, table, col_name, row_record, param_col, param_val)

# column(col) - колонка
# row(row) - ряд
# cell(cel) - ячейка
# heading - заголовок


class UiWinAdd(QWidget):  # метод создания ДОЛНИТЕЛЬНЫХ ПЛАТЕЖЕЙ
    def __init__(self):
        super().__init__()

        self.label = QtWidgets.QLabel("Имя платежа", self)
        self.lineEdit = QtWidgets.QLineEdit(self)
        self.btn_OK = QtWidgets.QPushButton("OK", self)
        self.btn_Cancel = QtWidgets.QPushButton("Cancel", self)

    def name_plateg(self):
        self.setObjectName("Form")
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.resize(290, 120)
        self.setStyleSheet("background-color: rgb(78, 79, 84);")
        self.setWindowTitle("Добовление платежа")

        self.label.setGeometry(QtCore.QRect(10, 5, 270, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setStyleSheet("font-weight: 700; \n color: rgb(209, 209, 217); \n padding: .1em; \n border: 1px;")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")

        self.lineEdit.setGeometry(QtCore.QRect(10, 40, 270, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("border-radius: 4px; \n color: rgb(209, 209, 217); \n "
                                    "border: 1px solid rgba(50, 50, 50, 240); \n "
                                    "background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, "
                                    "stop:0 rgba(125, 126, 131, 255), stop:0.01 rgba(108, 109, 114, 255), "
                                    "stop:0.99 rgba(91, 92, 96, 255), stop:1 rgba(125, 126, 131, 255));")
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setFocus()
        self.lineEdit.setObjectName("lineEdit")

        self.btn_OK.setGeometry(QtCore.QRect(30, 80, 110, 30))
        self.btn_OK.setAutoDefault(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHeightForWidth(self.btn_OK.sizePolicy().hasHeightForWidth())
        self.btn_OK.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_OK.setFont(font)
        self.btn_OK.setStyleSheet("font-weight: 700;\n color: rgb(209, 209, 217);\n padding: .5em 1em;")
        self.btn_OK.setObjectName("btn_OK")

        self.btn_Cancel.setGeometry(QtCore.QRect(150, 80, 110, 30))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHeightForWidth(self.btn_Cancel.sizePolicy().hasHeightForWidth())
        self.btn_Cancel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_Cancel.setFont(font)
        self.btn_Cancel.setStyleSheet("font-weight: 700;\n color: rgb(209, 209, 217);\n padding: .5em 1em;")
        self.btn_Cancel.setObjectName("btn_Cancel")

        self.show()
