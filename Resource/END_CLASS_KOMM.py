# ВЫБОР ПЕРИОДА
class Period:
    def __init__(self, c_box_month, c_box_year, label_month_year):

        self.month = ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь',
                      'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь']

        self.comboBox_month = c_box_month
        self.comboBox_year = c_box_year
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
