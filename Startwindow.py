# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Startwindow.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(613, 473)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.net_interfece = QtWidgets.QListWidget(self.centralwidget)
        self.net_interfece.setObjectName("net_interfece")
        item = QtWidgets.QListWidgetItem()
        self.net_interfece.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.net_interfece.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.net_interfece.addItem(item)
        self.gridLayout.addWidget(self.net_interfece, 0, 0, 1, 1)
        self.Start_capture = QtWidgets.QToolButton(self.centralwidget)
        self.Start_capture.setObjectName("Start_capture")
        self.gridLayout.addWidget(self.Start_capture, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 613, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuCapture = QtWidgets.QMenu(self.menubar)
        self.menuCapture.setObjectName("menuCapture")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionStart = QtWidgets.QAction(MainWindow)
        self.actionStart.setObjectName("actionStart")
        self.actionStopr = QtWidgets.QAction(MainWindow)
        self.actionStopr.setObjectName("actionStopr")
        self.actionRestart = QtWidgets.QAction(MainWindow)
        self.actionRestart.setObjectName("actionRestart")
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionExit)
        self.menuCapture.addAction(self.actionStart)
        self.menuCapture.addAction(self.actionStopr)
        self.menuCapture.addAction(self.actionRestart)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuCapture.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        __sortingEnabled = self.net_interfece.isSortingEnabled()
        self.net_interfece.setSortingEnabled(False)
        item = self.net_interfece.item(0)
        item.setText(_translate("MainWindow", "Network Interfeces"))
        item = self.net_interfece.item(1)
        item.setText(_translate("MainWindow", "Wifi"))
        item = self.net_interfece.item(2)
        item.setText(_translate("MainWindow", "Ethernet"))
        self.net_interfece.setSortingEnabled(__sortingEnabled)
        self.Start_capture.setText(_translate("MainWindow", "Start Capture"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuCapture.setTitle(_translate("MainWindow", "Capture"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionStart.setText(_translate("MainWindow", "Start"))
        self.actionStopr.setText(_translate("MainWindow", "Stop"))
        self.actionRestart.setText(_translate("MainWindow", "Restart"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

