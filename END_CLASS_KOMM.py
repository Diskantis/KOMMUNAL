import win32api
from UI_CLASS_KOMM import *
from FUN_KOMMUNAL import text_convert


# ВЫБОР ПЕРИОДА
class Period:
    def __init__(self, cBox_month, cBox_year, label_month_year):
        self.month = ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь',
                      'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь']

        self.comboBox_month = cBox_month
        self.comboBox_year = cBox_year
        self.label_month_year = label_month_year

    def label_sel_period(self):  # показывает в заголовке выбранный месяц и год
        m_sel = self.comboBox_month.currentText()  # выбранный в comboBox месяц
        y_sel = self.comboBox_year.currentText()  # выбранный в comboBox год
        self.label_month_year.setText(m_sel + " " + y_sel)  # заголовок ("Январь 2020")
        month_index = self.month.index(m_sel)
        return month_index

    def click_btn_left(self, month_index):  # прокрутка переиода в лево
        if month_index > 0:
            month_index = self.comboBox_month.currentIndex() - 1
            self.comboBox_month.setCurrentText(self.month[month_index])
            self.year_index = self.comboBox_year.currentText()
            self.label_month_year.setText(self.month[month_index] + " " + self.year_index)
        else:
            month_index = 11
            self.comboBox_month.setCurrentText(self.month[month_index])
            self.year_index = str(int(self.comboBox_year.currentText()) - 1)
            self.comboBox_year.setCurrentText(self.year_index)
            self.label_month_year.setText(self.month[month_index] + " " + self.year_index)
        return month_index

    def click_btn_right(self, month_index):  # прокрутка переиода в право
        if month_index < 11:
            month_index = self.comboBox_month.currentIndex() + 1
            self.comboBox_month.setCurrentText(self.month[month_index])
            self.year_index = self.comboBox_year.currentText()
            self.label_month_year.setText(self.month[month_index] + " " + self.year_index)
        else:
            month_index = 0
            self.comboBox_month.setCurrentText(self.month[month_index])
            self.year_index = str(int(self.comboBox_year.currentText()) + 1)
            self.comboBox_year.setCurrentText(self.year_index)
            self.label_month_year.setText(self.month[month_index] + " " + self.year_index)
        return month_index


# ДОБАВЛЕНИЕ НОВЫХ ДАННЫХ
class DataAdd:
    def __init__(self):
        self.win_add = UiWinAdd

    # открывает окно "добавление нового платежа"
    def btn_add_plateg(self):
        self.win_add.name_plateg()

        if win32api.GetKeyboardLayout() == 67699721:  # 67699721 - английский 00000409
            win32api.LoadKeyboardLayout("00000419", 1)  # 68748313 - русский    00000419

    # кнопка OK окна "имя нового платежа"
    def win_add_name_ok(self, ):
        self.name = self.win_add.lineEdit.text()
        self.win_add.lineEdit.clear()
        self.win_add.close()

        self.summ_plat = UiWinAdd()
        self.summ_plat.name_plateg()
        self.summ_plat.label.setText("Сумма платежа")

        if win32api.GetKeyboardLayout() == 68748313:  # 67699721 - английский 00000409
            win32api.LoadKeyboardLayout("00000409", 1)  # 68748313 - русский    00000419

        if self.summ_plat.btn_OK.clicked.connect(lambda: self.win_add_summ_ok(self.win_resize_y, self.position)): pass
        self.summ_plat.btn_OK.setAutoDefault(True)
        self.summ_plat.lineEdit.returnPressed.connect(self.summ_plat.btn_OK.click)
        self.summ_plat.btn_Cancel.clicked.connect(self.win_add_summ_cancel)

    # кнопка CANCEL окна "имя нового платежа"
    def win_add_name_cancel(self):
        self.win_add.lineEdit.clear()
        self.win_add.close()

    # кнопка OK окна "сумма нового платежа"
    def win_add_summ_ok(self, y, position):
        self.summ_plat.lineEdit.close()
        self.sum = self.summ_plat.lineEdit.text()
        self.frame_plateg(self.name, position)
        self.default_win(y)
        self.lineEdit_sum_Plat.setText(text_convert(self.sum) + " руб")

        self.dop_plategi[self.name] = float(self.sum), 0, 0, 0
        self.dict_pole[self.name] = self.lineEdit_sum_Plat
        self.plategi_sum += float(self.sum)
        self.itog_sum(self.plategi_sum)

        self.win_resize_y += 32
        self.position += 1

        self.summ_plat.lineEdit.clear()
        self.summ_plat.close()

        self.btn_del_Plat.clicked.connect(self.btn_del_plateg)  # возможно удаление после того как был создан доп. плат.

    # кнопка CANCEL окна "сумма нового платежа"
    def win_add_summ_cancel(self):
        self.summ_plat.lineEdit.clear()
        self.summ_plat.close()

    def btn_del_plateg(self):
        self.widget_Plat.close()
        self.plategi_sum -= float(self.sum)
        if self.plategi_sum <= 0:
            self.lineEdit_IS_sum.clear()
        self.itog_sum(self.plategi_sum)
        self.win_resize_y -= 32
        self.position -= 1