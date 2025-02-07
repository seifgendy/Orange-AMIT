# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'car.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer, QDateTime
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("*{\n"
"color:#000000\n"
"}\n"
"\n"
"#MainSide{\n"
"background-color:#808080\n"
"}\n"
"\n"
"#LeftSide{\n"
"background-color:#808080\n"
"}\n"
"\n"
"#RightSide{\n"
"background-color:#000000\n"
"}\n"
"\n"
"\n"
"")
        self.centralwidget.setObjectName("centralwidget")
        self.MainSide = QtWidgets.QWidget(self.centralwidget)
        self.MainSide.setGeometry(QtCore.QRect(0, 0, 791, 601))
        self.MainSide.setObjectName("MainSide")
        self.RightSide = QtWidgets.QWidget(self.MainSide)
        self.RightSide.setGeometry(QtCore.QRect(579, 60, 201, 541))
        self.RightSide.setObjectName("RightSide")
        self.Bluetooth = QtWidgets.QPushButton(self.RightSide)
        self.Bluetooth.setGeometry(QtCore.QRect(20, 120, 171, 51))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("bluetooth-alt.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Bluetooth.setIcon(icon)
        self.Bluetooth.setIconSize(QtCore.QSize(30, 30))
        self.Bluetooth.setObjectName("Bluetooth")
        self.Bluetooth_2 = QtWidgets.QPushButton(self.RightSide)
        self.Bluetooth_2.setGeometry(QtCore.QRect(20, 40, 171, 51))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("lock.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon1.addPixmap(QtGui.QPixmap("lock-open-alt.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.Bluetooth_2.setIcon(icon1)
        self.Bluetooth_2.setIconSize(QtCore.QSize(30, 30))
        self.Bluetooth_2.setObjectName("Bluetooth_2")
        self.Bluetooth_3 = QtWidgets.QPushButton(self.RightSide)
        self.Bluetooth_3.setGeometry(QtCore.QRect(20, 220, 171, 51))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("map-marker.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Bluetooth_3.setIcon(icon2)
        self.Bluetooth_3.setIconSize(QtCore.QSize(30, 30))
        self.Bluetooth_3.setObjectName("Bluetooth_3")
        self.Bluetooth_4 = QtWidgets.QPushButton(self.RightSide)
        self.Bluetooth_4.setGeometry(QtCore.QRect(20, 320, 171, 51))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("road-sign.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Bluetooth_4.setIcon(icon3)
        self.Bluetooth_4.setIconSize(QtCore.QSize(30, 30))
        self.Bluetooth_4.setObjectName("Bluetooth_4")
        self.Bluetooth_5 = QtWidgets.QPushButton(self.RightSide)
        self.Bluetooth_5.setGeometry(QtCore.QRect(20, 420, 171, 51))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("radio.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Bluetooth_5.setIcon(icon4)
        self.Bluetooth_5.setIconSize(QtCore.QSize(30, 30))
        self.Bluetooth_5.setObjectName("Bluetooth_5")
        self.LeftSide = QtWidgets.QWidget(self.MainSide)
        self.LeftSide.setGeometry(QtCore.QRect(-10, 0, 591, 601))
        self.LeftSide.setObjectName("LeftSide")
        self.Time = QtWidgets.QLabel(self.MainSide)
        self.Time.setGeometry(QtCore.QRect(590, 0, 81, 41))
        self.Time.setObjectName("Time")
        self.temp = QtWidgets.QLabel(self.MainSide)
        self.temp.setGeometry(QtCore.QRect(696, 0, 81, 41))
        self.temp.setObjectName("temp")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Timer to update time every second
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)  # Update every 1000 ms (1 second)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Bluetooth.setText(_translate("MainWindow", "     Bluetooth"))
        self.Bluetooth_2.setText(_translate("MainWindow", "     Lock"))
        self.Bluetooth_3.setText(_translate("MainWindow", "     Navigation"))
        self.Bluetooth_4.setText(_translate("MainWindow", "   Sign Detection"))
        self.Bluetooth_5.setText(_translate("MainWindow", "     Radio"))
        self.Time.setText(_translate("MainWindow", "00:00"))
        self.temp.setText(_translate("MainWindow", "TextLabel"))

    def update_time(self):
        """ Update the time label with the current time """
        current_time = QDateTime.currentDateTime().toString("hh:mm:ss")
        self.Time.setText(current_time)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
