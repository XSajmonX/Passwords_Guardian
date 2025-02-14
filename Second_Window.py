from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import *
import Fourth_Window
import Generator
import Mail


class second_win(QDialog):
    def __init__(self,user,main_window):
        super().__init__()
        self.main_win = main_window
        self.records = []
        self.user = user
        self.val = Generator.generate_verify_code()
        self.initUI()

    def initUI(self):
        uic.loadUi("UI_design/secui.ui", self) # Inicjalizacjia graficznego interfejsu
        # Pobranie pól tekstowych (QLineEdit)
        self.edit_login = self.findChild(QtWidgets.QLineEdit, 'lineEdit_mail')

        # Pobranie przycisku (QPushButton)
        self.mail_butt = self.findChild(QtWidgets.QPushButton, 'mailbutt')
        self.enter_butt = self.findChild(QtWidgets.QPushButton, 'enter')

        # Interakcja z przyciskiem
        self.mail_butt.clicked.connect(self.send_mail)
        self.enter_butt.clicked.connect(self.check_code)

    def check_code(self):
        eline = self.edit_login.text()
        if eline == self.val:
            print("kod jest ok")

            self.add_rec_window = Fourth_Window.fourth_win(self.user,self.main_win)
            self.close()
            self.add_rec_window.exec_()

    def send_mail(self):
        # generuje randomowy kod weryfikacyjny
        self.val = Generator.generate_verify_code()
        #Mail.new_mail(user.email)  # do poprawy - przekazanie danych przez konstruktor
        # wysyła kod na dany email