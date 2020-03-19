# -*- coding: utf-8 -*-

import sqlite3  # создание и управление базой данных

# sqlite3_create_db, sqlite3_insert_tbl, sqlite3_read_db, sqlite3_read_sort, sqlite3_delete_table, \
# sqlite3_delete_record, sqlite3_update_record

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
# cols_name = 'id, Actual_PW, Actual_WA_1, Actual_WA_2, Actual_WA_3, Actual_WA_4, Actual_GZ'
# col_name = 'id'  # Имя колонки
# row_record = '2'  # Имя записи
# param_col = 'Actual_PW'
# param_val = 0
# sort_col = 'id'
# data_1 = [2, 'Февраль 2019', 815, 950, 291, 297, 216, 221, 134, 136, 171, 174, 990, 1000]
# data_2 = [3, 'Март 2019', 950, 0, 297, 0, 221, 0, 136, 0, 174, 0, 1000, 0]


# a = sqlite3_read_db(data_base, table)
# a = a[0]
#
#
# def chek_pokaz(a):
#     print(a)
#     for n in range(0, 11, 2):
#         for i in range(len(a) - 1):
#             if a[i + 1][n+2] != a[i][n+3]:
#                 print(a[i + 1][n+2], end=" ")
#                 print(a[i][n+3], end=" ")
#                 print('bad', end='\n')
#             # else:
#             #     print(a[i + 1][n+2], end=" ")
#             #     print(a[i][n+3], end=" ")
#             #     print('OK', end='\n')
#
#
# chek_pokaz(a)

# str(self.ui.comboBox_month.currentText())
# str(self.ui.comboBox_year.currentText())