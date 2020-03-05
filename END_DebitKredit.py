# -*- coding: utf-8 -*-

import sys
import win32api

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication

from FUN_KOMMUNAL import *
from END_CLASS_KOMM import Period
from UI_CLASS_KOMM import UiWinAdd

from UI_DebitKredit import UiWinDebitKredit


# ОКНО ДОХОДЫ/РАСХОДЫ
class DebitKredit(QtWidgets.QWidget, UiWinDebitKredit):
    def __init__(self, parent=None):
        super(DebitKredit, self).__init__(parent)

        self.wa = UiWinAdd()

        self.setupUi_DK(self)

        self.period_dk = Period(self.comboBox_month_DK, self.comboBox_year_DK, self.label_month_year_DK)

        current_month = convert_month(dt_month)  # Текущий месяц ("Январь")
        current_year = dt_year  # Текущий год ("2020")

        self.month_index = month.index(current_month)
        self.month_text = month[self.month_index]
        self.year_index = int(current_year)

        # ВЫБОР ПЕРИОДА
        combo_m = self.comboBox_month_DK
        combo_y = self.comboBox_year_DK
        selected_period(combo_m, combo_y)

        # установка ТЕКУЩЕГО ПЕРИОДА
        self.label_month_year_DK.setText(current_month + " " + current_year)  # устанавливает заголовок ("Январь 2020")
        self.comboBox_month_DK.setCurrentIndex(month.index(current_month))  # устанавливает текущий месяц ("Январь")
        self.comboBox_year_DK.setCurrentText(current_year)  # устанавливает текущий год ("2020")

        # ВЫБИРАЕМ период с помощью comboBox
        self.comboBox_month_DK.activated.connect(self.label_period)
        self.comboBox_year_DK.activated.connect(self.label_period)

        # ВЫБИРАЕМ период с помощью стрелок
        self.btn_Left_DK.clicked.connect(self.btn_period_left)
        self.btn_Right_DK.clicked.connect(self.btn_period_right)

        # ДОБАВЛЕНИЕ новые данные
        self.pushButton_add_Plateg_DK.clicked.connect(self.btn_add_plateg)

        # СОХРАНЯЕМ значения ДОХОДЫ/РАСХОДЫ
        self.pushButton_Save_DK.clicked.connect(self.btn_save_dk)

        # ЗАКРЫВАЕТ окно ДОХОДЫ/РАСХОДЫ
        self.pushButton_Cancel_DK.clicked.connect(self.btn_cancel_dk)

        # ЧИТАЕТ значения ДОХОДЫ/РАСХОДЫ из базы данных
        self.read_debit_kredit()

        self.show()

    # показывает в заголовке выбранный месяц и год
    def label_period(self):
        self.month_index = self.period_dk.label_sel_period()
        self.read_debit_kredit()

    # прокрутка переиода в лево
    def btn_period_left(self):
        self.month_index = self.period_dk.click_btn_left(self.month_index)
        self.read_debit_kredit()

    # прокрутка переиода в право
    def btn_period_right(self):
        self.month_index = self.period_dk.click_btn_right(self.month_index)
        self.read_debit_kredit()

    # открывает окно "добавление нового платежа"
    def btn_add_plateg(self):
        self.wa.name_plateg()
        if win32api.GetKeyboardLayout() == 67699721:  # 67699721 - английский 00000409
            win32api.LoadKeyboardLayout("00000419", 1)  # 68748313 - русский    00000419

        # # КНОПКИ окна ДОБАВЛЕНИЕ ПЛАТЕЖА
        # # кнопка OK
        # self.wa.btn_OK.clicked.connect(self.btn_ok_wa_name)
        # self.wa.btn_OK.setAutoDefault(True)
        # self.wa.lineEdit.returnPressed.connect(self.wa.btn_OK.click)
        #
        # # кнопка ОТМЕНА
        # self.wa.btn_Cancel.clicked.connect(self.btn_cancel_wa)

    # кнопка OK окна выбора "ДОХОД/РАСХОД"
    def btn_ok_wa_name(self):
        pass

    # кнопка OK окна "сумма нового платежа"
    def btn_ok_sum_pl(self):
        pass

    # кнопка CANCEL окна "имя нового платежа"
    def btn_cancel_wa(self):
        pass

    # кнопка CANCEL окна "сумма нового платежа"
    def btn_cancel_sum_plat(self):
        pass

    # читаем сохраненые данные из базы данных
    def read_debit_kredit(self):  # читаем данные из базы данных
        pass

    # вычисляем сумму платежа и заносим в поле сумма
    def sum_platega(self):
        pass

    # вычисляем итоговою сумму платежей
    def itog_sum(self):
        pass

    # режим редактирования
    def text_editing(self):
        pass

    # подготовка данных к сохранению
    def create_list_plateg_kommun(self):
        pass

    # кнопка сохранения данных
    def btn_save_dk(self):
        pass

    # режим перезаписи сохраненных данных
    def save_yes_or_not(self):
        pass

    # перезапись сохраненных данных
    def btn_ok_save_yn(self):
        pass

    # кнопка отмены перезаписи
    def btn_cancel_save_yn(self):
        pass

    def btn_cancel_dk(self):
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    win_DB = DebitKredit()
    sys.exit(app.exec_())
