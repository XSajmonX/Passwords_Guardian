from os import write
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import *
import Generator
import Mail

class second_win(QDialog):
    def __init__(self):
        super().__init__()
        self.records = []
        self.initUI()

    def initUI(self):
        uic.loadUi("UI_design/secui.ui", self) # Inicjalizacjia graficznego interfejsu


    def send_mail(self):
        # generuje randomowy kod weryfikacyjny
        self.val = Generator.generate()
        # wysyła kod na dany email