from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import *
from os import write
from Coder_Decoder_users import crypt, read_file


class third_win(QDialog):
    def __init__(self):
        super().__init__()
        self.user_list = []
        self.initUI()

    def initUI(self):
        uic.loadUi("UI_design/thiui.ui", self) # Inicjalizacjia graficznego interfejsu

        # Pobranie pól tekstowych (QLineEdit)
        self.login = self.findChild(QtWidgets.QLineEdit, 'user_lineEdit')
        self.user_pass = self.findChild(QtWidgets.QLineEdit, 'user_lineEdit1')
        self.user_pass_rep = self.findChild(QtWidgets.QLineEdit, 'user_lineEdit2')
        self.email = self.findChild(QtWidgets.QLineEdit, 'user_lineEdit3')

        # Pobranie przycisku (QPushButton)
        self.add = self.findChild(QtWidgets.QPushButton, 'user_add')

        # Interakcja z przyciskiem
        self.add.clicked.connect(self.add_user)



    def add_user(self):
        # Pobranie danych z QLineEdit
        login_text = self.login.text()
        password_text = self.user_pass.text()
        password_rep_text = self.user_pass_rep.text()
        email = self.email.text()

        # Weryfikacja podanych danych
        if password_text == password_rep_text:
            print('Pass ok')

        # Zapisanie danych nowego uzytkownika do pliku + szyfrowanie AES
        encrypt = crypt(login_text,password_text,email)
        save = open("Users.csv",'a')
        save.write(encrypt)
        save.close()
