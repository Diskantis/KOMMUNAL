# -*- coding: utf-8 -*-

import sys
import win32api

from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QApplication

from Resource.FUN_KOMMUNAL import *
from Resource.END_CLASS_KOMM import Period
from Resource.UI_CLASS_KOMM import UiWinAdd

from UI_PokazSchet import UiWinPokazanya


# ОКНО ПОКАЗАНИЯ СЧЕТЧИКОВ
class PokazSchet(QtWidgets.QWidget, UiWinPokazanya):
    def __init__(self):
        super(PokazSchet, self).__init__()

        self.setupUi_PS(self)

        self.period_ps = Period(self.comboBox_month_PS, self.comboBox_year_PS, self.label_month_year_PS)

        current_month = convert_month(dt_month)  # Текущий месяц ("Месяц")
        current_year = dt_year  # Текущий год ("Год")

        self.month_index = month.index(current_month)
        self.month_text = month[self.month_index]
        self.year_index = int(current_year)

        # ВЫБОР ПЕРИОДА
        combo_m = self.comboBox_month_PS
        combo_y = self.comboBox_year_PS
        selected_period(combo_m, combo_y)

        # установка ТЕКУЩЕГО ПЕРИОДА
        self.label_month_year_PS.setText(current_month + " " + current_year)  # устанавливает заголовок ("Месяц Год")
        self.comboBox_month_PS.setCurrentIndex(month.index(current_month))  # устанавливает текущий месяц ("Месяц")
        self.comboBox_year_PS.setCurrentText(current_year)  # устанавливает текущий год ("Год")

        # ВЫБИРАЕМ период
        self.comboBox_month_PS.activated.connect(self.label_period)  # месяц
        self.comboBox_year_PS.activated.connect(self.label_period)  # год

        self.btn_Left_PS.clicked.connect(self.btn_period_left)  # прокрутка в лево
        self.btn_Right_PS.clicked.connect(self.btn_period_right)  # прокрутка в право

        # режим РЕДАКТИРОВАНИЯ значений
        self.checkBox_Edit_PS.setChecked(False)
        self.checkBox_Edit_PS.stateChanged.connect(self.read_only)

        # СОХРАНЯЕТ показания счетчиков
        self.pushButton_Save_PS.clicked.connect(self.btn_save)

        # ЗАКРЫВАЕТ ОКНО показания счетчиков
        self.pushButton_Cancel_PS.clicked.connect(self.btn_cancel_ps)

        # ЧИТАЕТ показания из базы данных
        self.read_pokaz_schet()

        self.show()

    # показывает в заголовке выбранный месяц и год
    def label_period(self):
        self.month_index = self.period_ps.label_sel_period()
        self.read_pokaz_schet()

    # прокрутка переиода в лево
    def btn_period_left(self):
        self.month_index = self.period_ps.click_btn_left(self.month_index)
        self.read_pokaz_schet()

    # прокрутка переиода в право
    def btn_period_right(self):
        self.month_index = self.period_ps.click_btn_right(self.month_index)
        self.read_pokaz_schet()

    # читаем сохраненые данные из базы данных
    def read_pokaz_schet(self):
        if win32api.GetKeyboardLayout() == 68748313:  # 67699721 - английский 00000409
            win32api.LoadKeyboardLayout("00000409", 1)  # 68748313 - русский    00000419

        file_db = open('Komunal.db', 'a')  # открываем файл базы данных
        file_db.close()
        self.data_base = 'Komunal.db'  # имя базы данных
        table = 'Pokazanya_year_' + str(self.comboBox_year_PS.currentText())  # имя таблицы
        col_name = 'id'  # Имя колонки

        heading = ('id integer primary key , month_year text, Pred_PW integer, Actual_PW integer, Pred_WA_1 integer, '
                   'Actual_WA_1 integer, Pred_WA_2 integer, Actual_WA_2 integer, Pred_WA_3 integer, '
                   'Actual_WA_3 integer, Pred_WA_4 integer, Actual_WA_4 integer, Pred_GZ integer, Actual_GZ integer, '
                   'PW_month_ras integer, WA_C_month_ras integer, WA_H_month_ras integer, WA_month_ras integer, '
                   'GZ_month_ras integer')

        # это нужно если база данных отсутствует
        sqlite3_create_db(self.data_base, table, heading)  # создаем таблицу в базе данных

        # очищаем поля окна ПОКАЗАНИЯ СЧЕТЧИКОВ
        win_pole = [self.lineEdit_pred_pokaz_P, self.lineEdit_post_pokaz_P,
                    self.lineEdit_pred_pokaz_W1, self.lineEdit_post_pokaz_W1,
                    self.lineEdit_pred_pokaz_W2, self.lineEdit_post_pokaz_W2,
                    self.lineEdit_pred_pokaz_W3, self.lineEdit_post_pokaz_W3,
                    self.lineEdit_pred_pokaz_W4, self.lineEdit_post_pokaz_W4,
                    self.lineEdit_pred_pokaz_G, self.lineEdit_post_pokaz_G,
                    self.label_month_ras_P, self.label_month_ras_WC, self.label_month_ras_WH, self.label_month_ras,
                    self.label_month_ras_G, self.label_ERROR_PS, self.label_OK_PS]

        for i in win_pole:
            i.clear()

        self.checkBox_Edit_PS.show()

        if self.comboBox_month_PS.currentIndex() + 1 in sqlite3_read_db(self.data_base, table, col_name)[0]:
            self.label_OK_PS.setPixmap(QtGui.QPixmap("./Resource/img/Galochka.png"))

        if not sqlite3_read_db(self.data_base, table)[0] and month[self.comboBox_month_PS.currentIndex()] == "Январь":
            table = 'Pokazanya_year_' + str(int(self.comboBox_year_PS.currentText()) - 1)

        read_table = sqlite3_read_db(self.data_base, table)  # читаем таблицу из базе данных
        read_table = read_table[0]

        for i in range(len(read_table)):
            pred_pokaz = read_table[i]  # показания сохраненного периода

            if self.label_month_year_PS.text() == pred_pokaz[1]:
                # присваеваем полям значения из сохраненной таблицы
                for a, b in zip(win_pole[:18], range(2, 19)):
                    a.setText(str(pred_pokaz[b]))
                break
            else:
                cor_month = month[self.comboBox_month_PS.currentIndex() - 1]
                if cor_month in pred_pokaz[1]:
                    # присваеваем полям "ПРЕДЫДУЩИЕ" значения из сохраненной таблицы
                    for c, d in zip(win_pole[:11:2], range(3, 14, 2)):
                        c.setText(str(pred_pokaz[d]))
                    # присваеваем полям "ПОСЛЕДНЕЕ" и "МЕСЯЧНЫЙ расход" значения "0"
                    for j in win_pole[1: 12: 2] + win_pole[12: 17]:
                        j.setText("0")

        self.lineEdit_post_pokaz_P.textEdited[str].connect(lambda: self.text_editing(self.label_month_ras_P))
        self.lineEdit_pred_pokaz_P.textEdited[str].connect(lambda: self.text_editing(self.label_month_ras_P))
        self.lineEdit_post_pokaz_W1.textEdited[str].connect(lambda: self.text_editing(self.label_month_ras_WC))
        self.lineEdit_pred_pokaz_W1.textEdited[str].connect(lambda: self.text_editing(self.label_month_ras_WC))
        self.lineEdit_post_pokaz_W2.textEdited[str].connect(lambda: self.text_editing(self.label_month_ras_WH))
        self.lineEdit_pred_pokaz_W2.textEdited[str].connect(lambda: self.text_editing(self.label_month_ras_WH))
        self.lineEdit_post_pokaz_W3.textEdited[str].connect(lambda: self.text_editing(self.label_month_ras_WC))
        self.lineEdit_pred_pokaz_W3.textEdited[str].connect(lambda: self.text_editing(self.label_month_ras_WC))
        self.lineEdit_post_pokaz_W4.textEdited[str].connect(lambda: self.text_editing(self.label_month_ras_WH))
        self.lineEdit_pred_pokaz_W4.textEdited[str].connect(lambda: self.text_editing(self.label_month_ras_WH))
        self.lineEdit_post_pokaz_G.textEdited[str].connect(lambda: self.text_editing(self.label_month_ras_G))
        self.lineEdit_pred_pokaz_G.textEdited[str].connect(lambda: self.text_editing(self.label_month_ras_G))

    def text_editing(self, label_month):
        try:
            self.label_ERROR_PS.clear()
            self.checkBox_Edit_PS.show()
            label_month.setText('0')
            if label_month == self.label_month_ras_P:  # количество израсходованного за период ЭЛЕКТРИЧЕСТВА
                if int(self.lineEdit_post_pokaz_P.text()) != 0:
                    label_month.clear()
                    label_month.setText(str(int(self.lineEdit_post_pokaz_P.text()) -
                                            int(self.lineEdit_pred_pokaz_P.text())))
            elif label_month == self.label_month_ras_WC:  # количество израсходованного за период ХОЛОДНОЙ ВОДЫ
                if int(self.lineEdit_post_pokaz_W1.text()) or int(self.lineEdit_post_pokaz_W3.text()) != 0:
                    label_month.clear()
                    label_month.setText(str((int(self.lineEdit_post_pokaz_W1.text()) -
                                             int(self.lineEdit_pred_pokaz_W1.text())) +
                                            (int(self.lineEdit_post_pokaz_W3.text()) -
                                             int(self.lineEdit_pred_pokaz_W3.text()))))
                    self.label_month_ras.setText(str(int(self.label_month_ras_WC.text()) +
                                                     int(self.label_month_ras_WH.text())))
            elif label_month == self.label_month_ras_WH:  # количество израсходованного за период ГОРЯЧЕЙ ВОДЫ
                if int(self.lineEdit_post_pokaz_W2.text()) or int(self.lineEdit_post_pokaz_W4.text()) != 0:
                    label_month.clear()
                    label_month.setText(str((int(self.lineEdit_post_pokaz_W2.text()) -
                                             int(self.lineEdit_pred_pokaz_W2.text())) +
                                            (int(self.lineEdit_post_pokaz_W4.text()) -
                                             int(self.lineEdit_pred_pokaz_W4.text()))))
                    self.label_month_ras.setText(str(int(self.label_month_ras_WC.text()) +
                                                     int(self.label_month_ras_WH.text())))
            elif label_month == self.label_month_ras_G:  # количество израсходованного за период ГАЗА
                if int(self.lineEdit_post_pokaz_G.text()) != 0:
                    label_month.clear()
                    label_month.setText(str(int(self.lineEdit_post_pokaz_G.text()) -
                                            int(self.lineEdit_pred_pokaz_G.text())))
        except ValueError:
            self.checkBox_Edit_PS.hide()
            self.label_ERROR_PS.setText('Должно быдь значение!')

        self.create_list_pokaz_schet()

    def read_only(self):  # режим РЕДАКТИРОВАНИЯ значений
        if self.checkBox_Edit_PS.isChecked():
            self.lineEdit_pred_pokaz_P.setReadOnly(False)
            self.lineEdit_pred_pokaz_W1.setReadOnly(False)
            self.lineEdit_pred_pokaz_W2.setReadOnly(False)
            self.lineEdit_pred_pokaz_W3.setReadOnly(False)
            self.lineEdit_pred_pokaz_W4.setReadOnly(False)
            self.lineEdit_pred_pokaz_G.setReadOnly(False)
        else:
            self.lineEdit_pred_pokaz_P.setReadOnly(True)
            self.lineEdit_pred_pokaz_W1.setReadOnly(True)
            self.lineEdit_pred_pokaz_W2.setReadOnly(True)
            self.lineEdit_pred_pokaz_W3.setReadOnly(True)
            self.lineEdit_pred_pokaz_W4.setReadOnly(True)
            self.lineEdit_pred_pokaz_G.setReadOnly(True)

    def create_list_pokaz_schet(self):
        ppw = self.lineEdit_pred_pokaz_P.text()  # ПРЕДЫДУЩИЕ значение ЭЛЕКТРИЧЕСТВО
        apw = self.lineEdit_post_pokaz_P.text()  # ПОСЛЕДНЕЕ значение ЭЛЕКТРИЧЕСТВО
        pwa_1 = self.lineEdit_pred_pokaz_W1.text()  # ПРЕДЫДУЩИЕ значение ВОДА № 1
        awa_1 = self.lineEdit_post_pokaz_W1.text()  # ПОСЛЕДНЕЕ значение ВОДА № 1
        pwa_2 = self.lineEdit_pred_pokaz_W2.text()  # ПРЕДЫДУЩИЕ значение ВОДА № 2
        awa_2 = self.lineEdit_post_pokaz_W2.text()  # ПОСЛЕДНЕЕ значение ВОДА № 2
        pwa_3 = self.lineEdit_pred_pokaz_W3.text()  # ПРЕДЫДУЩИЕ значение ВОДА № 3
        awa_3 = self.lineEdit_post_pokaz_W3.text()  # ПОСЛЕДНЕЕ значение ВОДА № 3
        pwa_4 = self.lineEdit_pred_pokaz_W4.text()  # ПРЕДЫДУЩИЕ значение ВОДА № 4
        awa_4 = self.lineEdit_post_pokaz_W4.text()  # ПОСЛЕДНЕЕ значение ВОДА № 4
        pgz = self.lineEdit_pred_pokaz_G.text()  # ПРЕДЫДУЩИЕ значение ГАЗ
        agz = self.lineEdit_post_pokaz_G.text()  # ПОСЛЕДНЕЕ значение ГАЗ

        pow_mount_ras = self.label_month_ras_P.text()  # МЕСЯЧНЫЙ расход ЭЛЕКТРИЧЕСТВО
        w_cold_mount_ras = self.label_month_ras_WC.text()  # МЕСЯЧНЫЙ расход ХОЛОДНАЯ ВОДА
        w_hot_mount_ras = self.label_month_ras_WH.text()  # МЕСЯЧНЫЙ расход ГОРЯЧАЯ ВОДА
        w_mount_ras = self.label_month_ras.text()  # МЕСЯЧНЫЙ расход ВСЕГО ВОДА
        gaz_mount_ras = self.label_month_ras_G.text()  # МЕСЯЧНЫЙ расход ГАЗ

        # СОЗДАЕМ СПИСОК ПОКАЗАНИЙ ЗА МЕСЯЦ
        # номер месяца ("Январь" = 1)
        id_row = month.index(self.comboBox_month_PS.currentText()) + 1
        # название периода ("Январь 2020")
        select_period = self.comboBox_month_PS.currentText() + " " + self.comboBox_year_PS.currentText()
        # список данных счетчиков предыдущие и последние
        data = [id_row, select_period, ppw, apw, pwa_1, awa_1, pwa_2, awa_2, pwa_3, awa_3,
                pwa_4, awa_4, pgz, agz, pow_mount_ras, w_cold_mount_ras, w_hot_mount_ras, w_mount_ras, gaz_mount_ras]

        return data

    def btn_save(self):
        data = self.create_list_pokaz_schet()
        table = 'Pokazanya_year_' + data_convert(data)
        col_name = 'id'  # Имя колонки
        row_record = str(data[0])  # Имя записи

        a = sqlite3_read_db(self.data_base, table, col_name)[0]

        try:
            if int(row_record) in a:
                self.save_yes_or_not()
            else:
                sqlite3_insert_tbl(self.data_base, table, data)

                self.read_pokaz_schet()

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

        except sqlite3.IntegrityError:
            self.checkBox_Edit_PS.hide()
            self.label_ERROR_PS.setText('Такая запись уже существует!')

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

    def btn_ok_save_yn(self):
        data = self.create_list_pokaz_schet()  # список данных для записи
        table = 'Pokazanya_year_' + data_convert(data)  # имя таблицы (период)
        col_name = 'id'  # имя колонки
        row_record = str(data[0])  # имя записи

        sqlite3_delete_record(self.data_base, table, col_name, row_record)
        sqlite3_insert_tbl(self.data_base, table, data)

        self.read_pokaz_schet()

        self.save_yn.close()

    def btn_cancel_save_yn(self):
        self.save_yn.close()

    def btn_cancel_ps(self):
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    win_PS = PokazSchet()
    sys.exit(app.exec_())
