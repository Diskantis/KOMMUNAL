# -*- coding: utf-8 -*-

import sys

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication

from FUN_KOMMUNAL import *
from UI_KommunalPlateg import UiWinPlateg, UiWinAdd


# ОКНО КОММУНАЛЬНЫХ ПЛАТЕЖЕЙ
class KommunalPlateg(QtWidgets.QWidget, UiWinPlateg):
    def __init__(self, parent=None):
        super(KommunalPlateg, self).__init__(parent)

        self.wa = UiWinAdd()

        self.setupUi_KP(self)
        center(self.WinPlateg)

        self.y = 32
        self.position = 1

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
        if self.wa.btn_OK.clicked.connect(lambda: self.btn_ok_wa(self.y, self.position)): pass  # кнопка OK
        self.wa.btn_Cancel.clicked.connect(self.btn_cancel_wa)  # кнопка CANCEL

        # СОХРАНЯЕМ показания
        # self.wp.pushButton_Save_KP.clicked.connect(self.btn_save_kp)

        # ЗАКРЫВАЕТ окно ПОКАЗАНИЙ
        self.pushButton_Cancel_KP.clicked.connect(self.btn_cancel_kp)

        # ЧИТАЕТ платежи из базы данных
        self.read_plateg_kommun()

        # self.show()

    def label_sel_period(self):  # показывает в заголовке выбранный месяц и год
        # self.WinPlateg.resize(800, 400)
        # center(self.WinPlateg)
        # self.frame_plategi_KP.setGeometry(QtCore.QRect(20, 225, 760, 0))
        # self.label_OK_1.clear()
        # self.lineEdit_IS_sum.clear()
        # self.clear_layout(self.gridLayout)

        # self.y = 32
        # self.position = 1
        # self.plat = []
        # self.plat_sum = []
        # self.plategi_sum = 0

        m_sel = self.comboBox_month_KP.currentText()  # выбранный в comboBox месяц
        y_sel = self.comboBox_year_KP.currentText()  # выбранный в comboBox год
        self.label_month_year_KP.setText(m_sel + " " + y_sel)  # заголовок ("Январь 2020")
        self.month_index = month.index(m_sel)

        self.read_plateg_kommun()

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

        self.read_plateg_kommun()

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

        self.read_plateg_kommun()

    def btn_add_plateg(self):
        self.wa.name_plateg()

    def btn_ok_wa(self, y, position):
        name = self.wa.lineEdit.text()
        self.frame_plateg(name, position)

        self.frame_plategi_KP.setGeometry(QtCore.QRect(20, 225, 760, 0 + y))
        self.WinPlateg.resize(800, 365 + y)
        self.WinPlateg.setMinimumSize(QtCore.QSize(800, 365 + y))
        center(self.WinPlateg)

        self.y += 32
        self.position += 1

        self.wa.lineEdit.clear()
        self.wa.close()

    def btn_cancel_wa(self):
        self.wa.close()

    def text_label(self, label):
        sum_plate = 0
        if label == self.lineEdit_P_sum:
            sum_plate = float(self.lineEdit_P_kol.text()) * float(self.lineEdit_P_trf.text())
        elif label == self.lineEdit_W_sum:
            sum_plate = float(self.lineEdit_W_kol.text() * float(self.lineEdit_W_trf.text()))
        elif label == self.lineEdit_G_sum:
            sum_plate = float(self.lineEdit_G_kol.text() * float(self.lineEdit_G_trf.text()))
        return sum_plate

    def denominacia(self, cash):
        if int(self.comboBox_year_KP.currentText()) <= 2016:  # and self.comboBox_month_KP.currentIndex() + 1 < 6:
            den_cash = str(int(cash))
            den_cash = text_convert(den_cash)
        else:
            den_cash = str(round(cash, 2))
            den_cash = text_convert(den_cash)
        return den_cash

    def read_plateg_kommun(self):  # читаем данные из базы данных
        self.WinPlateg.resize(800, 400)
        center(self.WinPlateg)
        self.frame_plategi_KP.setGeometry(QtCore.QRect(20, 225, 760, 0))
        self.clear_layout(self.gridLayout)

        self.y = 32
        self.position = 1

        self.plat = []
        self.plat_sum = []
        self.plategi_sum = 0

        # очищаем ячейки окна
        a = [self.lineEdit_P_sum, self.lineEdit_P_kol, self.lineEdit_P_trf,
             self.lineEdit_W_sum, self.lineEdit_W_kol, self.lineEdit_W_trf,
             self.lineEdit_G_sum, self.lineEdit_G_kol, self.lineEdit_G_trf, self.label_ERROR, self.lineEdit_IS_sum]
        for i in a:
            i.clear()

        # self.label_ERROR.hide()
        # self.checkBox_Edit_KP.show()

        file_db = open('Komunal.db', 'a')
        file_db.close()
        data_base = 'Komunal.db'
        table_pokaz = 'Pokazanya_year_' + str(self.comboBox_year_KP.currentText())
        table_plateg = 'Plategi_year_' + str(self.comboBox_year_KP.currentText())
        heading = 'id integer, month_year text, Plateg text, Sum integer, Kol integer, Trf integer'

        sqlite3_create_db(data_base, table_plateg, heading)

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
            if i[0] == self.comboBox_month_KP.currentIndex() + 1:
                self.plat.append(i[2])
                self.plat_sum.append(i[3])
                if i[2] == 'Электричество':
                    self.lineEdit_P_trf.setText(str(i[5]))
                    pl_sum = float(self.lineEdit_P_kol.text()) * float(self.lineEdit_P_trf.text())
                    den = self.denominacia(pl_sum)
                    self.plategi_sum += float(pl_sum)
                    self.lineEdit_P_sum.setText(den + " руб")
                elif i[2] == 'Вода':
                    self.lineEdit_W_trf.setText(str(i[5]))
                    pl_sum = float(self.lineEdit_W_kol.text()) * float(self.lineEdit_W_trf.text())
                    den = self.denominacia(pl_sum)
                    self.plategi_sum += float(pl_sum)
                    self.lineEdit_W_sum.setText(den + " руб")
                elif i[2] == 'Газ':
                    self.lineEdit_G_trf.setText(str(i[5]))
                    pl_sum = float(self.lineEdit_G_kol.text()) * float(self.lineEdit_G_trf.text())
                    den = self.denominacia(pl_sum)
                    self.plategi_sum += float(pl_sum)
                    self.lineEdit_G_sum.setText(den + " руб")

                # if i[5] != 0:
                #     self.label_OK_1.setPixmap(QtGui.QPixmap("./Resource/img/Galochka.png"))

        if self.plategi_sum > 0:
            den = self.denominacia(self.plategi_sum)
            self.lineEdit_IS_sum.setText(den + " руб")

        for i in range(len(self.plat)):
            if i > 2:
                self.WinPlateg.resize(800, 365 + self.y)
                center(self.WinPlateg)
                self.frame_plategi_KP.setGeometry(QtCore.QRect(20, 225, 760, 0 + self.y))
                self.frame_plateg(self.plat[i], self.position)
                self.plategi_sum += float(self.plat_sum[i])
                self.lineEdit_Pl_sum.setText(text_convert(str(self.plat_sum[i])))
                self.y += 32
                self.position += 1

    #     if self.lineEdit_P_trf.textEdited[str].connect(lambda: self.text_label_1(self.lineEdit_P_sum)): pass  # ЭЛЕКТРО
    #     if self.lineEdit_W_trf.textEdited[str].connect(lambda: self.text_label_1(self.lineEdit_W_sum)): pass  # ВОДА
    #     if self.lineEdit_G_trf.textEdited[str].connect(lambda: self.text_label_1(self.lineEdit_G_sum)): pass  # ГАЗ
    #
    # def text_label_1(self, label):
    #     try:
    #         self.label_ERROR.clear()
    #         self.checkBox_Edit_KP.show()
    #         plateg_sum = 0
    #         if label == self.lineEdit_P_sum:
    #             a = float(self.lineEdit_P_kol.text()) * float(self.lineEdit_P_trf.text())
    #             ar = str(round(a, 2))  # обрезает число
    #             ar = text_convert(str(ar))  # разбивает число на разряды
    #             label.setText(ar)
    #             plateg_sum = a
    #         elif label == self.lineEdit_W_sum:
    #             a = float(int(self.lineEdit_W_kol.displayText()) * float(self.lineEdit_W_trf.text()))
    #             ar = str(round(a, 2))
    #             ar = text_convert(str(ar))
    #             label.setText(ar)
    #             plateg_sum = a
    #         elif label == self.lineEdit_G_sum:
    #             a = float(int(self.lineEdit_G_kol.displayText()) * float(self.lineEdit_G_trf.text()))
    #             ar = str(round(a, 2))
    #             ar = text_convert(str(ar))
    #             label.setText(ar)
    #             plateg_sum = a
    #         return plateg_sum
    #     except ValueError:
    #         self.checkBox_Edit_KP.hide()
    #         self.label_ERROR.setText('Должно быдь значение!')

        # for i in range(len(read_table_KP)):
        #     if read_table_KP[i][0] == self.comboBox_month_KP.currentIndex() + 1:
        #         self.plat.append(read_table_KP[i][2])
        #         self.plat_sum.append(read_table_KP[i][3])
        #         pred_plateg = read_table_KP[i]

        #     if read_table_KP[i][0] == month.index(self.comboBox_month_KP.currentText()) + 1 and :
        #         if self.lineEdit_P_trf.setText(str(read_table_KP[i][5])) != 0:
        #             self.text_label(self.lineEdit_P_sum)
        #             self.lineEdit_IS_sum.setText(text_convert(str(self.plategi_sum)))
        #         self.plategi_sum += float(read_table_KP[i][3])
        #     elif read_table_KP[i][0] == month.index(self.comboBox_month_KP.currentText()) + 1 and read_table_KP[i][2] == 'Вода':
        #         if self.lineEdit_W_trf.setText(str(read_table_KP[i][5])) != 0:
        #             self.text_label(self.lineEdit_W_sum)
        #         self.plategi_sum += float(read_table_KP[i][3])
        #     elif read_table_KP[i][0] == month.index(self.comboBox_month_KP.currentText()) + 1 and read_table_KP[i][2] == 'Газ':
        #         if self.lineEdit_G_trf.setText(str(read_table_KP[i][5])) != 0:
        #             self.text_label(self.lineEdit_G_sum)
        #         self.plategi_sum += float(read_table_KP[i][3])

    def clear_layout(self, layout):
        if layout is not None:
            while layout.count():
                child = layout.takeAt(0)
                if child.widget() is not None:
                    child.widget().deleteLater()
                elif child.layout() is not None:
                    self.clear_layout(child.layout())

    # def record_plateg_komun(self):
    #
    #     # print(self.plat, self.plat_sum, self.plategi_sum, end='\n')
    #
    #     psum = float(int(self.wp.lineEdit_P_kol.displayText()) * float(self.wp.lineEdit_P_trf.text()))
    #     pkol = self.wp.lineEdit_P_kol.text()
    #     ptrf = self.wp.lineEdit_P_trf.text()
    #     wsum = float(int(self.wp.lineEdit_W_kol.displayText()) * float(self.wp.lineEdit_W_trf.text()))
    #     wkol = self.wp.lineEdit_W_kol.text()
    #     wtrf = self.wp.lineEdit_W_trf.text()
    #     gsum = float(int(self.wp.lineEdit_G_kol.displayText()) * float(self.wp.lineEdit_G_trf.text()))
    #     gkol = self.wp.lineEdit_G_kol.text()
    #     gtrf = self.wp.lineEdit_G_trf.text()
    #
    #     # ksum = self.ui.lineEdit_K_sum.text()
    #     # tsum = self.ui.lineEdit_T_sum.text()
    #     # isum = self.ui.lineEdit_I_sum.text()
    #     # dsum = self.ui.lineEdit_D_sum.text()
    #
    #     id_row = month.index(str(self.wp.comboBox_month_KP.currentText())) + 1
    #     select_period_1 = str(self.wp.comboBox_month_KP.currentText()) + " " + str(
    #         self.wp.comboBox_year_KP.currentText())
    #     data_1_Power = [id_row, select_period_1, self.wp.label_Power.text(), psum, pkol, ptrf]
    #     data_1_Water = [id_row, select_period_1, self.wp.label_Water.text(), wsum, wkol, wtrf]
    #     data_1_Gaz = [id_row, select_period_1, self.wp.label_Gaz.text(), gsum, gkol, gtrf]
    #     # data_1_Kvar = [id_row, select_period_1, self.wp.label_Kvar.text(), ksum, 0, 0]
    #     # data_1_Tel = [id_row, select_period_1, self.wp.label_Tel.text(), tsum, 0, 0]
    #     # data_1_Inet = [id_row, select_period_1, self.wp.label_Inet.text(), isum, 0, 0]
    #     # data_1_DSad = [id_row, select_period_1, self.wp.label_DSad.text(), dsum, 0, 0]
    #
    #     if id_row != 12:
    #         select_period_2 = td_month(id_row, 0) + " " + str(self.wp.comboBox_year_KP.currentText())
    #         data_2_Power = [id_row + 1, select_period_2, self.wp.label_Power.text(), 0, 0, ptrf]
    #         data_2_Water = [id_row + 1, select_period_2, self.wp.label_Water.text(), 0, 0, wtrf]
    #         data_2_Gaz = [id_row + 1, select_period_2, self.wp.label_Gaz.text(), 0, 0, gtrf]
    #         # data_2_Kvar = [id_row + 1, select_period_2, self.ui.label_Kvar.text(), 0, 0, 0]
    #         # data_2_Tel = [id_row + 1, select_period_2, self.ui.label_Tel.text(), 0, 0, 0]
    #         # data_2_Inet = [id_row + 1, select_period_2, self.ui.label_Inet.text(), 0, 0, 0]
    #         # data_2_DSad = [id_row + 1, select_period_2, self.ui.label_DSad.text(), 0, 0, 0]
    #     else:
    #         select_period_2 = td_month(id_row, 12) + " " + str(int(self.wp.comboBox_year_KP.currentText()) + 1)
    #         data_2_Power = [id_row - 11, select_period_2, self.wp.label_Power.text(), 0, 0, ptrf]
    #         data_2_Water = [id_row - 11, select_period_2, self.wp.label_Water.text(), 0, 0, wtrf]
    #         data_2_Gaz = [id_row - 11, select_period_2, self.wp.label_Gaz.text(), 0, 0, gtrf]
    #         # data_2_Kvar = [id_row - 11, select_period_2, self.ui.label_Kvar.text(), 0, 0, 0]
    #         # data_2_Tel = [id_row - 11, select_period_2, self.ui.label_Tel.text(), 0, 0, 0]
    #         # data_2_Inet = [id_row - 11, select_period_2, self.ui.label_Inet.text(), 0, 0, 0]
    #         # data_2_DSad = [id_row - 11, select_period_2, self.ui.label_DSad.text(), 0, 0, 0]
    #
    #     return data_1_Power, data_1_Water, data_1_Gaz, data_2_Power, data_2_Water, data_2_Gaz
    #     data_1_Kvar, data_1_Tel, data_1_Inet, data_1_DSad, data_2_Kvar, data_2_Tel, data_2_Inet, data_2_DSad
    #
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

    def read_only(self):  # режим РЕДАКТИРОВАНИЯ значений
        if self.checkBox_Edit_KP.isChecked():
            self.lineEdit_P_sum.setReadOnly(False)
            self.lineEdit_P_kol.setReadOnly(False)
            self.lineEdit_W_sum.setReadOnly(False)
            self.lineEdit_W_kol.setReadOnly(False)
            self.lineEdit_G_sum.setReadOnly(False)
            self.lineEdit_G_kol.setReadOnly(False)
            self.lineEdit_Pl_sum.setReadOnly(False)  # TODO работает только когда добавлен платеж
        else:
            self.lineEdit_P_sum.setReadOnly(True)
            self.lineEdit_P_kol.setReadOnly(True)
            self.lineEdit_W_sum.setReadOnly(True)
            self.lineEdit_W_kol.setReadOnly(True)
            self.lineEdit_G_sum.setReadOnly(True)
            self.lineEdit_G_kol.setReadOnly(True)
            self.lineEdit_Pl_sum.setReadOnly(True)

    def btn_cancel_kp(self):
        self.WinPlateg.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    win_KP = KommunalPlateg()
    sys.exit(app.exec_())
