# -*- coding: utf-8 -*-

import sys
import win32api

from PyQt5.QtWidgets import QApplication

from FUN_KOMMUNAL import *
from UI_KommunalPlateg import UiWinPlateg


# ОКНО КОММУНАЛЬНЫХ ПЛАТЕЖЕЙ
class DebitKredit(QtWidgets.QWidget, UiWinPlateg):
    def __init__(self, parent=None):
        super(DebitKredit, self).__init__(parent)

        self.WinDKredit = UiWinPlateg()

        self.setupUi_KP(self)