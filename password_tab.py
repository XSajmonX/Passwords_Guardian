from File_operations import encrypt_record
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import *
from File_operations import read_records
from PyQt5.QtCore import Qt
from Record import Record
from modify import modify_win

class password_manager_win(QDialog):
    def __init__(self,user,main_window):
        super().__init__()
        self.main_win = main_window
        self.user_services = []
        self.user = user
        try:
            self.services = read_records(user)  # Lista obiektów usług
            self.services.reverse()
            self.initUI()
        except FileNotFoundError:
            print("brak pliku")
            self.services = []
            self.initUI()

    def initUI(self):
        uic.loadUi("UI_design/pass_win.ui", self) # Inicjalizacjia graficznego interfejsu
        # Pobranie pól tekstowych (QLineEdit)
        self.new_serv = self.findChild(QtWidgets.QLineEdit, 'new_service')
        self.new_login = self.findChild(QtWidgets.QLineEdit, 'new_login')
        self.new_pass = self.findChild(QtWidgets.QLineEdit, 'new_pass')

        self.new_record = self.findChild(QtWidgets.QPushButton, 'add_record')
        self.logoutButt = self.findChild(QtWidgets.QPushButton,'logout')
        self.Delete = self.findChild(QtWidgets.QPushButton, 'Delete')
        self.modify = self.findChild(QtWidgets.QPushButton, 'modify')

        self.new_record.clicked.connect(self.add_new_record)
        self.logoutButt.clicked.connect(self.log_out)
        self.Delete.clicked.connect(self.delete_selected_record)
        self.modify.clicked.connect(self.modify_record)


        self.table = self.findChild(QTableWidget, 'tableWidget')
        self.populate_table()

    def populate_table(self):
        self.table.setColumnCount(4)
        self.table.setRowCount(len(self.services))
        self.table.setHorizontalHeaderLabels(["Service", "Login", "Password", "Action"])
        """ Wstawia dane do tabeli """
        for row, service in enumerate(self.services):

            # Tworzymy komórki i ustawiamy wyrównanie do środka
            serv_item = QTableWidgetItem(service.serv)
            serv_item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)

            login_item = QTableWidgetItem(service.login)
            login_item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)

            hidden_pass = QTableWidgetItem("****")
            hidden_pass.setTextAlignment(Qt.AlignmentFlag.AlignCenter)


            self.table.setItem(row, 0, serv_item)
            self.table.setItem(row, 1, login_item)
            self.table.setItem(row, 2, hidden_pass)


            self.table.setRowHeight(row, 100)
            self.table.setColumnWidth(0, 150)  # "Usługa"
            self.table.setColumnWidth(1, 200)  # "Login"
            self.table.setColumnWidth(2, 500)  # "Hasło"
            self.table.setColumnWidth(3, 200)  # "Akcje" (przyciski)

            # Przycisk do odkrywania hasła
            btn_show = QPushButton("Show/Hide")
            btn_show.setAutoDefault(False)
            btn_show.clicked.connect(lambda _, r=row, p=hidden_pass, s=service: self.toggle_password(r, p, s))

            # Przycisk do kopiowania hasła
            btn_copy = QPushButton("Copy")
            btn_copy.setAutoDefault(False)
            btn_copy.clicked.connect(lambda _, s=service: self.copy_to_clipboard(s))

            # Dodanie przycisków do tabeli
            action_widget = QWidget()
            action_layout = QVBoxLayout()
            action_layout.addWidget(btn_show)
            action_layout.addWidget(btn_copy)
            action_layout.setSpacing(5)  # Dystans między przyciskami
            action_layout.setContentsMargins(0, 0, 0, 0)  # Brak marginesów
            action_widget.setLayout(action_layout)

            self.table.setCellWidget(row, 3, action_widget)

            # Uniemożliwienie edycji dla każdej komórki
            for col in range(3):  # Kolumny 0, 1, 2, 3
                item = self.table.item(row, col)
                if item:
                    item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)  # Tylko do odczytu

    def toggle_password(self, row, item, service):
        """ Odkrywa lub ukrywa hasło po kliknięciu """
        if item.text() == "****":
            item.setText(service.password)
            item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
        else:
            item.setText("****")
            item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)

    def copy_to_clipboard(self, service):
        """ Kopiuje hasło do schowka """
        clipboard = QApplication.clipboard()
        clipboard.setText(service.password)

    def add_new_record(self):
        serv = self.new_serv.text()
        log = self.new_login.text()
        pas = self.new_pass.text()

        if serv.strip() == "" or log.strip() == "" or pas.strip() == "":
            print("empty add new pass field")
            return

        encrypt_rec = encrypt_record(serv,log,pas)
        wr = open("Pass/{}.csv".format(self.user.id),'a')
        wr.write(encrypt_rec)
        wr.close()

        self.new_serv.setText("")
        self.new_login.setText("")
        self.new_pass.setText("")

        self.services.insert(0,Record(serv,log,pas))
        self.table.clear()
        self.populate_table()

    def log_out(self):
        self.close()
        self.main_win.show()

    def delete_selected_record(self):
        selected_row = self.table.currentRow()  # Pobierz zaznaczony wiersz
        if selected_row >= 0:  # Sprawdź, czy coś jest zaznaczone
            del self.services[selected_row]  # Usuń z listy
            self.table.removeRow(selected_row)  # Usuń z tabeli

        wr = open("Pass/{}.csv".format(self.user.id),'w')
        for record in self.services:
            encrypt_rec = encrypt_record(record.serv,record.login,record.password)
            wr.write(encrypt_rec)
        wr.close()

    def modify_record(self):
        selected_row = self.table.currentRow()  # Pobierz zaznaczony wiersz
        if selected_row >= 0:
            record = self.services[selected_row]

            self.mod = modify_win(self.user,self.table,record,self.services,selected_row,self.populate_table)
            self.mod.exec_()