from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QApplication, QMainWindow
import Generator
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.initUI()

    def initUI(self):
        uic.loadUi("mainui.ui", self)
        self.val = Generator.generate()
        # Pobranie pól tekstowych (QLineEdit)
        self.edit_login = self.findChild(QtWidgets.QLineEdit, 'lineEdit_login')
        self.edit_pass = self.findChild(QtWidgets.QLineEdit, 'lineEdit_pass')
        self.edit_mail = self.findChild(QtWidgets.QLineEdit, 'lineEdit_mail')

        # Pobranie przycisku (QPushButton)
        self.submit = self.findChild(QtWidgets.QPushButton, 'submit')
        self.mailbutt = self.findChild(QtWidgets.QPushButton, 'mailbutt')

        # interakcje z przyciskiem
        self.submit.clicked.connect(self.check)
        self.mailbutt.clicked.connect(self.send)

        # Pobranie etykiety (QLabel)
        self.label_login = self.findChild(QtWidgets.QLabel, 'label_login')

    def check(self):
        # Pobranie danych
        login_text = self.edit_login.text()
        password_text = self.edit_pass.text()
        code_text = self.edit_mail.text()

        print("Login:", login_text)
        print("Hasło:", password_text)
        print("Email:", code_text)

        # Weryfikacja poprawnosci danych z uzytkownikiem
        if code_text == self.val:
            print("ok")
        else:
            print("error")
        self.label_login.setText(password_text)



    def send(self):
        # generuje randomowy kod weryfikacyjny
        self.val = Generator.generate()

def window():
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())

window()