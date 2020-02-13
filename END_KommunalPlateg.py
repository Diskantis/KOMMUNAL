# -*- coding: utf-8 -*-

import sys
import win32api

from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QApplication

from FUN_KOMMUNAL import *
from UI_KommunalPlateg import UiWinPlateg, UiWinAdd


# ОКНО КОММУНАЛЬНЫХ ПЛАТЕЖЕЙ
class KommunalPlateg(QtWidgets.QWidget, UiWinPlateg):
    def __init__(self, parent=None):
        super(KommunalPlateg, self).__init__(parent)

        self.wa = UiWinAdd()

        self.name = ""
        self.sum = ""

        self.setupUi_KP(self)
        center(self.WinPlateg)

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
        self.comboBox_month_KP.activated.connect(self.label_sel_period)
        self.comboBox_year_KP.activated.connect(self.label_sel_period)

        self.btn_Left.clicked.connect(self.click_btn_left)
        self.btn_Right.clicked.connect(self.click_btn_right)

        # режим РЕДАКТИРОВАНИЯ значений
        self.checkBox_Edit_KP.setChecked(False)
        self.checkBox_Edit_KP.stateChanged.connect(self.read_only)

        # ДОБАВЛЕНИЕ ПЛАТЕЖА
        self.pushButton_add_Plateg_KP.clicked.connect(self.btn_add_plateg)

        # КНОПКИ окна ДОБАВЛЕНИЕ ПЛАТЕЖА
        if self.wa.btn_OK.clicked.connect(lambda: self.btn_ok_wa_name(self.win_resize_y, self.position)):
            pass    # кнопка OK
        self.wa.btn_OK.setAutoDefault(True)  # click on <Enter>
        self.wa.lineEdit.returnPressed.connect(self.wa.btn_OK.click)

        self.wa.btn_Cancel.clicked.connect(self.btn_cancel_wa)  # кнопка CANCEL

        # СОХРАНЯЕМ показания
        self.pushButton_Save_KP.clicked.connect(self.btn_save_kp)

        # ЗАКРЫВАЕТ окно ПОКАЗАНИЙ
        self.pushButton_Cancel_KP.clicked.connect(self.btn_cancel_kp)

        # ЧИТАЕТ платежи из базы данных
        self.read_kommunal_plateg()

        # self.show()

    def default_win(self, y=0):
        self.WinPlateg.resize(800, 400)
        self.WinPlateg.setMinimumSize(QtCore.QSize(800, 365 + y))
        center(self.WinPlateg)
        self.frame_plategi_KP.setGeometry(QtCore.QRect(20, 225, 760, 0 + y))

    def label_sel_period(self):  # показывает в заголовке выбранный месяц и год
        m_sel = self.comboBox_month_KP.currentText()  # выбранный в comboBox месяц
        y_sel = self.comboBox_year_KP.currentText()  # выбранный в comboBox год
        self.label_month_year_KP.setText(m_sel + " " + y_sel)  # заголовок ("Январь 2020")
        self.month_index = month.index(m_sel)

        self.read_kommunal_plateg()

    def click_btn_left(self):  # прокрутка переиода в лево
        if self.month_index > 0:
            self.month_index = self.comboBox_month_KP.currentIndex() - 1
            select_mount = month[self.month_index]
            self.comboBox_month_KP.setCurrentText(select_mount)
            self.year_index = str(self.comboBox_year_KP.currentText())
            self.label_month_year_KP.setText(select_mount + " " + self.year_index)
        else:
            self.month_index = 11
            select_mount = month[self.month_index]
            self.comboBox_month_KP.setCurrentText(select_mount)
            self.year_index = str(int(self.comboBox_year_KP.currentText()) - 1)
            self.comboBox_year_KP.setCurrentText(self.year_index)
            self.label_month_year_KP.setText(select_mount + " " + self.year_index)

        self.default_win()
        self.read_kommunal_plateg()

    def click_btn_right(self):  # прокрутка переиода в право
        if self.month_index < 11:
            self.month_index = self.comboBox_month_KP.currentIndex() + 1
            select_mount = month[self.month_index]
            self.comboBox_month_KP.setCurrentText(select_mount)
            self.year_index = str(self.comboBox_year_KP.currentText())
            self.label_month_year_KP.setText(select_mount + " " + self.year_index)
        else:
            self.month_index = 0
            select_mount = month[self.month_index]
            self.comboBox_month_KP.setCurrentText(select_mount)
            self.year_index = str(int(self.comboBox_year_KP.currentText()) + 1)
            self.comboBox_year_KP.setCurrentText(self.year_index)
            self.label_month_year_KP.setText(select_mount + " " + self.year_index)

        self.default_win()
        self.read_kommunal_plateg()

    def btn_add_plateg(self):
        self.wa.name_plateg()
        if win32api.GetKeyboardLayout() == 67699721:    # 67699721 - английский 00000409
            win32api.LoadKeyboardLayout("00000419", 1)  # 68748313 - русский    00000419

    def btn_ok_wa_name(self, y, position):
        self.name = self.wa.lineEdit.text()
        self.frame_plateg(self.name, position)
        self.wa.lineEdit.clear()
        self.wa.close()
        self.default_win(y)

        self.sum_pl = UiWinAdd()
        self.sum_pl.label.setText("Сумма платежа")
        self.sum_pl.name_plateg()

        if win32api.GetKeyboardLayout() == 68748313:    # 67699721 - английский 00000409
            win32api.LoadKeyboardLayout("00000409", 1)  # 68748313 - русский    00000419

        self.sum_pl.btn_OK.clicked.connect(self.btn_ok_sum_pl)
        self.sum_pl.btn_OK.setAutoDefault(True)
        self.sum_pl.lineEdit.returnPressed.connect(self.sum_pl.btn_OK.click)
        self.sum_pl.btn_Cancel.clicked.connect(self.btn_cancel_sum_pl)

    def btn_ok_sum_pl(self):
        self.sum = self.sum_pl.lineEdit.text()
        self.lineEdit_Pl_sum.setText(self.sum)

        self.list_plat.append(self.name)
        self.list_sum.append(self.sum)

        self.win_resize_y += 32
        self.position += 1

        self.sum_pl.lineEdit.clear()
        self.sum_pl.close()

    def btn_cancel_sum_pl(self):
        self.sum_pl.close()

    def btn_cancel_wa(self):
        self.wa.close()

    def read_kommunal_plateg(self):  # читаем данные из базы данных
        self.win_resize_y = 32
        self.position = 1
        self.plategi_sum = 0
        self.list_plat = []
        self.list_sum = []

        file_db = open('Komunal.db', 'a')
        file_db.close()
        data_base = 'Komunal.db'
        table_pokaz = 'Pokazanya_year_' + str(self.comboBox_year_KP.currentText())
        table_plateg = 'Plategi_year_' + str(self.comboBox_year_KP.currentText())
        heading = 'id integer, month_year text, Plateg text, Sum integer, Kol integer, Trf integer'

        sqlite3_create_db(data_base, table_plateg, heading)

        self.default_win()
        clear_layout(self.gridLayout)

        # очищаем ячейки окна
        a = [self.lineEdit_P_sum, self.lineEdit_P_kol, self.lineEdit_P_trf,
             self.lineEdit_W_sum, self.lineEdit_W_kol, self.lineEdit_W_trf,
             self.lineEdit_G_sum, self.lineEdit_G_kol, self.lineEdit_G_trf, self.label_ERROR, self.lineEdit_IS_sum]
        for i in a:
            i.clear()

        # читаем таблицу ПОКАЗАНИЙ счетчиков из базе данных
        read_table_PS = sqlite3_read_db(data_base, table_pokaz)
        read_table_PS = read_table_PS[0]

        for i in range(len(read_table_PS)):
            if read_table_PS[i][0] == month.index(self.comboBox_month_KP.currentText()) + 1:

                pred_pokaz = read_table_PS[i]

                self.lineEdit_P_kol.setText(str(pred_pokaz[14]))
                self.lineEdit_W_kol.setText(str(pred_pokaz[17]))
                self.lineEdit_G_kol.setText(str(pred_pokaz[18]))

        # читаем таблицу ПЛАТЕЖЕЙ из базе данных
        read_table_KP = sqlite3_read_db(data_base, table_plateg)
        read_table_KP = read_table_KP[0]

        for i in read_table_KP:
            year = self.comboBox_year_KP.currentText()
            if i[0] == self.comboBox_month_KP.currentIndex() + 1:
                self.list_plat.append(i[2])
                self.list_sum.append(i[3])
        #         if i[2] == 'Электричество':
        #             self.lineEdit_P_trf.setText(str(i[5]))
        #             pl_sum = float(self.lineEdit_P_kol.text()) * float(self.lineEdit_P_trf.text())
        #             self.plategi_sum += float(pl_sum)
        #             den = denominacia(year, pl_sum)
        #             self.lineEdit_P_sum.setText(den + " руб")
        #         elif i[2] == 'Вода':
        #             self.lineEdit_W_trf.setText(str(i[5]))
        #             pl_sum = float(self.lineEdit_W_kol.text()) * float(self.lineEdit_W_trf.text())
        #             self.plategi_sum += float(pl_sum)
        #             den = denominacia(year, pl_sum)
        #             self.lineEdit_W_sum.setText(den + " руб")
        #         elif i[2] == 'Газ':
        #             self.lineEdit_G_trf.setText(str(i[5]))
        #             pl_sum = float(self.lineEdit_G_kol.text()) * float(self.lineEdit_G_trf.text())
        #             self.plategi_sum += float(pl_sum)
        #             den = denominacia(year, pl_sum)
        #             self.lineEdit_G_sum.setText(den + " руб")
        #
                if i[5] != 0:
                    self.label_OK_1.setPixmap(QtGui.QPixmap("./Resource/img/Galochka.png"))
        #
        for i in range(len(self.list_plat)):
            if i > 2:
                self.WinPlateg.resize(800, 365 + self.win_resize_y)
                center(self.WinPlateg)
                self.frame_plategi_KP.setGeometry(QtCore.QRect(20, 225, 760, 0 + self.win_resize_y))
                self.frame_plateg(self.list_plat[i], self.position)
                self.plategi_sum += float(self.list_sum[i])
                self.lineEdit_Pl_sum.setText(text_convert(str(self.list_sum[i])) + " руб")
                self.win_resize_y += 32
                self.position += 1
        #
        # if self.plategi_sum > 0:
        #     year = self.comboBox_year_KP.currentText()
        #     den = denominacia(year, cash=self.plategi_sum)
        #     self.lineEdit_IS_sum.setText(den + " руб")

        print(self.list_plat)
        print(self.list_sum)

    def read_only(self):  # режим РЕДАКТИРОВАНИЯ значений
        if self.checkBox_Edit_KP.isChecked():
            self.lineEdit_P_trf.setReadOnly(False)
            self.lineEdit_W_trf.setReadOnly(False)
            self.lineEdit_G_trf.setReadOnly(False)
        else:
            self.lineEdit_P_trf.setReadOnly(True)
            self.lineEdit_W_trf.setReadOnly(True)
            self.lineEdit_G_trf.setReadOnly(True)

        if self.lineEdit_P_trf.textEdited[str].connect(lambda: self.text_label_1(self.lineEdit_P_sum)): pass  # ЭЛЕКТРО
        if self.lineEdit_W_trf.textEdited[str].connect(lambda: self.text_label_1(self.lineEdit_W_sum)): pass  # ВОДА
        if self.lineEdit_G_trf.textEdited[str].connect(lambda: self.text_label_1(self.lineEdit_G_sum)): pass  # ГАЗ

    def text_label_1(self, label):
        try:
            self.label_ERROR.clear()
            self.checkBox_Edit_KP.show()
            plateg_sum = 0
            if label == self.lineEdit_P_sum:
                a = float(self.lineEdit_P_kol.text()) * float(self.lineEdit_P_trf.text())
                den = text_convert(str(round(a, 2)))  # округляет число и разбивает число на разряды
                label.setText(den + " руб")
                plateg_sum = a
            elif label == self.lineEdit_W_sum:
                a = float(int(self.lineEdit_W_kol.displayText()) * float(self.lineEdit_W_trf.text()))
                den = text_convert(str(round(a, 2)))  # округляет число и разбивает число на разряды
                label.setText(den + " руб")
                plateg_sum = a
            elif label == self.lineEdit_G_sum:
                a = float(int(self.lineEdit_G_kol.displayText()) * float(self.lineEdit_G_trf.text()))
                den = text_convert(str(round(a, 2)))  # округляет число и разбивает число на разряды
                label.setText(den + " руб")
                plateg_sum = a
            return plateg_sum
        except ValueError:
            self.checkBox_Edit_KP.hide()
            self.label_ERROR.setText('Должно быдь значение!')

    # def create_list_plateg_kommun(self):
    #     ppw = self.lineEdit_pokaz_P1.text()  # ПРЕДЫДУЩИЕ значение ЭЛЕКТРИЧЕСТВО
    #     apw = self.lineEdit_P1.text()  # ПОСЛЕДНЕЕ значение ЭЛЕКТРИЧЕСТВО
    #     pwa_1 = self.lineEdit_pokaz_W1.text()  # ПРЕДЫДУЩИЕ значение ВОДА № 1
    #     awa_1 = self.lineEdit_W1.text()  # ПОСЛЕДНЕЕ значение ВОДА № 1
    #     pwa_2 = self.lineEdit_pokaz_W2.text()  # ПРЕДЫДУЩИЕ значение ВОДА № 2
    #     awa_2 = self.lineEdit_W2.text()  # ПОСЛЕДНЕЕ значение ВОДА № 2
    #     pwa_3 = self.lineEdit_pokaz_W3.text()  # ПРЕДЫДУЩИЕ значение ВОДА № 3
    #     awa_3 = self.lineEdit_W3.text()  # ПОСЛЕДНЕЕ значение ВОДА № 3
    #     pwa_4 = self.lineEdit_pokaz_W4.text()  # ПРЕДЫДУЩИЕ значение ВОДА № 4
    #     awa_4 = self.lineEdit_W4.text()  # ПОСЛЕДНЕЕ значение ВОДА № 4
    #     pgz = self.lineEdit_pokaz_G1.text()  # ПРЕДЫДУЩИЕ значение ГАЗ
    #     agz = self.lineEdit_G1.text()  # ПОСЛЕДНЕЕ значение ГАЗ
    #
    #     pow_mount_ras = self.label_PM_2.text()  # МЕСЯЧНЫЙ расход ЭЛЕКТРИЧЕСТВО
    #     w_cold_mount_ras = self.label_WM_2.text()  # МЕСЯЧНЫЙ расход ХОЛОДНАЯ ВОДА
    #     w_hot_mount_ras = self.label_WM_4.text()  # МЕСЯЧНЫЙ расход ГОРЯЧАЯ ВОДА
    #     w_mount_ras = self.label_WM_6.text()  # МЕСЯЧНЫЙ расход ВСЕГО ВОДА
    #     gaz_mount_ras = self.label_GM_2.text()  # МЕСЯЧНЫЙ расход ГАЗ
    #
    #     # СОЗДАЕМ СПИСОК ПОКАЗАНИЙ ЗА МЕСЯЦ
    #     # номер месяца ("Январь" = 1)
    #     id_row = month.index(self.comboBox_month_PS.currentText()) + 1
    #     # название периода ("Январь 2020")
    #     select_period = self.comboBox_month_PS.currentText() + " " + self.comboBox_year_PS.currentText()
    #     # список данных счетчиков предыдущие и последние
    #     data = [id_row, select_period, ppw, apw, pwa_1, awa_1, pwa_2, awa_2, pwa_3, awa_3,
    #             pwa_4, awa_4, pgz, agz, pow_mount_ras, w_cold_mount_ras, w_hot_mount_ras, w_mount_ras, gaz_mount_ras]
    #
    #     return data

    def create_list_plateg_kommun(self):

        # print(self.list_plat, self.list_sum, self.plategi_sum, sep='\n')

        # psum = float(self.wp.lineEdit_P_sum.text())
        # pkol = self.lineEdit_P_kol.text()
        # ptrf = self.lineEdit_P_trf.text()
        # wsum = float(self.wp.lineEdit_W_sum.text())
        # wkol = self.lineEdit_W_kol.text()
        # wtrf = self.lineEdit_W_trf.text()
        # gsum = float(self.wp.lineEdit_G_sum.text())
        # gkol = self.lineEdit_G_kol.text()
        # gtrf = self.lineEdit_G_trf.text()

        # c.setText(str(pred_pokaz[d]))
        data = []

        id_row = self.comboBox_month_KP.currentIndex() + 1
        select_period = self.comboBox_month_KP.currentText() + " " + self.comboBox_year_KP.currentText()
        for c, d in zip(self.list_plat, self.list_sum):
            data += [(id_row, select_period, c, d, 0, 0)]

        # data_1_Water = [id_row, select_period, self.label_Water.text(), wsum, wkol, wtrf]
        # data_1_Gaz = [id_row, select_period, self.label_Gaz.text(), gsum, gkol, gtrf]
        # data_1_Kvar = [id_row, select_period_1, self.wp.label_Kvar.text(), ksum, 0, 0]
        # data_1_Tel = [id_row, select_period_1, self.wp.label_Tel.text(), tsum, 0, 0]
        # data_1_Inet = [id_row, select_period_1, self.wp.label_Inet.text(), isum, 0, 0]
        # data_1_DSad = [id_row, select_period_1, self.wp.label_DSad.text(), dsum, 0, 0]
        #
        # if id_row != 12:
        #     select_period_2 = td_month(id_row, 0) + " " + str(self.wp.comboBox_year_KP.currentText())
        #     data_2_Power = [id_row + 1, select_period_2, self.wp.label_Power.text(), 0, 0, ptrf]
        #     data_2_Water = [id_row + 1, select_period_2, self.wp.label_Water.text(), 0, 0, wtrf]
        #     data_2_Gaz = [id_row + 1, select_period_2, self.wp.label_Gaz.text(), 0, 0, gtrf]
        #     # data_2_Kvar = [id_row + 1, select_period_2, self.ui.label_Kvar.text(), 0, 0, 0]
        #     # data_2_Tel = [id_row + 1, select_period_2, self.ui.label_Tel.text(), 0, 0, 0]
        #     # data_2_Inet = [id_row + 1, select_period_2, self.ui.label_Inet.text(), 0, 0, 0]
        #     # data_2_DSad = [id_row + 1, select_period_2, self.ui.label_DSad.text(), 0, 0, 0]
        # else:
        #     select_period_2 = td_month(id_row, 12) + " " + str(int(self.wp.comboBox_year_KP.currentText()) + 1)
        #     data_2_Power = [id_row - 11, select_period_2, self.wp.label_Power.text(), 0, 0, ptrf]
        #     data_2_Water = [id_row - 11, select_period_2, self.wp.label_Water.text(), 0, 0, wtrf]
        #     data_2_Gaz = [id_row - 11, select_period_2, self.wp.label_Gaz.text(), 0, 0, gtrf]
        #     # data_2_Kvar = [id_row - 11, select_period_2, self.ui.label_Kvar.text(), 0, 0, 0]
        #     # data_2_Tel = [id_row - 11, select_period_2, self.ui.label_Tel.text(), 0, 0, 0]
        #     # data_2_Inet = [id_row - 11, select_period_2, self.ui.label_Inet.text(), 0, 0, 0]
        #     # data_2_DSad = [id_row - 11, select_period_2, self.ui.label_DSad.text(), 0, 0, 0]
        #
        return data
        # data_1_Power, data_1_Water, data_1_Gaz, data_2_Power, data_2_Water, data_2_Gaz
        # data_1_Kvar, data_1_Tel, data_1_Inet, data_1_DSad, data_2_Kvar, data_2_Tel, data_2_Inet, data_2_DSad

    def btn_save_kp(self):
        pass
        # print(self.create_list_plateg_kommun())

        # data_base = 'Komunal.db'
        # data = self.create_list_plateg_kommun()
        # table = 'Plategi_year_' + data_convert(data)
        #
        # try:
        #     sqlite3_insert_tbl(data_base, table, data)

            # if self.comboBox_month_PS.currentIndex() + 2 != 13:
            #     b = month[self.comboBox_month_PS.currentIndex() + 1]
            #     c = self.comboBox_year_PS.currentText()
            # else:
            #     b = month[self.comboBox_month_PS.currentIndex() - 11]
            #     c = str(int(self.comboBox_year_PS.currentText()) + 1)
            #
            # self.label_month_year_PS.setText(b + " " + c)  # устанавливает заголовок ("Месяц Год")
            # self.comboBox_month_PS.setCurrentIndex(month.index(b))  # устанавливает текущий месяц ("Месяц")
            # self.comboBox_year_PS.setCurrentText(c)  # устанавливает текущий год ("Год")

            # self.read_pokaz_schet()
        #
        # except sqlite3.IntegrityError:
        #     self.checkBox_Edit_KP.hide()
        #     self.label_ERROR.setText('Такая запись уже существует!')

    # def btn_save_kp(self):
    #     data_1_Power, data_1_Water, data_1_Gaz, data_2_Power, data_2_Water, data_2_Gaz, = self.write_Plateg_Komun()
    #     # data_1_Kvar, data_1_Tel, data_1_Inet, data_1_DSad, data_2_Kvar, data_2_Tel, data_2_Inet, data_2_DSad
    #
    #     data_base = 'Komunal.db'
    #     table_1 = 'Plategi_year_' + data_convert(data_1_Power)
    #     table_2 = 'Plategi_year_' + data_convert(data_2_Power)
    #
    #     heading = 'id integer, month_year text, Plateg text, Sum integer, Kol integer, Trf integer'
    #
    #     sqlite3_create_db(data_base, table_1, heading)
    #     sqlite3_create_db(data_base, table_2, heading)
    #
    #     try:
    #         col_name = 'id'
    #         a = [data_1_Power, data_1_Water, data_1_Gaz, data_2_Power, data_2_Water, data_2_Gaz]
    #         # data_1_Kvar, data_1_Tel, data_1_Inet, data_1_DSad, data_2_Kvar, data_2_Tel, data_2_Inet, data_2_DSad
    #
    #         for i in a:
    #             row_record = str(i[0])
    #             sqlite3_delete_record(data_base, table_1, col_name, row_record)
    #
    #         for i in a[0:7]:
    #             data_1 = i
    #             sqlite3_insert_tbl(data_base, table_1, data_1)
    #
    #         for i in a[6:14]:
    #             data_2 = i
    #             sqlite3_insert_tbl(data_base, table_2, data_2)
    #
    #         self.wp.label_OK_1.setPixmap(QtGui.QPixmap("./Resource/img/Galochka.png"))
    #
    #         if month.index(str(self.wp.comboBox_month_KP.currentText())) + 2 != 13:
    #             a = month.index(str(self.wp.comboBox_month_KP.currentText())) + 2
    #             b = td_month(a)
    #             c = str(self.wp.comboBox_year_KP.currentText())
    #         else:
    #             a = month.index(str(self.wp.comboBox_month_KP.currentText())) - 10
    #             b = td_month(a)
    #             c = str(int(self.wp.comboBox_year_KP.currentText()) + 1)
    #
    #         combo_m = self.wp.comboBox_month_KP
    #         combo_y = self.wp.comboBox_year_KP
    #
    #         today, a, b = self.ps.period(b, c, combo_m, combo_y)
    #
    #         self.wp.label_month_year_KP.setText(today)
    #         self.wp.comboBox_month_KP.setCurrentIndex(month.index(a))
    #         self.wp.comboBox_year_KP.setCurrentText(b)
    #         self.month_activated()
    #
    #     except sqlite3.IntegrityError:
    #         self.wp.checkBox_Edit_KP.hide()
    #         self.wp.label_ERROR.setText('Такая запись уже есть!')

    def btn_cancel_kp(self):
        self.WinPlateg.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    win_KP = KommunalPlateg()
    sys.exit(app.exec_())
