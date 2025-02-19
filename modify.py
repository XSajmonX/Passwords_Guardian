from File_operations import encrypt_record
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import *
from File_operations import read_records
from PyQt5.QtCore import Qt
from Record import Record


class modify_win(QDialog):
    def __init__(self,user,table,record,services,selected,refresh):
        super().__init__()
        self.populate_table = refresh
        self.table = table
        self.record = record
        self.services = services
        self.user = user
        self.selected = selected
        self.initUI()


    def initUI(self):
        uic.loadUi("UI_design/modify_win.ui", self)  # Inicjalizacjia graficznego interfejsu
        # Pobranie pól tekstowych (QLineEdit)
        self.serv = self.findChild(QtWidgets.QLineEdit, 'serv')
        self.login = self.findChild(QtWidgets.QLineEdit, 'log')
        self.passw = self.findChild(QtWidgets.QLineEdit, 'pass')

        self.serv.setText(self.record.serv)
        self.login.setText(self.record.login)

        self.modify = self.findChild(QtWidgets.QPushButton, 'modify_butt')
        self.modify.clicked.connect(self.commit_changes)

    def commit_changes(self):
        serv = self.serv.text()
        log = self.login.text()
        passw = self.passw.text()
        print("commited")

        if passw.strip() == '' or log.strip() == '' or serv.strip() == '':
            print("empty modify pass")
            return

        self.services[self.selected].serv = serv
        self.services[self.selected].login = log
        self.services[self.selected].password = passw

        wr = open("Pass/{}.csv".format(self.user.id),'w')
        for record in self.services:
            encrypt_rec = encrypt_record(record.serv,record.login,record.password)
            wr.write(encrypt_rec)
        wr.close()

        self.populate_table()
