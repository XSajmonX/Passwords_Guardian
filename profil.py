from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import *
from File_operations import crypt, read_users_file

class profil_win(QDialog):
    def __init__(self,user):
        super().__init__()
        self.user = user
        self.initUI()
        self.setWindowTitle("User Profile")

    def initUI(self):
        uic.loadUi("UI_design/add_user_win.ui", self)  # Inicjalizacjia graficznego interfejsu
        # Pobranie pól tekstowych (QLineEdit)
        self.login = self.findChild(QtWidgets.QLineEdit, 'user_lineEdit')
        self.user_pass = self.findChild(QtWidgets.QLineEdit, 'user_lineEdit1')
        self.user_pass_rep = self.findChild(QtWidgets.QLineEdit, 'user_lineEdit2')
        self.email = self.findChild(QtWidgets.QLineEdit, 'user_lineEdit3')

        self.login.setText(self.user.login)

        # Pobranie przycisku (QPushButton)
        self.commit = self.findChild(QtWidgets.QPushButton, 'user_add')
        self.commit.setText("Modify Profil")
        # Interakcja z przyciskiem
        self.commit.clicked.connect(self.modify_profil)

    def modify_profil(self):

        # Pobranie danych z QLineEdit
        login_text = self.login.text()
        password_text = self.user_pass.text()
        password_rep_text = self.user_pass_rep.text()
        email = self.email.text()
        # Weryfikacja podanych danych
        if password_text.strip() == '' or password_rep_text.strip() == '' or login_text.strip() == '' or email.strip() == '':
            print("empty field - add user")
            return

        # Weryfikacja podanych danych
        if password_text == password_rep_text:
            print('Pass ok')
        else:
            print("Pass1 not equal Pass2")
            return

        users_list = read_users_file()

        # Zmiana danych użytkownika
        for user in users_list:
            if user.id == self.user.id:
                user.login = login_text
                user.password = password_text
                user.email = email

        # Zapisanie danych uzytkownika do pliku + szyfrowanie
        encrypt = crypt(self.user.id,login_text,password_text,email)
        save = open("Users.csv",'w')
        save.write(encrypt)
        save.close()