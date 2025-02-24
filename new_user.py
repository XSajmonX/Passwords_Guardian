from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import *
from File_operations import crypt, read_users_file
from Generator import generate_unique_id, gen_with_length
import Messagebox

class create_user_win(QDialog):
    def __init__(self):
        super().__init__()
        self.user_list = []
        self.initUI()

    def initUI(self):
        uic.loadUi("UI_design/add_user_win.ui", self) # Inicjalizacjia graficznego interfejsu

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

        #print(users_list)
        # Pobranie danych z QLineEdit
        login_text = self.login.text()
        password_text = self.user_pass.text()
        password_rep_text = self.user_pass_rep.text()
        email = self.email.text()

        if password_text.strip() == '' or password_rep_text.strip() == '' or login_text.strip() == '' or email.strip() == '':
            print("empty field - add user")
            Messagebox.messagebox("Empty fields")
            return

        # Weryfikacja podanych danych
        if password_text == password_rep_text:
            print('Pass ok')
        else:
            Messagebox.messagebox("Incorrect Password")
            print("Pass1 not equal Pass2")
            return

        try:
            user_id = generate_unique_id()
            users_list = read_users_file()
            for user in users_list:
                if login_text == user.login and password_text == user.password:
                    return print("Uzytkownik o takich danych istnieje")
        except FileNotFoundError:
            user_id = gen_with_length(10)
            print("brak pliku")

        # Zapisanie danych nowego uzytkownika do pliku + szyfrowanie AES
        encrypt = crypt(user_id,login_text,password_text,email)
        save = open("Users.csv",'a')
        save.write(encrypt)
        Messagebox.messagebox("New user has been created!")
        save.close()
