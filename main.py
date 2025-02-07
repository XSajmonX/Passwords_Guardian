from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QApplication, QMainWindow
import Generator
import Second_Window
import sys
import Third_Window


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.initUI()

    def initUI(self):
        uic.loadUi("UI_design/mainui.ui", self)
        self.val = Generator.generate()
        # Pobranie pól tekstowych (QLineEdit)
        self.edit_login = self.findChild(QtWidgets.QLineEdit, 'lineEdit_login')
        self.edit_pass = self.findChild(QtWidgets.QLineEdit, 'lineEdit_pass')
        self.edit_mail = self.findChild(QtWidgets.QLineEdit, 'lineEdit_mail')

        # Pobranie przycisku (QPushButton)
        self.submit = self.findChild(QtWidgets.QPushButton, 'submit')
        self.mailbutt = self.findChild(QtWidgets.QPushButton, 'mailbutt')
        self.create_user = self.findChild(QtWidgets.QPushButton, 'create_user')

        # interakcje z przyciskiem
        self.submit.clicked.connect(self.check)
        self.mailbutt.clicked.connect(self.send)
        self.create_user.clicked.connect(self.create)

        # Pobranie etykiety (QLabel)
        self.label_login = self.findChild(QtWidgets.QLabel, 'label_login')

    def create(self):
        self.usr_create_window = Third_Window.third_win()  # Tworzenie drugiego okna
        self.usr_create_window.show()

    def check(self):
        # Pobranie danych
        login_text = self.edit_login.text()
        password_text = self.edit_pass.text()
        code_text = self.edit_mail.text()
        '''
                print("Login:", login_text)
        print("Hasło:", password_text)
        print("Email:", code_text)
        '''


        # Weryfikacja poprawnosci danych z uzytkownikiem
        if code_text == self.val:
            print("ok")
        else:
            print("error")

        self.second_window = Second_Window.second_win()  # Tworzenie drugiego okna
        self.second_window.show()
        self.close()


    def send(self):
        # generuje randomowy kod weryfikacyjny
        self.val = Generator.generate()

def window():
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())

window()