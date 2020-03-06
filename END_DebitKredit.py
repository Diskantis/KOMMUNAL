# -*- coding: utf-8 -*-

import sys
import win32api

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication

from Resource.FUN_KOMMUNAL import *
from Resource.END_CLASS_KOMM import Period
from Resource.UI_CLASS_KOMM import UiWinAdd

from UI_DebitKredit import UiWinDebitKredit


# ОКНО ДОХОДЫ/РАСХОДЫ
class DebitKredit(QtWidgets.QWidget, UiWinDebitKredit):
    def __init__(self, parent=None):
        super(DebitKredit, self).__init__(parent)

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
        self.pushButton_add_Plateg_DK.clicked.connect(self.sel_deb_kred)

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

    # значения по умолчанию
    def default_win(self, y=0):
        self.WinDebKred.resize(800, 400)
        self.WinDebKred.setMinimumSize(QtCore.QSize(800, 365 + y))
        self.frame_Debit.setGeometry(QtCore.QRect(20, 85, 760, 0 + y))
        self.frame_Kredit.setGeometry(QtCore.QRect(20, 190, 760, 0 + y))

    # окно выбора "ДОХОД/РАСХОД"
    def sel_deb_kred(self):
        self.radio_plat = UiWinAdd()
        self.radio_plat.radio_btn()

        self.radio_plat.btn_OK.clicked.connect(self.win_add_name_ok)  # кнопка OK
        self.radio_plat.btn_OK.setAutoDefault(True)

        self.radio_plat.btn_Cancel.clicked.connect(self.radio_plat_cancel)  # кнопка CANCEL

    # кнопка CANCEL окна выбора "ДОХОД/РАСХОД"
    def radio_plat_cancel(self):
        self.radio_plat.close()

    # окно "ИМЯ нового платежа"
    def win_add_name_ok(self):
        self.radio_plat.close()

        if win32api.GetKeyboardLayout() == 67699721:  # 67699721 - английский 00000409
            win32api.LoadKeyboardLayout("00000419", 1)  # 68748313 - русский    00000419

        self.win_add = UiWinAdd()
        self.win_add.name_plateg()

        self.name = self.win_add.lineEdit.text()

        self.win_add.btn_OK.clicked.connect(self.win_add_summ_ok)  # кнопка OK
        self.win_add.btn_OK.setAutoDefault(True)
        self.win_add.lineEdit.returnPressed.connect(self.win_add.btn_OK.click)

        self.win_add.btn_Cancel.clicked.connect(self.win_add_name_cancel)  # кнопка CANCEL

    # кнопка CANCEL окна "ИМЯ нового платежа"
    def win_add_name_cancel(self):
        self.win_add.lineEdit.clear()
        self.win_add.close()

    # окно "СУММА нового платежа"
    def win_add_summ_ok(self):
        self.win_add.lineEdit.clear()
        self.win_add.close()

        if win32api.GetKeyboardLayout() == 68748313:  # 67699721 - английский 00000409
            win32api.LoadKeyboardLayout("00000409", 1)  # 68748313 - русский    00000419

        self.summ_plat = UiWinAdd()
        self.summ_plat.name_plateg()
        self.summ_plat.label.setText("Сумма платежа")

        self.sum = self.summ_plat.lineEdit.text()

        if self.summ_plat.btn_OK.clicked.connect(lambda: self.create_plat(self.win_resize_y, self.position)): pass
        self.summ_plat.btn_OK.setAutoDefault(True)
        self.summ_plat.lineEdit.returnPressed.connect(self.summ_plat.btn_OK.click)

        self.summ_plat.btn_Cancel.clicked.connect(self.win_add_summ_cancel)  # кнопка CANCEL

    # кнопка CANCEL окна "СУММА нового платежа"
    def win_add_summ_cancel(self):
        self.summ_plat.lineEdit.clear()
        self.summ_plat.close()

    def create_plat(self, y, position):
        self.summ_plat.lineEdit.clear()
        self.summ_plat.close()

        self.frame_plateg(self.frame_Kredit, self.name, self.gLayout_Kredit, position)
        self.default_win(y)
        # self.lineEdit_sum_Plat.setText(text_convert(self.sum) + " руб")

        # self.dop_plategi[self.name] = float(self.sum), 0, 0, 0
        # self.dict_pole[self.name] = self.lineEdit_sum_Plat
        # self.plategi_sum += float(self.sum)
        # self.itog_sum(self.plategi_sum)

        self.win_resize_y += 32
        self.position += 1

        self.btn_del_Plat.clicked.connect(self.btn_del_plateg)  # возможно удаление после того как был создан доп. плат.

    # УДАЛЕНИЕ "нового платежа"
    def btn_del_plateg(self):
        self.widget_Plat.close()
        self.plategi_sum -= float(self.sum)
        if self.plategi_sum <= 0:
            self.lineEdit_IS_sum.clear()
        self.itog_sum(self.plategi_sum)
        self.win_resize_y -= 32
        self.position -= 1

    # читаем сохраненые данные из базы данных
    def read_debit_kredit(self):  # читаем данные из базы данных
        pass
        self.win_resize_y = 35
        self.position = 1

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
