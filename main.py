from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QApplication, QMainWindow
import Second_Window
import sys
import Third_Window
from Coder_Decoder_users import read_file


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.initUI()

    def initUI(self):
        uic.loadUi("UI_design/mainui.ui", self) # Inicjalizacjia graficznego interfejsu

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
        self.usr_create_window = Third_Window.third_win()
        self.usr_create_window.show()

    def check(self):
        read_file()

        # Pobranie danych
        login_text = self.edit_login.text()
        password_text = self.edit_pass.text()
        '''
        print("Login:", login_text)
        print("Hasło:", password_text)
        '''
        # Weryfikacja danych logujacego sie użytkownika


        # Otworzenie okna do weryfikacji email
        #self.second_window = Second_Window.second_win()
       # self.second_window.exec_()


def window():
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())

window()