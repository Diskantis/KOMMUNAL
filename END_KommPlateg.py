# -*- coding: utf-8 -*-

import sys
import win32api

from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QApplication

from UI_KommPlateg import UiWinPlateg
from Resource.FUN_KOMMUNAL import *
from Resource.END_CLASS_KOMM import Period
from Resource.UI_CLASS_KOMM import UiWinAdd, NewPlateg


# ОКНО КОММУНАЛЬНЫХ ПЛАТЕЖЕЙ
class KommunalPlateg(QtWidgets.QWidget, UiWinPlateg):
    def __init__(self):
        super(KommunalPlateg, self).__init__()

        self.setupUi_KP(self)

        self.win_h = 365
        self.frame_h = 0

        self.period_kp = Period(self.comboBox_month_KP, self.comboBox_year_KP, self.label_month_year_KP)

        current_month = convert_month(dt_month)  # Текущий месяц ("Январь")
        current_year = dt_year  # Текущий год ("2020")

        self.month_index = month.index(current_month)
        self.month_text = month[self.month_index]
        self.year_index = int(current_year)

        # ВЫБОР ПЕРИОДА
        combo_m = self.comboBox_month_KP
        combo_y = self.comboBox_year_KP
        selected_period(combo_m, combo_y)

        # установка ТЕКУЩЕГО ПЕРИОДА
        self.label_month_year_KP.setText(current_month + " " + current_year)  # устанавливает заголовок ("Январь 2020")
        self.comboBox_month_KP.setCurrentIndex(month.index(current_month))  # устанавливает текущий месяц ("Январь")
        self.comboBox_year_KP.setCurrentText(current_year)  # устанавливает текущий год ("2020")

        # ВЫБИРАЕМ период
        self.comboBox_month_KP.activated.connect(self.label_period)
        self.comboBox_year_KP.activated.connect(self.label_period)

        self.btn_Left_KP.clicked.connect(self.btn_period_left)
        self.btn_Right_KP.clicked.connect(self.btn_period_right)

        # режим РЕДАКТИРОВАНИЯ значений
        self.checkBox_Edit_KP.setChecked(False)
        self.checkBox_Edit_KP.stateChanged.connect(self.read_only)

        # ДОБАВЛЕНИЕ ПЛАТЕЖА
        self.pushButton_add_Plateg_KP.clicked.connect(self.btn_add_plateg)

        # СОХРАНЯЕМ показания
        self.pushButton_Save_KP.clicked.connect(self.btn_save_kp)

        # ЗАКРЫВАЕТ окно ПЛАТЕЖИ
        self.pushButton_Cancel_KP.clicked.connect(self.btn_cancel_kp)

        # ЧИТАЕТ платежи из базы данных
        self.read_kommunal_plateg()

        self.show()

    # показывает в заголовке выбранный месяц и год
    def label_period(self):
        self.month_index = self.period_kp.label_sel_period()
        self.read_kommunal_plateg()

    # прокрутка переиода в лево
    def btn_period_left(self):
        self.month_index = self.period_kp.click_btn_left(self.month_index)
        self.read_kommunal_plateg()

    # прокрутка переиода в право
    def btn_period_right(self):
        self.month_index = self.period_kp.click_btn_right(self.month_index)
        self.read_kommunal_plateg()

    # значения по умолчанию
    def default_win(self, y=0):
        self.WinPlateg.resize(800, 365)
        self.WinPlateg.setMinimumSize(QtCore.QSize(800, 365 + y))
        self.frame_plategi_KP.setGeometry(QtCore.QRect(20, 225, 760, 0 + y))

    # открывает окно "добавление нового платежа"
    def btn_add_plateg(self):
        self.win_add = UiWinAdd()
        self.win_add.name_plateg()

        if win32api.GetKeyboardLayout() == 67699721:  # 67699721 - английский 00000409
            win32api.LoadKeyboardLayout("00000419", 1)  # 68748313 - русский    00000419

        # КНОПКИ окна ДОБАВЛЕНИЕ ПЛАТЕЖА
        self.win_add.btn_OK.clicked.connect(self.win_add_name_ok)  # кнопка OK окна ИМЯ
        self.win_add.btn_OK.setAutoDefault(True)
        self.win_add.lineEdit.returnPressed.connect(self.win_add.btn_OK.click)

        self.win_add.btn_Cancel.clicked.connect(self.win_add_name_cancel)  # кнопка CANCEL

    # кнопка OK окна "ИМЯ нового платежа"
    def win_add_name_ok(self):
        self.name = self.win_add.lineEdit.text()

        self.win_add.lineEdit.clear()
        self.win_add.close()

        self.summ_plat = UiWinAdd()
        self.summ_plat.name_plateg()
        self.summ_plat.label.setText("Сумма платежа")

        if win32api.GetKeyboardLayout() == 68748313:  # 67699721 - английский 00000409
            win32api.LoadKeyboardLayout("00000409", 1)  # 68748313 - русский    00000419

        self.summ_plat.btn_OK.clicked.connect(self.win_add_summ_ok)  # кнопка OK окна СУММА
        self.summ_plat.btn_OK.setAutoDefault(True)
        self.summ_plat.lineEdit.returnPressed.connect(self.summ_plat.btn_OK.click)

        self.summ_plat.btn_Cancel.clicked.connect(self.win_add_summ_cancel)

    # кнопка OK окна "СУММА нового платежа"
    def win_add_summ_ok(self):
        self.sum = self.summ_plat.lineEdit.text()
        self.sum_text = text_convert(self.sum)

        self.create_plat(self.name, self.sum_text)

        # возможно удаление после того как был создан доп. плат.
        self.new_p.btn_del_Plat.clicked.connect(self.new_p.deleteLater)
        self.new_p.btn_del_Plat.clicked.connect(self.btn_del_plateg)

        self.summ_plat.lineEdit.clear()
        self.summ_plat.close()

    def create_plat(self, name, summ):
        self.new_p = NewPlateg(name, summ)
        self.gridLayout.addWidget(self.new_p)

        self.frame_h += 35
        self.win_h += 35

        self.WinPlateg.setMinimumSize(QtCore.QSize(800, self.win_h))
        self.frame_plategi_KP.setGeometry(QtCore.QRect(20, 225, 760, self.frame_h))

        self.dop_plategi[self.name] = float(self.sum), 0, 0
        self.dict_pole[self.name] = float(self.sum)
        self.plategi_sum += float(self.sum)
        self.itog_sum(self.plategi_sum)

    def btn_del_plateg(self):
        self.frame_h -= 35
        self.win_h -= 35
        self.win_h_del = self.win_h - 35

        self.WinPlateg.setMinimumSize(QtCore.QSize(800, self.win_h))
        self.frame_plategi_KP.setGeometry(QtCore.QRect(20, 225, 760, self.frame_h))
        self.WinPlateg.resize(800, self.win_h_del)

        # self.widget_Plat.close()
        # self.plategi_sum -= float(self.sum)
        # if self.plategi_sum <= 0:
        #     self.lineEdit_IS_sum.clear()
        # self.itog_sum(self.plategi_sum)

    # кнопка CANCEL окна "ИМЯ нового платежа"
    def win_add_name_cancel(self):
        self.win_add.lineEdit.clear()
        self.win_add.close()

    # кнопка CANCEL окна "СУММА нового платежа"
    def win_add_summ_cancel(self):
        self.summ_plat.lineEdit.clear()
        self.summ_plat.close()

    # читаем сохраненые данные из базы данных
    def read_kommunal_plateg(self):  # читаем данные из базы данных
        self.win_resize_y = 35
        self.position = 1

        self.default_win()
        self.checkBox_Edit_KP.setChecked(False)

        # очищаем поля окна ПЛАТЕЖИ
        self.dict_pole = {'Электричество': [self.lineEdit_sum_Power, self.lineEdit_kol_Power, self.lineEdit_trf_Power],
                          'Вода': [self.lineEdit_sum_Water, self.lineEdit_kol_Water, self.lineEdit_trf_Water],
                          'Газ': [self.lineEdit_sum_Gaz, self.lineEdit_kol_Gaz, self.lineEdit_trf_Gaz]}

        self.list_pole_trf = [self.lineEdit_trf_Power, self.lineEdit_trf_Water, self.lineEdit_trf_Gaz,
                              self.label_ERROR_KP, self.label_OK_KP, self.lineEdit_IS_sum]

        for i in self.dict_pole.values():
            for j in i:
                j.clear()

        for i in self.list_pole_trf:
            i.clear()

        self.checkBox_Edit_KP.show()

        clear_layout(self.gridLayout)  # удаляем все доп. платежи

        file_db = open('Komunal.db', 'a')
        file_db.close()
        self.data_base = 'Komunal.db'
        table_pokaz = 'Pokazanya_year_' + str(self.comboBox_year_KP.currentText())
        table_plateg = 'Plategi_year_' + str(self.comboBox_year_KP.currentText())
        col_name = 'id'
        heading = 'id integer, month_year text, Plateg text, Sum integer, Kol integer, Trf integer'

        sqlite3_create_db(self.data_base, table_plateg, heading)  # создаем базу данных в случаи ее отсутствия

        # читаем таблицу ПОКАЗАНИЙ счетчиков из базы данных
        try:
            read_table_PS = sqlite3_read_db(self.data_base, table_pokaz)
            read_table_PS = read_table_PS[0]

            for i in range(len(read_table_PS)):
                if read_table_PS[i][0] == month.index(self.comboBox_month_KP.currentText()) + 1:
                    pred_pokaz = read_table_PS[i]

                    self.lineEdit_kol_Power.setText(str(pred_pokaz[14]))
                    self.lineEdit_kol_Water.setText(str(pred_pokaz[17]))
                    self.lineEdit_kol_Gaz.setText(str(pred_pokaz[18]))

        except sqlite3.OperationalError:
            self.checkBox_Edit_KP.show()

        # проверяем существует ли такая запись в таблице ПЛАТЕЖЕЙ, если ДА то помечаем галочкой
        if self.comboBox_month_KP.currentIndex() + 1 in sqlite3_read_db(self.data_base, table_plateg, col_name)[0]:
            self.label_OK_KP.setPixmap(QtGui.QPixmap("./Resource/img/Galochka.png"))

        self.dop_plategi = {}  # словарь всех ПЛАТЕЖЕЙ
        self.plategi_trf = {}  # словарь только значений тарифов

        year = self.comboBox_year_KP.currentText()  # "ГОД" нужен для функции denominacia

        # читаем таблицу ПЛАТЕЖЕЙ из базы данных (ищим значения тарифов)
        try:
            # если нет записи (только январь)
            if self.comboBox_month_KP.currentIndex() + 1 not in sqlite3_read_db(
                    self.data_base, table_plateg, "id")[0] and month[self.comboBox_month_KP.currentIndex()] == "Январь":
                # таблица из предыдущего года
                table_plateg_jan = 'Plategi_year_' + str(int(self.comboBox_year_KP.currentText()) - 1)
                read_table_last = sqlite3_read_db(self.data_base, table_plateg_jan)[0]
                for a in read_table_last:  # значения тарифов из декабрьской таблицы
                    if a[0] == self.comboBox_month_KP.currentIndex() + 12:
                        self.plategi_trf[a[2]] = a[5]
            # если нет записи (любой месяц кроме января)
            elif self.comboBox_month_KP.currentIndex() + 1 not in sqlite3_read_db(
                    self.data_base, table_plateg, "id")[0] and month[self.comboBox_month_KP.currentIndex()] != "Январь":
                # таблица из текущего года
                table_plateg = 'Plategi_year_' + str(self.comboBox_year_KP.currentText())
                read_table_last = sqlite3_read_db(self.data_base, table_plateg)[0]
                for a in read_table_last:  # значения тарифов предыдущего периода
                    if a[0] == self.comboBox_month_KP.currentIndex():
                        self.plategi_trf[a[2]] = a[5]
            else:  # если есть запись (любой месяц)
                # таблица из текущего года
                table_plateg = 'Plategi_year_' + str(self.comboBox_year_KP.currentText())
                read_table_last = sqlite3_read_db(self.data_base, table_plateg)[0]
                for a in read_table_last:  # значения тарифов сохраненного периода
                    if a[0] == self.comboBox_month_KP.currentIndex() + 1:
                        self.plategi_trf[a[2]] = a[5]

            # устанавливаем значения тарифов в поля окна
            for j, a in zip(self.plategi_trf.values(), self.list_pole_trf[:3]):
                a.setText(str(j))

            # вычисляем значения суммы для наших счетчиков согласно тарифов
            # и заносим эти значения в поля окна и в словарь платежей
            for p, v in self.dict_pole.items():
                pl_sum = float(v[1].text()) * float(v[2].text())  # вычисляем значения суммы
                list_pl = pl_sum, int(v[1].text()), float(v[2].text())
                self.dop_plategi[p] = list_pl  # заносим значения в словарь платежей
                den = denominacia(year, pl_sum)
                v[0].setText(den + " руб")  # заносим значения в поля окна

        except sqlite3.OperationalError:
            self.checkBox_Edit_KP.show()
        except ValueError:
            self.checkBox_Edit_KP.show()

        # читаем таблицу ПЛАТЕЖЕЙ из базы данных (имя и значение доп.платежа)
        read_table_KP = sqlite3_read_db(self.data_base, table_plateg)[0]

        for i in read_table_KP:  # имя и значения доп.платежа сохраненного периода
            year = self.comboBox_year_KP.currentText()

            if i[0] == self.comboBox_month_KP.currentIndex() + 1:
                self.dop_plategi[i[2]] = i[3]  # заносим в словарь

            try:
                if i[2] == 'Электричество':
                    self.lineEdit_trf_Power.setText(str(self.plategi_trf.get(i[2], "")))
                    self.sum_platega(self.dict_pole, i[2], year)
                elif i[2] == 'Вода':
                    self.lineEdit_trf_Water.setText(str(self.plategi_trf.get(i[2], "")))
                    self.sum_platega(self.dict_pole, i[2], year)
                elif i[2] == 'Газ':
                    self.lineEdit_trf_Gaz.setText(str(self.plategi_trf.get(i[2], "")))
                    self.sum_platega(self.dict_pole, i[2], year)

            except ValueError:
                self.checkBox_Edit_KP.show()

        self.plategi_sum = 0  # общая сумма всех платежей

        # вычисляем общую сумму всех платежей
        for i, j in self.dop_plategi.items():
            self.plategi_sum += float(j[0]) if type(j) == tuple else float(j)

            if i == 'Электричество':
                continue
            elif i == 'Вода':
                continue
            elif i == 'Газ':
                continue
            else:
                self.WinPlateg.setMinimumSize(QtCore.QSize(800, 365 + self.win_resize_y))
                self.frame_plategi_KP.setGeometry(QtCore.QRect(20, 225, 760, 0 + self.win_resize_y))
                summ = text_convert(str(float(j)))
                self.new_p = NewPlateg(i, summ)
                self.gridLayout.addWidget(self.new_p)

                # self.frame_plateg(i, self.position)
                self.dop_plategi[i] = (float(j), 0, 0)
                self.dict_pole[i] = self.new_p.lineEdit_sum_Plat
                self.new_p.lineEdit_sum_Plat.setText(text_convert(str(j)) + " руб")
                self.win_resize_y += 32
                self.position += 1

            self.new_p.lineEdit_sum_Plat.textEdited[str].connect(
                lambda: self.text_editing(self.new_p.lineEdit_sum_Plat))

        self.itog_sum(self.plategi_sum)

        self.btn_check_Power.clicked[bool].connect(check_plateg)
        self.btn_check_Water.clicked[bool].connect(check_plateg)
        self.btn_check_Gaz.clicked[bool].connect(check_plateg)

    # вычисляем итоговою сумму платежей
    def itog_sum(self, plategi_sum):
        if self.plategi_sum > 0:
            year = self.comboBox_year_KP.currentText()
            den = denominacia(year, cash=plategi_sum)
            self.lineEdit_IS_sum.setText(den + " руб")

    # функция вычисляет сумму платежа и заносит значение в поле сумма
    def sum_platega(self, pole, plat, year):
        v = pole.get(plat)
        pl_sum = float(v[1].text()) * float(v[2].text())
        list_pl = pl_sum, int(v[1].text()), float(v[2].text())
        self.dop_plategi[plat] = list_pl
        den = denominacia(year, pl_sum)
        v[0].setText(den + " руб")

    # включение режима редактирования
    def read_only(self):  # режим РЕДАКТИРОВАНИЯ значений
        if self.checkBox_Edit_KP.isChecked():
            self.lineEdit_trf_Power.setReadOnly(False)
            self.lineEdit_trf_Water.setReadOnly(False)
            self.lineEdit_trf_Gaz.setReadOnly(False)
        else:
            self.lineEdit_trf_Power.setReadOnly(True)
            self.lineEdit_trf_Water.setReadOnly(True)
            self.lineEdit_trf_Gaz.setReadOnly(True)

        self.lineEdit_trf_Power.textEdited[str].connect(lambda: self.text_editing(self.lineEdit_sum_Power))
        self.lineEdit_trf_Water.textEdited[str].connect(lambda: self.text_editing(self.lineEdit_sum_Water))
        self.lineEdit_trf_Gaz.textEdited[str].connect(lambda: self.text_editing(self.lineEdit_sum_Gaz))

    # режим редактирования
    def text_editing(self, lineEdit_sum):
        try:
            if win32api.GetKeyboardLayout() == 68748313:  # 67699721 - английский 00000409
                win32api.LoadKeyboardLayout("00000409", 1)  # 68748313 - русский    00000419

            self.label_ERROR_KP.clear()
            self.checkBox_Edit_KP.show()
            year = self.comboBox_year_KP.currentText()

            if lineEdit_sum == self.lineEdit_sum_Power:
                self.sum_platega(self.dict_pole, 'Электричество', year)
            elif lineEdit_sum == self.lineEdit_sum_Water:
                self.sum_platega(self.dict_pole, 'Вода', year)
            elif lineEdit_sum == self.lineEdit_sum_Gaz:
                self.sum_platega(self.dict_pole, 'Газ', year)
            elif lineEdit_sum == self.new_p.lineEdit_sum_Plat:
                v = self.dict_pole.get(self.new_p.label_Plat.text())
                pl_sum = float(v.text())
                list_pl = pl_sum, 0, 0
                self.dop_plategi[self.new_p.label_Plat.text()] = list_pl

                def ok():
                    den_ok = denominacia(year, pl_sum)
                    v.setText(den_ok + " руб")

                v.returnPressed.connect(ok)

            self.plategi_sum = 0

            for i, j in self.dop_plategi.items():
                self.plategi_sum += float(j[0]) if type(j) == tuple else float(j)

            self.itog_sum(self.plategi_sum)

        except ValueError:
            self.checkBox_Edit_KP.hide()
            self.label_ERROR_KP.setText('Должно быдь значение!')

    # подготовка данных к сохранению
    def create_list_plateg_kommun(self):
        data = []

        id_row = self.comboBox_month_KP.currentIndex() + 1
        select_period = self.comboBox_month_KP.currentText() + " " + self.comboBox_year_KP.currentText()

        for i, j in self.dop_plategi.items():
            data.append((id_row, select_period, i, *j))

        return data

    # кнопка сохранения данных
    def btn_save_kp(self):
        data = self.create_list_plateg_kommun()
        print(self.create_list_plateg_kommun())

        table = 'Plategi_year_' + data_convert(data[1])

        col_name = 'id'  # Имя колонки
        row_record = str(data[0][0])  # Имя записи
        a = sqlite3_read_db(self.data_base, table, col_name)[0]

        try:
            if int(row_record) in a:
                self.save_yes_or_not()
            else:
                for data_i in data:
                    pass
                    sqlite3_insert_tbl(self.data_base, table, data_i)

                self.read_kommunal_plateg()

            # if self.comboBox_month_KP.currentIndex() + 2 != 13:
            #     b = month[self.comboBox_month_KP.currentIndex() + 1]
            #     c = self.comboBox_year_KP.currentText()
            # else:
            #     b = month[self.comboBox_month_KP.currentIndex() - 11]
            #     c = str(int(self.comboBox_year_KP.currentText()) + 1)
            #
            # self.label_month_year_KP.setText(b + " " + c)  # устанавливает заголовок ("Месяц Год")
            # self.comboBox_month_KP.setCurrentIndex(month.index(b))  # устанавливает текущий месяц ("Месяц")
            # self.comboBox_year_KP.setCurrentText(c)  # устанавливает текущий год ("Год")

        except sqlite3.IntegrityError:
            self.checkBox_Edit_KP.hide()
            self.label_ERROR.setText('Такая запись уже существует!')

    # режим перезаписи сохраненных данных
    def save_yes_or_not(self):
        self.save_yn = UiWinAdd()
        self.save_yn.name_plateg()
        self.save_yn.setWindowTitle("Сохранение")
        self.save_yn.lineEdit.close()
        self.save_yn.label.setGeometry(QtCore.QRect(10, 0, 270, 70))
        self.save_yn.label.setText("Вы действительно хотите \n презаписать эту запись?")

        self.save_yn.btn_OK.clicked.connect(self.btn_ok_save_yn)
        self.save_yn.btn_OK.setAutoDefault(True)
        self.save_yn.btn_Cancel.clicked.connect(self.btn_cancel_save_yn)

    # перезапись сохраненных данных
    def btn_ok_save_yn(self):
        data = self.create_list_plateg_kommun()  # список данных для записи
        table = 'Plategi_year_' + data_convert(data[1])  # имя таблицы (период)
        col_name = 'id'  # имя колонки
        row_record = str(data[0][0])  # имя записи

        for data_i in data:
            pass
            sqlite3_delete_record(self.data_base, table, col_name, row_record)
            sqlite3_insert_tbl(self.data_base, table, data_i)

        self.read_kommunal_plateg()

        self.save_yn.close()

    # кнопка отмены перезаписи
    def btn_cancel_save_yn(self):
        self.save_yn.close()

    # кнопка закрытия окна "Коммунальные платежи"
    def btn_cancel_kp(self):
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    win_KP = KommunalPlateg()
    sys.exit(app.exec_())
