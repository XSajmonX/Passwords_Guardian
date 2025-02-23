from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import *
from password_tab import password_manager_win
import Generator
import Mail
import Messagebox

class verify_win(QDialog):
    def __init__(self,user,main_window,verify):
        super().__init__()
        self.main_win = main_window     # przekazanie głównego okna
        self.records = []
        self.user = user    # zalogowany user
        self.val = verify
        self.initUI()

    def initUI(self):
        uic.loadUi("UI_design/verify_win.ui", self) # Inicjalizacjia graficznego interfejsu
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
        if eline.strip() == '':
            Messagebox.messagebox("empty fields")
            print("empty verify code")
            return

        if eline == self.val:
            print("kod jest ok")

            self.add_rec_window = password_manager_win(self.user,self.main_win)
            self.close()
            self.add_rec_window.exec_()

    def send_mail(self):
        # generuje randomowy kod weryfikacyjny
        self.val = Generator.generate_verify_code()
        # wyślij email, wyjątek gdy brak połączenia z Internetem
        try:
            Mail.new_mail(self.user.email,self.val)  # do poprawy - przekazanie danych przez konstruktor
        except :
            Messagebox.messagebox("Check your connection to Internet. I can't send an email")
            print("nie wyslano emaila")
            return
        # wysyła kod na dany email