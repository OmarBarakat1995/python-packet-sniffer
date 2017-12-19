# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!
import subprocess
import numpy as np
from PyQt5 import QtCore, QtGui, QtWidgets
from funcs import *
from scapy.all import *
import netifaces as nif
import psutil
from threading import Thread
import time
import datetime
import socket
from input_dialogue import *

class Ui_capturing_window():
    def __init__(self, mac):
        self.chosen_mac = mac
        print("constructoooooooooooooooooor")
        print(self.chosen_mac)
        self.capturing_status = True
        self.ip_protocols = {num:name[8:] for name,num in vars(socket).items() if name.startswith("IPPROTO")}


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(676, 545)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Search = QtWidgets.QLineEdit(self.centralwidget)
        self.Search.setObjectName("Search")
        self.verticalLayout.addWidget(self.Search)
        self.Searchbutton = QtWidgets.QToolButton(self.centralwidget)
        self.Searchbutton.setObjectName("Searchbutton")
        self.verticalLayout.addWidget(self.Searchbutton)
        self.Packets_table = QtWidgets.QTableWidget(self.centralwidget)
        self.Packets_table.setObjectName("Packets")
        self.Packets_table.setColumnCount(5)
        self.Packets_table.setRowCount(0)
        self.Packets_table.setColumnWidth(0,200) ###########################
        self.Packets_table.itemSelectionChanged.connect(self.selected_change)

        item = QtWidgets.QTableWidgetItem()
        self.Packets_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.Packets_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.Packets_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.Packets_table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.Packets_table.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.Packets_table.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.Packets_table.setHorizontalHeaderItem(6, item)
        self.verticalLayout.addWidget(self.Packets_table)
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout.addWidget(self.line_2)

        self.pack_details = QtWidgets.QTextBrowser(self.centralwidget)
        self.pack_details.setObjectName("pack_hex")
        self.verticalLayout.addWidget(self.pack_details)

        self.pack_raw = QtWidgets.QTextBrowser(self.centralwidget)
        self.pack_raw.setObjectName("pack_hex")
        self.verticalLayout.addWidget(self.pack_raw)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 676, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuCapture = QtWidgets.QMenu(self.menubar)
        self.menuCapture.setObjectName("menuCapture")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionOpen.triggered.connect(self.load_c)


        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionSave.triggered.connect(self.save_c)

        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")


        self.actionStart = QtWidgets.QAction(MainWindow)
        self.actionStart.setObjectName("actionStart")
        self.actionStart.triggered.connect(self.start_c)


        self.actionStop = QtWidgets.QAction(MainWindow)
        self.actionStop.setObjectName("actionStop")
        self.actionStop.triggered.connect(self.stop_c)


        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)


        self.menuFile.addAction(self.actionExit)
        self.menuCapture.addAction(self.actionStart)
        self.menuCapture.addAction(self.actionStop)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuCapture.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Second"))
        self.Search.setText(_translate("MainWindow", "Filter"))
        self.Searchbutton.setText(_translate("MainWindow", "Search"))

        item = self.Packets_table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Time"))
        item = self.Packets_table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Source"))
        item = self.Packets_table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Destination"))
        item = self.Packets_table.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Protocol"))
        item = self.Packets_table.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Length"))
        #item = self.Packets_table.horizontalHeaderItem(5)
        #item.setText(_translate("MainWindow", "Info"))

        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuCapture.setTitle(_translate("MainWindow", "Capture"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionStart.setText(_translate("MainWindow", "Start"))
        self.actionStop.setText(_translate("MainWindow", "Stop"))


    def reshow(self):
        self.window_to_reshow.show()

    def start_c(self):
        print("yessssssss")
        self.capturing_status = True
        sniffer = Thread(target=self.threaded_sniff_target)
        sniffer.daemon = True
        sniffer.start()


    def stop_c(self):
        print("stop")
        self.capturing_status = False

    def sniffed_packet(self,p):
        if IP in p:
            print("src", p[IP].src, mac_for_ip(p[IP].src))
            print("dst", p[IP].dst, mac_for_ip(p[IP].dst))
            if self.chosen_mac in [mac_for_ip(p[IP].src), mac_for_ip(p[IP].dst)]:
                rowPosition = self.Packets_table.rowCount()
                self.Packets_table.insertRow(rowPosition)
                self.Packets_table.setItem(rowPosition, 0, QtWidgets.QTableWidgetItem(str(datetime.datetime.fromtimestamp(p.time))))
                self.Packets_table.setItem(rowPosition, 1, QtWidgets.QTableWidgetItem(p[IP].src))
                self.Packets_table.setItem(rowPosition, 2, QtWidgets.QTableWidgetItem(p[IP].dst))
                self.Packets_table.setItem(rowPosition, 3, QtWidgets.QTableWidgetItem(self.ip_protocols[int(p[IP].proto)]))
                self.Packets_table.setItem(rowPosition, 4, QtWidgets.QTableWidgetItem(str(p[IP].len)))



    def threaded_sniff_target(self):
        self.pckts = sniff(prn=self.sniffed_packet, stop_callback=lambda : not self.capturing_status)
        print("stopped")


    def selected_change(self):
        index = self.Packets_table.currentRow()
        p = self.pckts[index]
        print(index)
        #print(str(hexdump(self.pckts[0])))

        #print("hexdump : \n",funcs.hexdump(s))
        #print(s)
        b = p.show
        p.show()
        try:
            #raw_load = self.pckts[index][Raw].load
            #print("raw load:", type(raw_load), raw_load)
            #base64_load = base64.b64encode(raw_load)
            #print("base64 :", type(base64_load), base64_load )
            #hb = base64_load.decode()
            #print("decoded :",type(hb), hb)

            e = str(b).index("<Raw")
            hex_dump = my_hexdump2(p)
            self.pack_raw.setText(hex_dump)
            hexdump(p)
            hd2 = my_hexdump2(p)
            print("hd2 : \n", hd2)

        except:
            e = -1
            self.pack_raw.setText(" ")

        self.pack_details.setText((("\n" + "-"*150 + "\n").join(str(b)[28: e].split("|"))).replace(" ","\n"))

        #self.pack_details.setText(str(index))
        #print("------------",str(p[self.ip_protocols[int(p[IP].proto)]].payload))

    def selected_change2(self):
        index = self.Packets_table.currentRow()
        print(index)

    def save_c(self):
        try:
            dialouge_box = Dialouge()
            self.file_name = dialouge_box. initUI()
            wrpcap(self.file_name, self.pckts)
        except:
            self.save_err_msg()


    def load_c(self):
        try:
            dialouge_box = Dialouge()
            self.file_name = dialouge_box.initUI()

            self.loadedPckts = rdpcap(self.file_name)

            print(len(self.loadedPckts))

            for p in self.loadedPckts:
                rowPosition = self.Packets_table.rowCount()
                self.Packets_table.insertRow(rowPosition)
                self.Packets_table.setItem(rowPosition, 0, QtWidgets.QTableWidgetItem(str(datetime.datetime.fromtimestamp(p.time))))
                self.Packets_table.setItem(rowPosition, 1, QtWidgets.QTableWidgetItem(p[IP].src))
                self.Packets_table.setItem(rowPosition, 2, QtWidgets.QTableWidgetItem(p[IP].dst))
                self.Packets_table.setItem(rowPosition, 3, QtWidgets.QTableWidgetItem(self.ip_protocols[int(p[IP].proto)]))
                self.Packets_table.setItem(rowPosition, 4, QtWidgets.QTableWidgetItem(str(p[IP].len)))

        except:
            self.load_err_msg()

    def save_err_msg(self):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Critical)
        msg.setWindowTitle("Error Message")
        msg.setText("couldn't save file")
        msg.exec_()


    def load_err_msg(self):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Critical)
        msg.setWindowTitle("Error Message")
        msg.setText("File not found!")
        msg.exec_()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_capturing_window("64:5a:04:b4:6a:1c")
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

