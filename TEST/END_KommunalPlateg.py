# -*- coding: utf-8 -*-

import sys

from PyQt5.QtWidgets import QApplication

from Resource.FUN_KOMMUNAL import *
from Resource.END_CLASS_KOMM import *
from Resource.UI_CLASS_KOMM import UiWinAdd

from TEST.UI_KommunalPlateg import UiWinPlateg


# ОКНО КОММУНАЛЬНЫХ ПЛАТЕЖЕЙ
class KommunalPlateg(QtWidgets.QWidget, UiWinPlateg):
    def __init__(self, parent=None):
        super(KommunalPlateg, self).__init__(parent)

        self.wa = UiWinAdd()

        self.setupUi_KP(self)

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

        self.btn_Left.clicked.connect(self.btn_period_left)
        self.btn_Right.clicked.connect(self.btn_period_right)

        # режим РЕДАКТИРОВАНИЯ значений
        self.checkBox_Edit_KP.setChecked(False)
        self.checkBox_Edit_KP.stateChanged.connect(self.read_only)

        # ДОБАВЛЕНИЕ ПЛАТЕЖА
        self.pushButton_add_Plateg_KP.clicked.connect(self.btn_add_plateg)

        # КНОПКИ окна ДОБАВЛЕНИЕ ПЛАТЕЖА
        self.wa.btn_OK.clicked.connect(self.btn_ok_wa_name)  # кнопка OK
        self.wa.btn_OK.setAutoDefault(True)  # click on <Enter>
        self.wa.lineEdit.returnPressed.connect(self.wa.btn_OK.click)

        self.wa.btn_Cancel.clicked.connect(self.btn_cancel_wa)  # кнопка CANCEL

        # СОХРАНЯЕМ показания
        self.pushButton_Save_KP.clicked.connect(self.btn_save_kp)

        # ЗАКРЫВАЕТ окно ПЛАТЕЖИ
        self.pushButton_Cancel_KP.clicked.connect(self.btn_cancel_kp)

        # ЧИТАЕТ платежи из базы данных
        self.read_kommunal_plateg()

        # self.show()

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
        self.WinPlateg.resize(800, 400)
        self.WinPlateg.setMinimumSize(QtCore.QSize(800, 365 + y))
        self.frame_plategi_KP.setGeometry(QtCore.QRect(20, 225, 760, 0 + y))

    # открывает окно "добавление нового платежа"
    def btn_add_plateg(self):
        self.wa.name_plateg()
        if win32api.GetKeyboardLayout() == 67699721:  # 67699721 - английский 00000409
            win32api.LoadKeyboardLayout("00000419", 1)  # 68748313 - русский    00000419

    # кнопка OK окна "имя нового платежа"
    def btn_ok_wa_name(self, ):
        self.name = self.wa.lineEdit.text()
        self.wa.lineEdit.clear()
        self.wa.close()

        self.sum_pl = UiWinAdd()
        self.sum_pl.label.setText("Сумма платежа")
        self.sum_pl.name_plateg()

        if win32api.GetKeyboardLayout() == 68748313:  # 67699721 - английский 00000409
            win32api.LoadKeyboardLayout("00000409", 1)  # 68748313 - русский    00000419

        if self.sum_pl.btn_OK.clicked.connect(lambda: self.btn_ok_sum_pl(self.win_resize_y, self.position)): pass
        self.sum_pl.btn_OK.setAutoDefault(True)
        self.sum_pl.lineEdit.returnPressed.connect(self.sum_pl.btn_OK.click)
        self.sum_pl.btn_Cancel.clicked.connect(self.btn_cancel_sum_pl)

    # кнопка OK окна "сумма нового платежа"
    def btn_ok_sum_pl(self, y, position):
        self.sum_pl.lineEdit.close()
        self.sum = self.sum_pl.lineEdit.text()
        self.frame_plateg(self.name, position)
        self.default_win(y)
        dop_pl = text_convert(self.sum)
        self.lineEdit_Pl_sum.setText(dop_pl + " руб")

        self.dop_plategi[self.name] = float(self.sum), 0, 0
        self.dict_pole[self.name] = self.lineEdit_Pl_sum
        self.plategi_sum += float(self.sum)
        self.itog_sum(self.plategi_sum)

        self.win_resize_y += 32
        self.position += 1

        self.sum_pl.lineEdit.clear()
        self.sum_pl.close()

        self.btn_Pl_pdf.clicked.connect(self.btn_del_plateg)

    def btn_del_plateg(self):
        self.widget_Plat.close()
        self.win_resize_y -= 32
        self.position -= 1

    # кнопка CANCEL окна "имя нового платежа"
    def btn_cancel_wa(self):
        self.wa.lineEdit.clear()
        self.wa.close()

    # кнопка CANCEL окна "сумма нового платежа"
    def btn_cancel_sum_pl(self):
        self.sum_pl.lineEdit.clear()
        self.sum_pl.close()

    # читаем сохраненые данные из базы данных
    def read_kommunal_plateg(self):  # читаем данные из базы данных
        self.win_resize_y = 35
        self.position = 1

        self.default_win()
        self.checkBox_Edit_KP.setChecked(False)

        # очищаем поля окна ПЛАТЕЖИ
        self.dict_pole = {'Электричество': [self.lineEdit_P_sum, self.lineEdit_P_kol, self.lineEdit_P_trf],
                          'Вода': [self.lineEdit_W_sum, self.lineEdit_W_kol, self.lineEdit_W_trf],
                          'Газ': [self.lineEdit_G_sum, self.lineEdit_G_kol, self.lineEdit_G_trf]}

        self.list_pole = [self.lineEdit_P_trf, self.lineEdit_W_trf, self.lineEdit_G_trf,
                          self.label_ERROR, self.label_OK_1, self.lineEdit_IS_sum]

        for i in self.dict_pole.values():
            for j in i:
                j.clear()

        for i in self.list_pole:
            i.clear()

        self.checkBox_Edit_KP.show()

        clear_layout(self.gridLayout)  # удаляем все доп. платежи

        file_db = open('../Komunal.db', 'a')
        file_db.close()
        data_base = 'Komunal.db'
        table_pokaz = 'Pokazanya_year_' + str(self.comboBox_year_KP.currentText())
        table_plateg = 'Plategi_year_' + str(self.comboBox_year_KP.currentText())
        col_name = 'id'
        heading = 'id integer, month_year text, Plateg text, Sum integer, Kol integer, Trf integer'

        sqlite3_create_db(data_base, table_plateg, heading)  # создаем базу данных в случаи ее отсутствия

        # читаем таблицу ПОКАЗАНИЙ счетчиков из базы данных
        try:
            read_table_PS = sqlite3_read_db(data_base, table_pokaz)
            read_table_PS = read_table_PS[0]

            for i in range(len(read_table_PS)):
                if read_table_PS[i][0] == month.index(self.comboBox_month_KP.currentText()) + 1:
                    pred_pokaz = read_table_PS[i]

                    self.lineEdit_P_kol.setText(str(pred_pokaz[14]))
                    self.lineEdit_W_kol.setText(str(pred_pokaz[17]))
                    self.lineEdit_G_kol.setText(str(pred_pokaz[18]))

        except sqlite3.OperationalError:
            self.checkBox_Edit_KP.show()

        # проверяем существует ли такая запись в таблице ПЛАТЕЖЕЙ, если ДА то помечаем галочкой
        if self.comboBox_month_KP.currentIndex() + 1 in sqlite3_read_db(data_base, table_plateg, col_name)[0]:
            self.label_OK_1.setPixmap(QtGui.QPixmap("./Resource/img/Galochka.png"))

        self.dop_plategi = {}  # словарь всех ПЛАТЕЖЕЙ
        self.plategi_trf = {}  # словарь только значений тарифов

        year = self.comboBox_year_KP.currentText()  # "ГОД" нужен для функции denominacia

        # читаем таблицу ПЛАТЕЖЕЙ из базы данных (ищим значения тарифов)
        try:
            # если нет записи (только январь)
            if self.comboBox_month_KP.currentIndex() + 1 not in sqlite3_read_db(data_base, table_plateg, "id")[0] and \
                    month[self.comboBox_month_KP.currentIndex()] == "Январь":
                # таблица из предыдущего года
                table_plateg_jan = 'Plategi_year_' + str(int(self.comboBox_year_KP.currentText()) - 1)
                read_table_last = sqlite3_read_db(data_base, table_plateg_jan)[0]
                for a in read_table_last:  # значения тарифов из декабрьской таблицы
                    if a[0] == self.comboBox_month_KP.currentIndex() + 12:
                        self.plategi_trf[a[2]] = a[5]
            # если нет записи (любой месяц кроме января)
            elif self.comboBox_month_KP.currentIndex() + 1 not in sqlite3_read_db(data_base, table_plateg, "id")[0] \
                    and month[self.comboBox_month_KP.currentIndex()] != "Январь":
                # таблица из текущего года
                table_plateg = 'Plategi_year_' + str(self.comboBox_year_KP.currentText())
                read_table_last = sqlite3_read_db(data_base, table_plateg)[0]
                for a in read_table_last:  # значения тарифов предыдущего периода
                    if a[0] == self.comboBox_month_KP.currentIndex():
                        self.plategi_trf[a[2]] = a[5]
            else:  # если есть запись (любой месяц)
                # таблица из текущего года
                table_plateg = 'Plategi_year_' + str(self.comboBox_year_KP.currentText())
                read_table_last = sqlite3_read_db(data_base, table_plateg)[0]
                for a in read_table_last:  # значения тарифов сохраненного периода
                    if a[0] == self.comboBox_month_KP.currentIndex() + 1:
                        self.plategi_trf[a[2]] = a[5]

            # устанавливаем значения тарифов в поля окна
            for j, a in zip(self.plategi_trf.values(), self.list_pole[:3]):
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
        read_table_KP = sqlite3_read_db(data_base, table_plateg)[0]

        for i in read_table_KP:  # имя и значения доп.платежа сохраненного периода
            year = self.comboBox_year_KP.currentText() #

            if i[0] == self.comboBox_month_KP.currentIndex() + 1:
                self.dop_plategi[i[2]] = i[3]  # заносим в словарь

            try: #
                if i[2] == 'Электричество':
                    self.lineEdit_P_trf.setText(str(self.plategi_trf.get(i[2], "")))
                    self.sum_platega(self.dict_pole, i[2], year)
                elif i[2] == 'Вода':
                    self.lineEdit_W_trf.setText(str(self.plategi_trf.get(i[2], "")))
                    self.sum_platega(self.dict_pole, i[2], year)
                elif i[2] == 'Газ':
                    self.lineEdit_G_trf.setText(str(self.plategi_trf.get(i[2], "")))
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
                self.frame_plateg(i, self.position)
                self.dop_plategi[i] = (float(j), 0, 0)
                self.dict_pole[i] = self.lineEdit_Pl_sum
                self.lineEdit_Pl_sum.setText(text_convert(str(j)) + " руб")
                self.win_resize_y += 32
                self.position += 1

            if self.lineEdit_Pl_sum.textEdited[str].connect(lambda: self.text_editing(self.lineEdit_Pl_sum)): pass

        self.itog_sum(self.plategi_sum)

    # def check_plateg(self, name_btn, status):
    #     icon = QtGui.QIcon()
    #     name_btn.setIcon(icon)
    #     if status == 1:
    #         icon.addPixmap(QtGui.QPixmap("Resource/img/icon_checked_o.png"), QtGui.QIcon.Active, QtGui.QIcon.On)
    #     else:
    #         icon.addPixmap(QtGui.QPixmap("Resource/img/icon_checked_n.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

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
            self.lineEdit_P_trf.setReadOnly(False)
            self.lineEdit_W_trf.setReadOnly(False)
            self.lineEdit_G_trf.setReadOnly(False)
        else:
            self.lineEdit_P_trf.setReadOnly(True)
            self.lineEdit_W_trf.setReadOnly(True)
            self.lineEdit_G_trf.setReadOnly(True)

        if self.lineEdit_P_trf.textEdited[str].connect(lambda: self.text_editing(self.lineEdit_P_sum)): pass
        if self.lineEdit_W_trf.textEdited[str].connect(lambda: self.text_editing(self.lineEdit_W_sum)): pass
        if self.lineEdit_G_trf.textEdited[str].connect(lambda: self.text_editing(self.lineEdit_G_sum)): pass

    # режим редактирования
    def text_editing(self, label):
        try:
            if win32api.GetKeyboardLayout() == 68748313:  # 67699721 - английский 00000409
                win32api.LoadKeyboardLayout("00000409", 1)  # 68748313 - русский    00000419

            self.label_ERROR.clear()
            self.checkBox_Edit_KP.show()
            year = self.comboBox_year_KP.currentText()

            if label == self.lineEdit_P_sum:
                self.sum_platega(self.dict_pole, 'Электричество', year)
            elif label == self.lineEdit_W_sum:
                self.sum_platega(self.dict_pole, 'Вода', year)
            elif label == self.lineEdit_G_sum:
                self.sum_platega(self.dict_pole, 'Газ', year)
            elif label == self.lineEdit_Pl_sum:
                v = self.dict_pole.get(self.label_Plat.text())
                pl_sum = float(v.text())
                list_pl = pl_sum, 0, 0
                self.dop_plategi[self.label_Plat.text()] = list_pl

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
            self.label_ERROR.setText('Должно быдь значение!')

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
        data_base = 'Komunal.db'
        data = self.create_list_plateg_kommun()
        table = 'Plategi_year_' + data_convert(data[1])

        col_name = 'id'  # Имя колонки
        row_record = str(data[0][0])  # Имя записи
        a = sqlite3_read_db(data_base, table, col_name)[0]

        try:
            if int(row_record) in a:
                self.save_yes_or_not()
            else:
                for data_i in data:
                    pass
                    # sqlite3_insert_tbl(data_base, table, data_i)

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
        data_base = 'Komunal.db'  # имя базы данных
        data = self.create_list_plateg_kommun()  # список данных для записи
        table = 'Plategi_year_' + data_convert(data[1])  # имя таблицы (период)
        col_name = 'id'  # имя колонки
        row_record = str(data[0][0])  # имя записи

        for data_i in data:
            pass
            # sqlite3_delete_record(data_base, table, col_name, row_record)
            # sqlite3_insert_tbl(data_base, table, data_i)

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
