# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(408, 703)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Connec = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Connec.setFont(font)
        self.Connec.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.Connec.setObjectName("Connec")
        self.horizontalLayout.addWidget(self.Connec)
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.label_8.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout.addWidget(self.label_8)
        self.choiseCom = QtWidgets.QComboBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.choiseCom.setFont(font)
        self.choiseCom.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.choiseCom.setObjectName("choiseCom")
        self.choiseCom.addItem("")
        self.choiseCom.addItem("")
        self.choiseCom.addItem("")
        self.choiseCom.addItem("")
        self.choiseCom.addItem("")
        self.choiseCom.addItem("")
        self.choiseCom.addItem("")
        self.choiseCom.addItem("")
        self.choiseCom.addItem("")
        self.choiseCom.addItem("")
        self.choiseCom.addItem("")
        self.choiseCom.addItem("")
        self.choiseCom.addItem("")
        self.choiseCom.addItem("")
        self.choiseCom.addItem("")
        self.choiseCom.addItem("")
        self.choiseCom.addItem("")
        self.choiseCom.addItem("")
        self.choiseCom.addItem("")
        self.choiseCom.addItem("")
        self.choiseCom.addItem("")
        self.choiseCom.addItem("")
        self.choiseCom.addItem("")
        self.choiseCom.addItem("")
        self.choiseCom.addItem("")
        self.choiseCom.addItem("")
        self.choiseCom.addItem("")
        self.choiseCom.addItem("")
        self.choiseCom.addItem("")
        self.choiseCom.addItem("")
        self.choiseCom.addItem("")
        self.choiseCom.addItem("")
        self.choiseCom.addItem("")
        self.horizontalLayout.addWidget(self.choiseCom)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.Log = QtWidgets.QTabWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Log.setFont(font)
        self.Log.setToolTipDuration(-3)
        self.Log.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.Log.setObjectName("Log")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.Print = QtWidgets.QPushButton(self.tab_4)
        self.Print.setGeometry(QtCore.QRect(10, 110, 111, 31))
        self.Print.setObjectName("Print")
        self.SelectPrinter = QtWidgets.QPushButton(self.tab_4)
        self.SelectPrinter.setGeometry(QtCore.QRect(10, 170, 111, 31))
        self.SelectPrinter.setObjectName("SelectPrinter")
        self.ReadCard = QtWidgets.QPushButton(self.tab_4)
        self.ReadCard.setGeometry(QtCore.QRect(10, 10, 191, 61))
        self.ReadCard.setObjectName("ReadCard")
        self.AutoPrint = QtWidgets.QCheckBox(self.tab_4)
        self.AutoPrint.setGeometry(QtCore.QRect(10, 210, 121, 31))
        self.AutoPrint.setObjectName("AutoPrint")
        self.printerName = QtWidgets.QLabel(self.tab_4)
        self.printerName.setGeometry(QtCore.QRect(10, 140, 191, 31))
        self.printerName.setText("")
        self.printerName.setObjectName("printerName")
        self.line_8 = QtWidgets.QFrame(self.tab_4)
        self.line_8.setGeometry(QtCore.QRect(10, 80, 191, 20))
        self.line_8.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.line_10 = QtWidgets.QFrame(self.tab_4)
        self.line_10.setGeometry(QtCore.QRect(10, 240, 191, 20))
        self.line_10.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_10.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_10.setObjectName("line_10")
        self.InitCard = QtWidgets.QPushButton(self.tab_4)
        self.InitCard.setGeometry(QtCore.QRect(10, 320, 191, 61))
        self.InitCard.setObjectName("InitCard")
        self.AutoIncriment = QtWidgets.QCheckBox(self.tab_4)
        self.AutoIncriment.setGeometry(QtCore.QRect(10, 390, 151, 31))
        self.AutoIncriment.setObjectName("AutoIncriment")
        self.cardLine = QtWidgets.QLineEdit(self.tab_4)
        self.cardLine.setGeometry(QtCore.QRect(10, 270, 191, 41))
        self.cardLine.setObjectName("cardLine")
        self.Log.addTab(self.tab_4, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.groupBox = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox.setGeometry(QtCore.QRect(10, 410, 191, 131))
        self.groupBox.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.groupBox.setObjectName("groupBox")
        self.SleepCard = QtWidgets.QPushButton(self.groupBox)
        self.SleepCard.setGeometry(QtCore.QRect(100, 90, 81, 31))
        self.SleepCard.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.SleepCard.setObjectName("SleepCard")
        self.dtCompetion = QtWidgets.QDateTimeEdit(self.groupBox)
        self.dtCompetion.setGeometry(QtCore.QRect(10, 50, 171, 31))
        self.dtCompetion.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.dtCompetion.setMinimumDate(QtCore.QDate(2017, 12, 31))
        self.dtCompetion.setCalendarPopup(True)
        self.dtCompetion.setObjectName("dtCompetion")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(10, 20, 171, 20))
        self.label_4.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.label_4.setObjectName("label_4")
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 540, 191, 71))
        self.groupBox_2.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.groupBox_2.setObjectName("groupBox_2")
        self.ReadLog = QtWidgets.QPushButton(self.groupBox_2)
        self.ReadLog.setGeometry(QtCore.QRect(10, 30, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ReadLog.setFont(font)
        self.ReadLog.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.ReadLog.setObjectName("ReadLog")
        self.LogCard = QtWidgets.QPushButton(self.groupBox_2)
        self.LogCard.setGeometry(QtCore.QRect(100, 30, 81, 31))
        self.LogCard.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.LogCard.setObjectName("LogCard")
        self.groupBox_3 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 260, 191, 151))
        self.groupBox_3.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.groupBox_3.setObjectName("groupBox_3")
        self.SetNum = QtWidgets.QPushButton(self.groupBox_3)
        self.SetNum.setGeometry(QtCore.QRect(100, 30, 81, 31))
        self.SetNum.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.SetNum.setObjectName("SetNum")
        self.SetStart = QtWidgets.QPushButton(self.groupBox_3)
        self.SetStart.setGeometry(QtCore.QRect(10, 70, 81, 31))
        self.SetStart.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.SetStart.setObjectName("SetStart")
        self.SetFinish = QtWidgets.QPushButton(self.groupBox_3)
        self.SetFinish.setGeometry(QtCore.QRect(100, 70, 81, 31))
        self.SetFinish.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.SetFinish.setObjectName("SetFinish")
        self.CheckSt = QtWidgets.QPushButton(self.groupBox_3)
        self.CheckSt.setGeometry(QtCore.QRect(100, 110, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.CheckSt.setFont(font)
        self.CheckSt.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.CheckSt.setObjectName("CheckSt")
        self.ClearSt = QtWidgets.QPushButton(self.groupBox_3)
        self.ClearSt.setGeometry(QtCore.QRect(10, 110, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ClearSt.setFont(font)
        self.ClearSt.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.ClearSt.setObjectName("ClearSt")
        self.sbStationNum = QtWidgets.QSpinBox(self.groupBox_3)
        self.sbStationNum.setGeometry(QtCore.QRect(10, 30, 81, 31))
        self.sbStationNum.setFrame(True)
        self.sbStationNum.setAlignment(QtCore.Qt.AlignCenter)
        self.sbStationNum.setMinimum(1)
        self.sbStationNum.setMaximum(255)
        self.sbStationNum.setObjectName("sbStationNum")
        self.groupBox_4 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_4.setGeometry(QtCore.QRect(10, 120, 191, 71))
        self.groupBox_4.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.groupBox_4.setObjectName("groupBox_4")
        self.SetTime = QtWidgets.QPushButton(self.groupBox_4)
        self.SetTime.setGeometry(QtCore.QRect(100, 30, 81, 31))
        self.SetTime.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.SetTime.setObjectName("SetTime")
        self.groupBox_5 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_5.setGeometry(QtCore.QRect(10, 190, 191, 71))
        self.groupBox_5.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.groupBox_5.setObjectName("groupBox_5")
        self.btnCreateInfoCard = QtWidgets.QPushButton(self.groupBox_5)
        self.btnCreateInfoCard.setGeometry(QtCore.QRect(100, 30, 81, 31))
        self.btnCreateInfoCard.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.btnCreateInfoCard.setObjectName("btnCreateInfoCard")
        self.btnReadInfo = QtWidgets.QPushButton(self.groupBox_5)
        self.btnReadInfo.setGeometry(QtCore.QRect(10, 30, 81, 31))
        self.btnReadInfo.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.btnReadInfo.setObjectName("btnReadInfo")
        self.groupBox_6 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_6.setGeometry(QtCore.QRect(9, 10, 191, 111))
        self.groupBox_6.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.groupBox_6.setObjectName("groupBox_6")
        self.btnApplyPwd = QtWidgets.QPushButton(self.groupBox_6)
        self.btnApplyPwd.setGeometry(QtCore.QRect(100, 70, 81, 31))
        self.btnApplyPwd.setObjectName("btnApplyPwd")
        self.sbCurPwd3 = QtWidgets.QSpinBox(self.groupBox_6)
        self.sbCurPwd3.setGeometry(QtCore.QRect(10, 30, 51, 31))
        self.sbCurPwd3.setFrame(True)
        self.sbCurPwd3.setAlignment(QtCore.Qt.AlignCenter)
        self.sbCurPwd3.setMaximum(255)
        self.sbCurPwd3.setObjectName("sbCurPwd3")
        self.sbCurPwd2 = QtWidgets.QSpinBox(self.groupBox_6)
        self.sbCurPwd2.setGeometry(QtCore.QRect(70, 30, 51, 31))
        self.sbCurPwd2.setFrame(True)
        self.sbCurPwd2.setAlignment(QtCore.Qt.AlignCenter)
        self.sbCurPwd2.setMaximum(255)
        self.sbCurPwd2.setObjectName("sbCurPwd2")
        self.sbCurPwd1 = QtWidgets.QSpinBox(self.groupBox_6)
        self.sbCurPwd1.setGeometry(QtCore.QRect(130, 30, 51, 31))
        self.sbCurPwd1.setFrame(True)
        self.sbCurPwd1.setAlignment(QtCore.Qt.AlignCenter)
        self.sbCurPwd1.setMaximum(255)
        self.sbCurPwd1.setObjectName("sbCurPwd1")
        self.Log.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.WorkTime = QtWidgets.QComboBox(self.tab_3)
        self.WorkTime.setGeometry(QtCore.QRect(130, 10, 71, 31))
        self.WorkTime.setEditable(False)
        self.WorkTime.setObjectName("WorkTime")
        self.WorkTime.addItem("")
        self.WorkTime.addItem("")
        self.WorkTime.addItem("")
        self.WorkTime.addItem("")
        self.label = QtWidgets.QLabel(self.tab_3)
        self.label.setGeometry(QtCore.QRect(10, 10, 111, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.tab_3)
        self.label_2.setGeometry(QtCore.QRect(10, 50, 111, 31))
        self.label_2.setObjectName("label_2")
        self.StartFinish = QtWidgets.QComboBox(self.tab_3)
        self.StartFinish.setGeometry(QtCore.QRect(130, 50, 71, 31))
        self.StartFinish.setEditable(False)
        self.StartFinish.setObjectName("StartFinish")
        self.StartFinish.addItem("")
        self.StartFinish.addItem("")
        self.label_3 = QtWidgets.QLabel(self.tab_3)
        self.label_3.setGeometry(QtCore.QRect(10, 90, 111, 31))
        self.label_3.setObjectName("label_3")
        self.CheckInitTime = QtWidgets.QComboBox(self.tab_3)
        self.CheckInitTime.setGeometry(QtCore.QRect(130, 90, 71, 31))
        self.CheckInitTime.setEditable(False)
        self.CheckInitTime.setObjectName("CheckInitTime")
        self.CheckInitTime.addItem("")
        self.CheckInitTime.addItem("")
        self.label_5 = QtWidgets.QLabel(self.tab_3)
        self.label_5.setGeometry(QtCore.QRect(10, 130, 111, 31))
        self.label_5.setObjectName("label_5")
        self.AutoDel = QtWidgets.QComboBox(self.tab_3)
        self.AutoDel.setGeometry(QtCore.QRect(130, 130, 71, 31))
        self.AutoDel.setEditable(False)
        self.AutoDel.setObjectName("AutoDel")
        self.AutoDel.addItem("")
        self.AutoDel.addItem("")
        self.PassCard = QtWidgets.QPushButton(self.tab_3)
        self.PassCard.setGeometry(QtCore.QRect(10, 390, 191, 31))
        self.PassCard.setObjectName("PassCard")
        self.SaveSet = QtWidgets.QPushButton(self.tab_3)
        self.SaveSet.setGeometry(QtCore.QRect(110, 430, 91, 31))
        self.SaveSet.setObjectName("SaveSet")
        self.LoadSet = QtWidgets.QPushButton(self.tab_3)
        self.LoadSet.setGeometry(QtCore.QRect(10, 430, 91, 31))
        self.LoadSet.setObjectName("LoadSet")
        self.groupBox_7 = QtWidgets.QGroupBox(self.tab_3)
        self.groupBox_7.setGeometry(QtCore.QRect(10, 240, 191, 71))
        self.groupBox_7.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.groupBox_7.setObjectName("groupBox_7")
        self.sbNewPwd3 = QtWidgets.QSpinBox(self.groupBox_7)
        self.sbNewPwd3.setGeometry(QtCore.QRect(10, 30, 51, 31))
        self.sbNewPwd3.setFrame(True)
        self.sbNewPwd3.setAlignment(QtCore.Qt.AlignCenter)
        self.sbNewPwd3.setMaximum(255)
        self.sbNewPwd3.setObjectName("sbNewPwd3")
        self.sbNewPwd2 = QtWidgets.QSpinBox(self.groupBox_7)
        self.sbNewPwd2.setGeometry(QtCore.QRect(70, 30, 51, 31))
        self.sbNewPwd2.setFrame(True)
        self.sbNewPwd2.setAlignment(QtCore.Qt.AlignCenter)
        self.sbNewPwd2.setMaximum(255)
        self.sbNewPwd2.setObjectName("sbNewPwd2")
        self.sbNewPwd1 = QtWidgets.QSpinBox(self.groupBox_7)
        self.sbNewPwd1.setGeometry(QtCore.QRect(130, 30, 51, 31))
        self.sbNewPwd1.setFrame(True)
        self.sbNewPwd1.setAlignment(QtCore.Qt.AlignCenter)
        self.sbNewPwd1.setMaximum(255)
        self.sbNewPwd1.setObjectName("sbNewPwd1")
        self.groupBox_8 = QtWidgets.QGroupBox(self.tab_3)
        self.groupBox_8.setGeometry(QtCore.QRect(10, 310, 191, 71))
        self.groupBox_8.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.groupBox_8.setObjectName("groupBox_8")
        self.sbOldPwd3 = QtWidgets.QSpinBox(self.groupBox_8)
        self.sbOldPwd3.setGeometry(QtCore.QRect(10, 30, 51, 31))
        self.sbOldPwd3.setFrame(True)
        self.sbOldPwd3.setAlignment(QtCore.Qt.AlignCenter)
        self.sbOldPwd3.setMaximum(255)
        self.sbOldPwd3.setObjectName("sbOldPwd3")
        self.sbOldPwd2 = QtWidgets.QSpinBox(self.groupBox_8)
        self.sbOldPwd2.setGeometry(QtCore.QRect(70, 30, 51, 31))
        self.sbOldPwd2.setFrame(True)
        self.sbOldPwd2.setAlignment(QtCore.Qt.AlignCenter)
        self.sbOldPwd2.setMaximum(255)
        self.sbOldPwd2.setObjectName("sbOldPwd2")
        self.sbOldPwd1 = QtWidgets.QSpinBox(self.groupBox_8)
        self.sbOldPwd1.setGeometry(QtCore.QRect(130, 30, 51, 31))
        self.sbOldPwd1.setFrame(True)
        self.sbOldPwd1.setAlignment(QtCore.Qt.AlignCenter)
        self.sbOldPwd1.setMaximum(255)
        self.sbOldPwd1.setObjectName("sbOldPwd1")
        self.groupBox_9 = QtWidgets.QGroupBox(self.tab_3)
        self.groupBox_9.setGeometry(QtCore.QRect(10, 460, 191, 151))
        self.groupBox_9.setObjectName("groupBox_9")
        self.cbUartPort = QtWidgets.QComboBox(self.groupBox_9)
        self.cbUartPort.setGeometry(QtCore.QRect(120, 30, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cbUartPort.setFont(font)
        self.cbUartPort.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.cbUartPort.setObjectName("cbUartPort")
        self.cbUartPort.addItem("")
        self.cbUartPort.addItem("")
        self.cbUartPort.addItem("")
        self.cbUartPort.addItem("")
        self.cbUartPort.addItem("")
        self.cbUartPort.addItem("")
        self.cbUartPort.addItem("")
        self.cbUartPort.addItem("")
        self.cbUartPort.addItem("")
        self.cbUartPort.addItem("")
        self.cbUartPort.addItem("")
        self.cbUartPort.addItem("")
        self.cbUartPort.addItem("")
        self.cbUartPort.addItem("")
        self.cbUartPort.addItem("")
        self.cbUartPort.addItem("")
        self.cbUartPort.addItem("")
        self.cbUartPort.addItem("")
        self.cbUartPort.addItem("")
        self.cbUartPort.addItem("")
        self.cbUartPort.addItem("")
        self.cbUartPort.addItem("")
        self.cbUartPort.addItem("")
        self.cbUartPort.addItem("")
        self.cbUartPort.addItem("")
        self.cbUartPort.addItem("")
        self.cbUartPort.addItem("")
        self.cbUartPort.addItem("")
        self.cbUartPort.addItem("")
        self.cbUartPort.addItem("")
        self.cbUartPort.addItem("")
        self.cbUartPort.addItem("")
        self.label_9 = QtWidgets.QLabel(self.groupBox_9)
        self.label_9.setGeometry(QtCore.QRect(10, 30, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.label_9.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.groupBox_9)
        self.label_10.setGeometry(QtCore.QRect(10, 70, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_10.setFont(font)
        self.label_10.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.label_10.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_10.setObjectName("label_10")
        self.btnUartRead = QtWidgets.QPushButton(self.groupBox_9)
        self.btnUartRead.setGeometry(QtCore.QRect(10, 110, 81, 31))
        self.btnUartRead.setObjectName("btnUartRead")
        self.btnUartWrite = QtWidgets.QPushButton(self.groupBox_9)
        self.btnUartWrite.setGeometry(QtCore.QRect(100, 110, 81, 31))
        self.btnUartWrite.setObjectName("btnUartWrite")
        self.sbStationNumByUart = QtWidgets.QSpinBox(self.groupBox_9)
        self.sbStationNumByUart.setGeometry(QtCore.QRect(120, 70, 61, 31))
        self.sbStationNumByUart.setFrame(True)
        self.sbStationNumByUart.setAlignment(QtCore.Qt.AlignCenter)
        self.sbStationNumByUart.setMinimum(1)
        self.sbStationNumByUart.setMaximum(255)
        self.sbStationNumByUart.setObjectName("sbStationNumByUart")
        self.label_6 = QtWidgets.QLabel(self.tab_3)
        self.label_6.setGeometry(QtCore.QRect(10, 170, 111, 31))
        self.label_6.setObjectName("label_6")
        self.cbFastMark = QtWidgets.QComboBox(self.tab_3)
        self.cbFastMark.setGeometry(QtCore.QRect(130, 170, 71, 31))
        self.cbFastMark.setEditable(False)
        self.cbFastMark.setObjectName("cbFastMark")
        self.cbFastMark.addItem("")
        self.cbFastMark.addItem("")
        self.cbAntennaGain = QtWidgets.QComboBox(self.tab_3)
        self.cbAntennaGain.setGeometry(QtCore.QRect(130, 210, 71, 31))
        self.cbAntennaGain.setEditable(False)
        self.cbAntennaGain.setObjectName("cbAntennaGain")
        self.cbAntennaGain.addItem("")
        self.cbAntennaGain.addItem("")
        self.cbAntennaGain.addItem("")
        self.cbAntennaGain.addItem("")
        self.cbAntennaGain.addItem("")
        self.cbAntennaGain.addItem("")
        self.label_7 = QtWidgets.QLabel(self.tab_3)
        self.label_7.setGeometry(QtCore.QRect(10, 210, 111, 31))
        self.label_7.setObjectName("label_7")
        self.Log.addTab(self.tab_3, "")
        self.verticalLayout.addWidget(self.Log)
        self.horizontalLayout_4.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.textBrowser.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout_2.addWidget(self.textBrowser)
        self.btnClearText = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btnClearText.setFont(font)
        self.btnClearText.setObjectName("btnClearText")
        self.verticalLayout_2.addWidget(self.btnClearText)
        self.horizontalLayout_4.addLayout(self.verticalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.actionConnect = QtWidgets.QAction(MainWindow)
        self.actionConnect.setObjectName("actionConnect")
        self.actionChose_COM_port = QtWidgets.QAction(MainWindow)
        self.actionChose_COM_port.setObjectName("actionChose_COM_port")
        self.actionSave_log = QtWidgets.QAction(MainWindow)
        self.actionSave_log.setObjectName("actionSave_log")
        self.actionOpen_help_txt = QtWidgets.QAction(MainWindow)
        self.actionOpen_help_txt.setObjectName("actionOpen_help_txt")

        self.retranslateUi(MainWindow)
        self.Log.setCurrentIndex(0)
        self.cbUartPort.setCurrentIndex(0)
        self.cbAntennaGain.setCurrentIndex(5)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.Connec, self.choiseCom)
        MainWindow.setTabOrder(self.choiseCom, self.Log)
        MainWindow.setTabOrder(self.Log, self.SetTime)
        MainWindow.setTabOrder(self.SetTime, self.SetNum)
        MainWindow.setTabOrder(self.SetNum, self.SetStart)
        MainWindow.setTabOrder(self.SetStart, self.SetFinish)
        MainWindow.setTabOrder(self.SetFinish, self.ClearSt)
        MainWindow.setTabOrder(self.ClearSt, self.CheckSt)
        MainWindow.setTabOrder(self.CheckSt, self.LogCard)
        MainWindow.setTabOrder(self.LogCard, self.ReadLog)
        MainWindow.setTabOrder(self.ReadLog, self.SleepCard)
        MainWindow.setTabOrder(self.SleepCard, self.WorkTime)
        MainWindow.setTabOrder(self.WorkTime, self.StartFinish)
        MainWindow.setTabOrder(self.StartFinish, self.CheckInitTime)
        MainWindow.setTabOrder(self.CheckInitTime, self.AutoDel)
        MainWindow.setTabOrder(self.AutoDel, self.PassCard)
        MainWindow.setTabOrder(self.PassCard, self.LoadSet)
        MainWindow.setTabOrder(self.LoadSet, self.SaveSet)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "SportiduinoPQ"))
        self.Connec.setText(_translate("MainWindow", "Connect"))
        self.label_8.setText(_translate("MainWindow", "Com Port"))
        self.choiseCom.setItemText(0, _translate("MainWindow", "auto"))
        self.choiseCom.setItemText(1, _translate("MainWindow", "0"))
        self.choiseCom.setItemText(2, _translate("MainWindow", "1"))
        self.choiseCom.setItemText(3, _translate("MainWindow", "2"))
        self.choiseCom.setItemText(4, _translate("MainWindow", "3"))
        self.choiseCom.setItemText(5, _translate("MainWindow", "4"))
        self.choiseCom.setItemText(6, _translate("MainWindow", "5"))
        self.choiseCom.setItemText(7, _translate("MainWindow", "6"))
        self.choiseCom.setItemText(8, _translate("MainWindow", "7"))
        self.choiseCom.setItemText(9, _translate("MainWindow", "8"))
        self.choiseCom.setItemText(10, _translate("MainWindow", "9"))
        self.choiseCom.setItemText(11, _translate("MainWindow", "10"))
        self.choiseCom.setItemText(12, _translate("MainWindow", "11"))
        self.choiseCom.setItemText(13, _translate("MainWindow", "12"))
        self.choiseCom.setItemText(14, _translate("MainWindow", "13"))
        self.choiseCom.setItemText(15, _translate("MainWindow", "14"))
        self.choiseCom.setItemText(16, _translate("MainWindow", "15"))
        self.choiseCom.setItemText(17, _translate("MainWindow", "16"))
        self.choiseCom.setItemText(18, _translate("MainWindow", "17"))
        self.choiseCom.setItemText(19, _translate("MainWindow", "18"))
        self.choiseCom.setItemText(20, _translate("MainWindow", "19"))
        self.choiseCom.setItemText(21, _translate("MainWindow", "20"))
        self.choiseCom.setItemText(22, _translate("MainWindow", "21"))
        self.choiseCom.setItemText(23, _translate("MainWindow", "22"))
        self.choiseCom.setItemText(24, _translate("MainWindow", "23"))
        self.choiseCom.setItemText(25, _translate("MainWindow", "24"))
        self.choiseCom.setItemText(26, _translate("MainWindow", "25"))
        self.choiseCom.setItemText(27, _translate("MainWindow", "26"))
        self.choiseCom.setItemText(28, _translate("MainWindow", "27"))
        self.choiseCom.setItemText(29, _translate("MainWindow", "28"))
        self.choiseCom.setItemText(30, _translate("MainWindow", "29"))
        self.choiseCom.setItemText(31, _translate("MainWindow", "30"))
        self.choiseCom.setItemText(32, _translate("MainWindow", "31"))
        self.Print.setText(_translate("MainWindow", "Print"))
        self.SelectPrinter.setText(_translate("MainWindow", "Select Printer"))
        self.ReadCard.setToolTip(_translate("MainWindow", "Reads a participant card"))
        self.ReadCard.setText(_translate("MainWindow", "Read Card"))
        self.AutoPrint.setText(_translate("MainWindow", "AutoPrint"))
        self.InitCard.setToolTip(_translate("MainWindow", "Inits a participant card"))
        self.InitCard.setText(_translate("MainWindow", "Init Card"))
        self.AutoIncriment.setText(_translate("MainWindow", "AutoIncriment"))
        self.Log.setTabText(self.Log.indexOf(self.tab_4), _translate("MainWindow", "Main"))
        self.groupBox.setTitle(_translate("MainWindow", "Sleep Card"))
        self.SleepCard.setToolTip(_translate("MainWindow", "Creates a config card to force a base station to sleep and to wake-up at competion date"))
        self.SleepCard.setText(_translate("MainWindow", "Create"))
        self.dtCompetion.setDisplayFormat(_translate("MainWindow", "dd.MM.yyyy HH:mm"))
        self.label_4.setText(_translate("MainWindow", "Competion Date/Time"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Dump Card"))
        self.ReadLog.setToolTip(_translate("MainWindow", "Reads a config card consists dump info"))
        self.ReadLog.setText(_translate("MainWindow", "Read"))
        self.LogCard.setToolTip(_translate("MainWindow", "Creates a config card to read dump from a base station"))
        self.LogCard.setText(_translate("MainWindow", "Create"))
        self.groupBox_3.setTitle(_translate("MainWindow", "StationNum Card"))
        self.SetNum.setToolTip(_translate("MainWindow", "Creates a config card to set a number for a base station"))
        self.SetNum.setText(_translate("MainWindow", "Set Num"))
        self.SetStart.setToolTip(_translate("MainWindow", "Creates a config card to make a base station as a start station"))
        self.SetStart.setText(_translate("MainWindow", "Set Start"))
        self.SetFinish.setToolTip(_translate("MainWindow", "Creates a config card to make a base station as a finish station"))
        self.SetFinish.setText(_translate("MainWindow", "Set Finish"))
        self.CheckSt.setToolTip(_translate("MainWindow", "Creates a config card to make a base station as a check station"))
        self.CheckSt.setText(_translate("MainWindow", "Check St"))
        self.ClearSt.setToolTip(_translate("MainWindow", "Creates a config card to make a base station as a clear station"))
        self.ClearSt.setText(_translate("MainWindow", "Clear St"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Date/Time Card"))
        self.SetTime.setToolTip(_translate("MainWindow", "Creates a config card to set date/time for a base station"))
        self.SetTime.setText(_translate("MainWindow", "Create"))
        self.groupBox_5.setTitle(_translate("MainWindow", "GetInfo Card"))
        self.btnCreateInfoCard.setToolTip(_translate("MainWindow", "Creates a config card to get info about a base station"))
        self.btnCreateInfoCard.setText(_translate("MainWindow", "Create"))
        self.btnReadInfo.setToolTip(_translate("MainWindow", "Creates a config card to get info about a base station"))
        self.btnReadInfo.setText(_translate("MainWindow", "Read"))
        self.groupBox_6.setToolTip(_translate("MainWindow", "Current password of a base station"))
        self.groupBox_6.setTitle(_translate("MainWindow", "Password"))
        self.btnApplyPwd.setToolTip(_translate("MainWindow", "Applies current password for all next config cards"))
        self.btnApplyPwd.setText(_translate("MainWindow", "Apply"))
        self.Log.setTabText(self.Log.indexOf(self.tab_2), _translate("MainWindow", "Settings#1"))
        self.WorkTime.setItemText(0, _translate("MainWindow", "6 hour"))
        self.WorkTime.setItemText(1, _translate("MainWindow", "24 hour"))
        self.WorkTime.setItemText(2, _translate("MainWindow", "not work"))
        self.WorkTime.setItemText(3, _translate("MainWindow", "all time"))
        self.label.setText(_translate("MainWindow", "Work Time"))
        self.label_2.setText(_translate("MainWindow", "Start / Finish"))
        self.StartFinish.setItemText(0, _translate("MainWindow", "off"))
        self.StartFinish.setItemText(1, _translate("MainWindow", "on"))
        self.label_3.setText(_translate("MainWindow", "Check InitTime"))
        self.CheckInitTime.setItemText(0, _translate("MainWindow", "off"))
        self.CheckInitTime.setItemText(1, _translate("MainWindow", "on"))
        self.label_5.setText(_translate("MainWindow", "AutoDel Set"))
        self.AutoDel.setItemText(0, _translate("MainWindow", "off"))
        self.AutoDel.setItemText(1, _translate("MainWindow", "on"))
        self.PassCard.setToolTip(_translate("MainWindow", "Creates a config card to change password and settings for a base station"))
        self.PassCard.setText(_translate("MainWindow", " Create Pwd Card"))
        self.SaveSet.setToolTip(_translate("MainWindow", "Stores settings to a file"))
        self.SaveSet.setText(_translate("MainWindow", "Save Set"))
        self.LoadSet.setToolTip(_translate("MainWindow", "Loads settings from a file"))
        self.LoadSet.setText(_translate("MainWindow", "Load Set"))
        self.groupBox_7.setToolTip(_translate("MainWindow", "New password for a base station"))
        self.groupBox_7.setTitle(_translate("MainWindow", "New Password"))
        self.groupBox_8.setToolTip(_translate("MainWindow", "Old password of a base station"))
        self.groupBox_8.setTitle(_translate("MainWindow", "Old Password"))
        self.groupBox_9.setTitle(_translate("MainWindow", "Config by UART"))
        self.cbUartPort.setCurrentText(_translate("MainWindow", "0"))
        self.cbUartPort.setItemText(0, _translate("MainWindow", "0"))
        self.cbUartPort.setItemText(1, _translate("MainWindow", "1"))
        self.cbUartPort.setItemText(2, _translate("MainWindow", "2"))
        self.cbUartPort.setItemText(3, _translate("MainWindow", "3"))
        self.cbUartPort.setItemText(4, _translate("MainWindow", "4"))
        self.cbUartPort.setItemText(5, _translate("MainWindow", "5"))
        self.cbUartPort.setItemText(6, _translate("MainWindow", "6"))
        self.cbUartPort.setItemText(7, _translate("MainWindow", "7"))
        self.cbUartPort.setItemText(8, _translate("MainWindow", "8"))
        self.cbUartPort.setItemText(9, _translate("MainWindow", "9"))
        self.cbUartPort.setItemText(10, _translate("MainWindow", "10"))
        self.cbUartPort.setItemText(11, _translate("MainWindow", "11"))
        self.cbUartPort.setItemText(12, _translate("MainWindow", "12"))
        self.cbUartPort.setItemText(13, _translate("MainWindow", "13"))
        self.cbUartPort.setItemText(14, _translate("MainWindow", "14"))
        self.cbUartPort.setItemText(15, _translate("MainWindow", "15"))
        self.cbUartPort.setItemText(16, _translate("MainWindow", "16"))
        self.cbUartPort.setItemText(17, _translate("MainWindow", "17"))
        self.cbUartPort.setItemText(18, _translate("MainWindow", "18"))
        self.cbUartPort.setItemText(19, _translate("MainWindow", "19"))
        self.cbUartPort.setItemText(20, _translate("MainWindow", "20"))
        self.cbUartPort.setItemText(21, _translate("MainWindow", "21"))
        self.cbUartPort.setItemText(22, _translate("MainWindow", "22"))
        self.cbUartPort.setItemText(23, _translate("MainWindow", "23"))
        self.cbUartPort.setItemText(24, _translate("MainWindow", "24"))
        self.cbUartPort.setItemText(25, _translate("MainWindow", "25"))
        self.cbUartPort.setItemText(26, _translate("MainWindow", "26"))
        self.cbUartPort.setItemText(27, _translate("MainWindow", "27"))
        self.cbUartPort.setItemText(28, _translate("MainWindow", "28"))
        self.cbUartPort.setItemText(29, _translate("MainWindow", "29"))
        self.cbUartPort.setItemText(30, _translate("MainWindow", "30"))
        self.cbUartPort.setItemText(31, _translate("MainWindow", "31"))
        self.label_9.setText(_translate("MainWindow", "Com Port"))
        self.label_10.setText(_translate("MainWindow", "Station Num"))
        self.btnUartRead.setToolTip(_translate("MainWindow", "Reads settings of a base station by UART"))
        self.btnUartRead.setText(_translate("MainWindow", "Read"))
        self.btnUartWrite.setToolTip(_translate("MainWindow", "Writes settings to a base station by UART"))
        self.btnUartWrite.setText(_translate("MainWindow", "Write"))
        self.label_6.setText(_translate("MainWindow", "Fast Mark"))
        self.cbFastMark.setItemText(0, _translate("MainWindow", "off"))
        self.cbFastMark.setItemText(1, _translate("MainWindow", "on"))
        self.cbAntennaGain.setItemText(0, _translate("MainWindow", "18 dB"))
        self.cbAntennaGain.setItemText(1, _translate("MainWindow", "23 dB"))
        self.cbAntennaGain.setItemText(2, _translate("MainWindow", "33 dB"))
        self.cbAntennaGain.setItemText(3, _translate("MainWindow", "38 dB"))
        self.cbAntennaGain.setItemText(4, _translate("MainWindow", "43 dB"))
        self.cbAntennaGain.setItemText(5, _translate("MainWindow", "48 dB"))
        self.label_7.setText(_translate("MainWindow", "Antenna Gain"))
        self.Log.setTabText(self.Log.indexOf(self.tab_3), _translate("MainWindow", "Settings#2"))
        self.btnClearText.setText(_translate("MainWindow", "Clear"))
        self.actionConnect.setText(_translate("MainWindow", "Connect"))
        self.actionChose_COM_port.setText(_translate("MainWindow", "Chose COM-port"))
        self.actionSave_log.setText(_translate("MainWindow", "Save log"))
        self.actionOpen_help_txt.setText(_translate("MainWindow", "Open help.txt"))

