# -*- coding: utf-8 -*-

import sys

from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QApplication

from FUN_KOMMUNAL import *
from UI_PokazSchet import UiWinPokazanya


# ОКНО ПОКАЗАНИЯ СЧЕТЧИКОВ
class PokazSchet(QtWidgets.QWidget, UiWinPokazanya):
    def __init__(self, parent=None):
        super(PokazSchet, self).__init__(parent)

        self.setupUi_PS(self)

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
        self.comboBox_month_PS.activated.connect(self.label_sel_period)  # месяц
        self.comboBox_year_PS.activated.connect(self.label_sel_period)  # год

        self.btn_Left.clicked.connect(self.click_btn_left)  # прокрутка в лево
        self.btn_Right.clicked.connect(self.click_btn_right)  # прокрутка в право

        # режим РЕДАКТИРОВАНИЯ значений
        self.checkBox_Edit_PS.setChecked(False)
        self.checkBox_Edit_PS.stateChanged.connect(self.read_only)

        # СОХРАНЯЕТ показания счетчиков
        self.pushButton_Save_PS.clicked.connect(self.btn_save)

        # ЗАКРЫВАЕТ ОКНО показания счетчиков
        self.pushButton_Cancel_PS.clicked.connect(self.btn_cancel_ps)

        # ЧИТАЕТ показания из базы данных
        self.read_pokaz_schet()

    def label_sel_period(self):  # показывает в заголовке выбранный месяц и год
        m_sel = self.comboBox_month_PS.currentText()  # выбранный в comboBox месяц
        y_sel = self.comboBox_year_PS.currentText()  # выбранный в comboBox год
        self.label_month_year_PS.setText(m_sel + " " + y_sel)  # заголовок ("Январь 2020")
        self.month_index = month.index(m_sel)

        self.read_pokaz_schet()

    def click_btn_left(self):  # прокрутка переиода в лево
        if self.month_index > 0:
            self.month_index = self.comboBox_month_PS.currentIndex() - 1
            select_mount = month[self.month_index]
            self.comboBox_month_PS.setCurrentText(select_mount)
            self.year_index = self.comboBox_year_PS.currentText()
            self.label_month_year_PS.setText(select_mount + " " + self.year_index)
        else:
            self.month_index = 11
            select_mount = month[self.month_index]
            self.comboBox_month_PS.setCurrentText(select_mount)
            self.year_index = str(int(self.comboBox_year_PS.currentText()) - 1)
            self.comboBox_year_PS.setCurrentText(self.year_index)
            self.label_month_year_PS.setText(select_mount + " " + self.year_index)

        self.read_pokaz_schet()

    def click_btn_right(self):  # прокрутка переиода в право
        if self.month_index < 11:
            self.month_index = self.comboBox_month_PS.currentIndex() + 1
            select_mount = month[self.month_index]
            self.comboBox_month_PS.setCurrentText(select_mount)
            self.year_index = self.comboBox_year_PS.currentText()
            self.label_month_year_PS.setText(select_mount + " " + self.year_index)
        else:
            self.month_index = 0
            select_mount = month[self.month_index]
            self.comboBox_month_PS.setCurrentText(select_mount)
            self.year_index = str(int(self.comboBox_year_PS.currentText()) + 1)
            self.comboBox_year_PS.setCurrentText(self.year_index)
            self.label_month_year_PS.setText(select_mount + " " + self.year_index)

        self.read_pokaz_schet()

    def read_pokaz_schet(self):

        file_db = open('Komunal.db', 'a')  # открываем файл базы данных
        file_db.close()
        data_base = 'Komunal.db'  # имя базы данных
        table = 'Pokazanya_year_' + str(self.comboBox_year_PS.currentText())  # имя таблицы

        heading = ('id integer primary key , month_year text, Pred_PW integer, Actual_PW integer, Pred_WA_1 integer, '
                   'Actual_WA_1 integer, Pred_WA_2 integer, Actual_WA_2 integer, Pred_WA_3 integer, '
                   'Actual_WA_3 integer, Pred_WA_4 integer, Actual_WA_4 integer, Pred_GZ integer, Actual_GZ integer, '
                   'PW_month_ras integer, WA_C_month_ras integer, WA_H_month_ras integer, WA_month_ras integer, '
                   'GZ_month_ras integer')

        # это нужно если база данных отсутствует
        sqlite3_create_db(data_base, table, heading)  # создаем таблицу в базе данных

        # очищаем поля окна ПОКАЗАНИЯ СЧЕТЧИКОВ
        win_pole = [self.lineEdit_pokaz_P1, self.lineEdit_P1, self.lineEdit_pokaz_W1, self.lineEdit_W1,
                    self.lineEdit_pokaz_W2, self.lineEdit_W2, self.lineEdit_pokaz_W3, self.lineEdit_W3,
                    self.lineEdit_pokaz_W4, self.lineEdit_W4, self.lineEdit_pokaz_G1, self.lineEdit_G1,
                    self.label_PM_2, self.label_WM_2, self.label_WM_4, self.label_WM_6, self.label_GM_2,
                    self.label_ERROR, self.label_OK_1]

        for i in win_pole:
            i.clear()

        self.checkBox_Edit_PS.show()

        if not sqlite3_read_db(data_base, table)[0] and month[self.comboBox_month_PS.currentIndex()] == "Январь":
            table = 'Pokazanya_year_' + str(int(self.comboBox_year_PS.currentText()) - 1)

        read_table = sqlite3_read_db(data_base, table)  # читаем таблицу из базе данных
        read_table = read_table[0]

        for i in range(len(read_table)):
            pred_pokaz = read_table[i]  # показания сохраненного периода

            if self.label_month_year_PS.text() == pred_pokaz[1]:
                # присваеваем полям значения из сохраненной таблицы
                for a, b in zip(win_pole[:18], range(2, 19)):
                    a.setText(str(pred_pokaz[b]))
                if pred_pokaz[3] != 0:
                    self.label_OK_1.setPixmap(QtGui.QPixmap("./Resource/img/Galochka.png"))
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

        if self.lineEdit_P1.textEdited[str].connect(lambda: self.text_label(self.label_PM_2)): pass  # ЭЛЕКТРИЧЕСТВО
        if self.lineEdit_W1.textEdited[str].connect(lambda: self.text_label(self.label_WM_2)): pass  # ХОЛОДНАЯ ВОДА № 1
        if self.lineEdit_W2.textEdited[str].connect(lambda: self.text_label(self.label_WM_4)): pass  # ГОРЯЧАЯ ВОДА № 2
        if self.lineEdit_W3.textEdited[str].connect(lambda: self.text_label(self.label_WM_2)): pass  # ХОЛОДНАЯ ВОДА № 3
        if self.lineEdit_W4.textEdited[str].connect(lambda: self.text_label(self.label_WM_4)): pass  # ГОРЯЧАЯ ВОДА № 4
        if self.lineEdit_W4.textEdited[str].connect(lambda: self.text_label(self.label_WM_6)): pass  # ВСЯ ВОДА
        if self.lineEdit_G1.textEdited[str].connect(lambda: self.text_label(self.label_GM_2)): pass  # ГАЗ

    def text_label(self, label):
        try:
            self.label_ERROR.clear()
            self.checkBox_Edit_PS.show()
            label.setText('0')
            if label == self.label_PM_2:  # количество израсходованного за период ЭЛЕКТРИЧЕСТВА
                if int(self.lineEdit_P1.text()) != 0:
                    label.clear()
                    label.setText(str(int(self.lineEdit_P1.text()) - int(self.lineEdit_pokaz_P1.text())))
            elif label == self.label_WM_2:  # количество израсходованного за период ХОЛОДНОЙ ВОДЫ
                if int(self.lineEdit_W1.text()) or int(self.lineEdit_W3.text()) != 0:
                    label.clear()
                    label.setText(str((int(self.lineEdit_W1.text()) - int(self.lineEdit_pokaz_W1.text())) +
                                      (int(self.lineEdit_W3.text()) - int(self.lineEdit_pokaz_W3.text()))))
            elif label == self.label_WM_4:  # количество израсходованного за период ГОРЯЧЕЙ ВОДЫ
                if int(self.lineEdit_W2.text()) or int(self.lineEdit_W4.text()) != 0:
                    label.clear()
                    label.setText(str((int(self.lineEdit_W2.text()) - int(self.lineEdit_pokaz_W2.text())) +
                                      (int(self.lineEdit_W4.text()) - int(self.lineEdit_pokaz_W4.text()))))
            elif label == self.label_WM_6:  # количество израсходованного за период ВСЕГО ВОДЫ
                if int(self.lineEdit_W4.text()) != 0:
                    label.clear()
                    label.setText(str(((int(self.lineEdit_W1.text()) - int(self.lineEdit_pokaz_W1.text())) +
                                       (int(self.lineEdit_W3.text()) - int(self.lineEdit_pokaz_W3.text()))) +
                                      ((int(self.lineEdit_W2.text()) - int(self.lineEdit_pokaz_W2.text())) +
                                       (int(self.lineEdit_W4.text()) - int(self.lineEdit_pokaz_W4.text())))))
            elif label == self.label_GM_2:  # количество израсходованного за период ГАЗА
                if int(self.lineEdit_G1.text()) != 0:
                    label.clear()
                    label.setText(str(int(self.lineEdit_G1.text()) - int(self.lineEdit_pokaz_G1.text())))
        except ValueError:
            self.checkBox_Edit_PS.hide()
            self.label_ERROR.setText('Должно быдь значение!')

    def create_list_pokaz_schet(self):
        ppw = self.lineEdit_pokaz_P1.text()  # ПРЕДЫДУЩИЕ значение ЭЛЕКТРИЧЕСТВО
        apw = self.lineEdit_P1.text()  # ПОСЛЕДНЕЕ значение ЭЛЕКТРИЧЕСТВО
        pwa_1 = self.lineEdit_pokaz_W1.text()  # ПРЕДЫДУЩИЕ значение ВОДА № 1
        awa_1 = self.lineEdit_W1.text()  # ПОСЛЕДНЕЕ значение ВОДА № 1
        pwa_2 = self.lineEdit_pokaz_W2.text()  # ПРЕДЫДУЩИЕ значение ВОДА № 2
        awa_2 = self.lineEdit_W2.text()  # ПОСЛЕДНЕЕ значение ВОДА № 2
        pwa_3 = self.lineEdit_pokaz_W3.text()  # ПРЕДЫДУЩИЕ значение ВОДА № 3
        awa_3 = self.lineEdit_W3.text()  # ПОСЛЕДНЕЕ значение ВОДА № 3
        pwa_4 = self.lineEdit_pokaz_W4.text()  # ПРЕДЫДУЩИЕ значение ВОДА № 4
        awa_4 = self.lineEdit_W4.text()  # ПОСЛЕДНЕЕ значение ВОДА № 4
        pgz = self.lineEdit_pokaz_G1.text()  # ПРЕДЫДУЩИЕ значение ГАЗ
        agz = self.lineEdit_G1.text()  # ПОСЛЕДНЕЕ значение ГАЗ

        pow_mount_ras = self.label_PM_2.text()  # МЕСЯЧНЫЙ расход ЭЛЕКТРИЧЕСТВО
        w_cold_mount_ras = self.label_WM_2.text()  # МЕСЯЧНЫЙ расход ХОЛОДНАЯ ВОДА
        w_hot_mount_ras = self.label_WM_4.text()  # МЕСЯЧНЫЙ расход ГОРЯЧАЯ ВОДА
        w_mount_ras = self.label_WM_6.text()  # МЕСЯЧНЫЙ расход ВСЕГО ВОДА
        gaz_mount_ras = self.label_GM_2.text()  # МЕСЯЧНЫЙ расход ГАЗ

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
        data_base = 'Komunal.db'
        data = self.create_list_pokaz_schet()
        table = 'Pokazanya_year_' + data_convert(data)

        try:
            sqlite3_insert_tbl(data_base, table, data)

            if self.comboBox_month_PS.currentIndex() + 2 != 13:
                b = month[self.comboBox_month_PS.currentIndex() + 1]
                c = self.comboBox_year_PS.currentText()
            else:
                b = month[self.comboBox_month_PS.currentIndex() - 11]
                c = str(int(self.comboBox_year_PS.currentText()) + 1)

            self.label_month_year_PS.setText(b + " " + c)  # устанавливает заголовок ("Месяц Год")
            self.comboBox_month_PS.setCurrentIndex(month.index(b))  # устанавливает текущий месяц ("Месяц")
            self.comboBox_year_PS.setCurrentText(c)  # устанавливает текущий год ("Год")

            self.read_pokaz_schet()

        except sqlite3.IntegrityError:
            self.checkBox_Edit_PS.hide()
            self.label_ERROR.setText('Такая запись уже существует!')

    def read_only(self):  # режим РЕДАКТИРОВАНИЯ значений
        if self.checkBox_Edit_PS.isChecked():
            self.lineEdit_pokaz_P1.setReadOnly(False)
            self.lineEdit_pokaz_W1.setReadOnly(False)
            self.lineEdit_pokaz_W2.setReadOnly(False)
            self.lineEdit_pokaz_W3.setReadOnly(False)
            self.lineEdit_pokaz_W4.setReadOnly(False)
            self.lineEdit_pokaz_G1.setReadOnly(False)
        else:
            self.lineEdit_pokaz_P1.setReadOnly(True)
            self.lineEdit_pokaz_W1.setReadOnly(True)
            self.lineEdit_pokaz_W2.setReadOnly(True)
            self.lineEdit_pokaz_W3.setReadOnly(True)
            self.lineEdit_pokaz_W4.setReadOnly(True)
            self.lineEdit_pokaz_G1.setReadOnly(True)

    def btn_cancel_ps(self):
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    win_PS = PokazSchet()
    sys.exit(app.exec_())
