from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QApplication, QMainWindow
import Mail
from new_user import create_user_win
import sys
from verify import verify_win
import Generator
from File_operations import read_users_file
import Messagebox

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.initUI()

    def initUI(self):
        uic.loadUi("UI_design/main_win.ui", self) # Inicjalizacjia graficznego interfejsu

        # Pobranie pól tekstowych (QLineEdit)
        self.edit_login = self.findChild(QtWidgets.QLineEdit, 'lineEdit_login')
        self.edit_pass = self.findChild(QtWidgets.QLineEdit, 'lineEdit_pass')

        # Pobranie przycisku (QPushButton)
        self.submit = self.findChild(QtWidgets.QPushButton, 'submit')
        self.create_user = self.findChild(QtWidgets.QPushButton, 'create_user')

        # Interakcje z przyciskiem
        self.submit.clicked.connect(self.check)
        self.create_user.clicked.connect(self.create)

        # Pobranie etykiety (QLabel)
        self.label_login = self.findChild(QtWidgets.QLabel, 'label_login')

    def create(self):
        # Otworzenie okna do tworzenia nowych użytkowników
        self.usr_create_window = create_user_win()
        self.usr_create_window.exec_()

    def check(self):
        try:
            users_list = read_users_file()
        except:
            Messagebox.messagebox("Lack of Users. Create a new accout!")
            return
        # Pobranie danych
        login_text = self.edit_login.text()
        password_text = self.edit_pass.text()

        if login_text.strip() == '' or password_text.strip() == '':
            Messagebox.messagebox("empty fields")
            print("empty field - login")
            return

        # Weryfikacja danych logujacego sie użytkownika
        i=0
        for user in users_list:
            if login_text == user.login and password_text == user.password:
                print("weryfikacja poprawna")

                print("Id:", user.id)
                print("Login:", user.login)
                print("Hasło:", user.password)
                print("Mail:", user.email)

                # wysłanie maila z kodem do weryfikacji
                verify_code = Generator.generate_verify_code()
                # wyślij email, wyjątek gdy brak połączenia z Internetem
                try:
                    Mail.new_mail(user.email,verify_code)
                except :
                    Messagebox.messagebox("Check your connection to Internet. I can't send an email")
                    print("nie wyslano emaila")
                    return
                # Otworzenie okna do weryfikacji email
                self.verify_window = verify_win(user,self,verify_code)

                self.edit_login.setText("")
                self.edit_pass.setText("")

                self.hide()
                self.verify_window.exec_()

            else:
                i=i+1
                continue
        if i == len(users_list):
            Messagebox.messagebox("User is not exist")
            print("User is not exist")
def window():
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())

window()