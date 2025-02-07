from os import write
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import *
import sys

class second_win(QDialog):
    def __init__(self):
        super().__init__()
        self.records = []
        self.initUI()


    def initUI(self):
        uic.loadUi("UI_design/secui.ui", self)

    def write(self):
        for record in self.records:
            pass