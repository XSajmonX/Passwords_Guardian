from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import *
from os import write

class third_win(QDialog):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        uic.loadUi("UI_design/thiui.ui", self)
