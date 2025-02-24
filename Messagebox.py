from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMessageBox

def messagebox(comment):
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Warning)
    msg.setWindowTitle("Information")
    msg.setWindowIcon(QIcon("UI_design/padlock.ico"))
    msg.setText(comment)
    msg.setStandardButtons(QMessageBox.Ok)
    msg.exec_()

def yes_no():
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Warning)
    msg.setWindowTitle("Warning!")
    msg.setWindowIcon(QIcon("UI_design/padlock.ico"))
    msg.setText("Are you sure to delete this record?")
    msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
    msg.setDefaultButton(QMessageBox.No)  # Domyślnie ustawiony na "Nie"
    reply = msg.exec_()

    if reply == QMessageBox.Yes:
        print("Yes")
        return 1
    else:
        print("No")
        return 0
