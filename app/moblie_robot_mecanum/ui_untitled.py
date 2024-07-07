# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitledSEPQqW.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        # MainWindow.resize(1050, 589)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"QWidget{\n"
"	border-radius:15px;\n"
"	background-color:#040f13;\n"
"}\n"
"QPushButton{\n"
"	background-color:#071e26;\n"
"	border-radius:5px;\n"
"}\n"
"QPushButton:hover{\n"
"        background-color:#040f13;\n"
"}\n"
"QPushButton:pressed{\n"
"        padding-left:5px;\n"
"        padding-top:5px;\n"
"        background-color:rgba(105,118,132,200);\n"
"}\n"
"QComboBox{\n"
"        padding:10px;\n"
"        background-color:#071e26;\n"
"        border-radius:5px;\n"
"        color:white;\n"
"}\n"
"QComboBox QListView{\n"
"        background-color:#040f13;\n"
"        border:1px solid rgba(0,0,0,10%);\n"
"}\n"
"QComboBox::drop-down{\n"
"        border:0px;\n"
"}\n"
"*{color:white}")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label, 0, Qt.AlignTop)

        self.widget_3 = QWidget(self.widget)
        self.widget_3.setObjectName(u"widget_3")
        self.horizontalLayout_2 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.pushButton = QPushButton(self.widget_3)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMaximumSize(QSize(16, 16))
        self.pushButton.setStyleSheet(u"QPushButton{\n"
"	border:none;\n"
"	border-radius:8px;\n"
"	background-color:rgb(255,170,0);\n"
"}\n"
"QPushButton:hover{\n"
"	background-color:rgba(255,170,0,150);\n"
"}")
        self.pushButton.setCheckable(True)

        self.horizontalLayout_2.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.widget_3)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMaximumSize(QSize(16, 16))
        self.pushButton_2.setStyleSheet(u"QPushButton{\n"
"	border:none;\n"
"	border-radius:8px;\n"
"	background-color:rgb(85,255,127);\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"QPushButton:hover{\n"
"	background-color:rgba(85,255,127,150);\n"
"}")
        self.pushButton_2.setCheckable(True)

        self.horizontalLayout_2.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.widget_3)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMaximumSize(QSize(16, 16))
        self.pushButton_3.setStyleSheet(u"QPushButton{\n"
"	border:none;\n"
"	border-radius:8px;\n"
"	background-color:rgb(255,0,0);\n"
"}\n"
"QPushButton:hover{\n"
"	background-color:rgba(255,0,0,150);\n"
"}")
        self.pushButton_3.setCheckable(True)

        self.horizontalLayout_2.addWidget(self.pushButton_3)


        self.horizontalLayout.addWidget(self.widget_3, 0, Qt.AlignRight)


        self.verticalLayout.addWidget(self.widget)

        self.widget_7 = QWidget(self.centralwidget)
        self.widget_7.setObjectName(u"widget_7")
        self.widget_7.setMinimumSize(QSize(70, 70))
        self.horizontalLayout_7 = QHBoxLayout(self.widget_7)
        self.horizontalLayout_7.setSpacing(11)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(11, 0, 0, 0)
        self.pushButton_4 = QPushButton(self.widget_7)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setMinimumSize(QSize(100, 50))
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(True)
        font1.setWeight(75)
        self.pushButton_4.setFont(font1)
        self.pushButton_4.setCheckable(True)

        self.horizontalLayout_7.addWidget(self.pushButton_4)

        self.pushButton_5 = QPushButton(self.widget_7)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setMinimumSize(QSize(100, 50))
        self.pushButton_5.setFont(font1)
        self.pushButton_5.setCheckable(True)

        self.horizontalLayout_7.addWidget(self.pushButton_5)

        self.label_5 = QLabel(self.widget_7)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(100, 50))
        self.label_5.setFont(font1)
        self.label_5.setStyleSheet(u"background-color:none")
        self.label_5.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_7.addWidget(self.label_5)

        self.comboBox = QComboBox(self.widget_7)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setMinimumSize(QSize(100, 50))
        font2 = QFont()
        font2.setPointSize(12)
        self.comboBox.setFont(font2)

        self.horizontalLayout_7.addWidget(self.comboBox)

        self.label_6 = QLabel(self.widget_7)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font1)
        self.label_6.setStyleSheet(u"background-color:none")
        self.label_6.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_7.addWidget(self.label_6)

        self.comboBox_2 = QComboBox(self.widget_7)
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setMinimumSize(QSize(100, 50))
        self.comboBox_2.setFont(font2)

        self.horizontalLayout_7.addWidget(self.comboBox_2)


        self.verticalLayout.addWidget(self.widget_7, 0, Qt.AlignLeft)

        self.widget_2 = QWidget(self.centralwidget)
        self.widget_2.setObjectName(u"widget_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy1)
        self.horizontalLayout_3 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.widget_4 = QWidget(self.widget_2)
        self.widget_4.setObjectName(u"widget_4")
        self.verticalLayout_2 = QVBoxLayout(self.widget_4)
        self.verticalLayout_2.setSpacing(11)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.pushButton_6 = QPushButton(self.widget_4)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setMinimumSize(QSize(100, 50))
        font3 = QFont()
        font3.setPointSize(11)
        self.pushButton_6.setFont(font3)
        self.pushButton_6.setCheckable(True)

        self.verticalLayout_2.addWidget(self.pushButton_6)

        self.pushButton_7 = QPushButton(self.widget_4)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setMinimumSize(QSize(100, 50))
        self.pushButton_7.setFont(font3)
        self.pushButton_7.setCheckable(True)

        self.verticalLayout_2.addWidget(self.pushButton_7)

        self.pushButton_9 = QPushButton(self.widget_4)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setMinimumSize(QSize(100, 50))
        self.pushButton_9.setFont(font3)
        self.pushButton_9.setCheckable(True)

        self.verticalLayout_2.addWidget(self.pushButton_9)

        self.pushButton_19 = QPushButton(self.widget_4)
        self.pushButton_19.setObjectName(u"pushButton_19")
        self.pushButton_19.setMinimumSize(QSize(0, 50))
        self.pushButton_19.setFont(font3)

        self.verticalLayout_2.addWidget(self.pushButton_19)

        self.pushButton_21 = QPushButton(self.widget_4)
        self.pushButton_21.setObjectName(u"pushButton_21")
        self.pushButton_21.setMinimumSize(QSize(0, 50))
        self.pushButton_21.setFont(font3)

        self.verticalLayout_2.addWidget(self.pushButton_21)


        self.horizontalLayout_3.addWidget(self.widget_4, 0, Qt.AlignLeft|Qt.AlignTop)

        self.widget_5 = QWidget(self.widget_2)
        self.widget_5.setObjectName(u"widget_5")
        sizePolicy.setHeightForWidth(self.widget_5.sizePolicy().hasHeightForWidth())
        self.widget_5.setSizePolicy(sizePolicy)
        self.horizontalLayout_4 = QHBoxLayout(self.widget_5)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_2 = QLabel(self.widget_5)
        self.label_2.setObjectName(u"label_2")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy2)

        self.horizontalLayout_4.addWidget(self.label_2)

        self.widget_6 = QWidget(self.widget_5)
        self.widget_6.setObjectName(u"widget_6")
        self.horizontalLayout_5 = QHBoxLayout(self.widget_6)
        self.horizontalLayout_5.setSpacing(20)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.widget_8 = QWidget(self.widget_6)
        self.widget_8.setObjectName(u"widget_8")
        self.verticalLayout_4 = QVBoxLayout(self.widget_8)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.widget_10 = QWidget(self.widget_8)
        self.widget_10.setObjectName(u"widget_10")
        self.horizontalLayout_6 = QHBoxLayout(self.widget_10)
        self.horizontalLayout_6.setSpacing(10)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.widget_12 = QWidget(self.widget_10)
        self.widget_12.setObjectName(u"widget_12")
        self.verticalLayout_5 = QVBoxLayout(self.widget_12)
        self.verticalLayout_5.setSpacing(10)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.pushButton_8 = QPushButton(self.widget_12)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setMinimumSize(QSize(50, 50))
        icon = QIcon()
        icon.addFile(u"icons/arrow-up-left.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_8.setIcon(icon)
        self.pushButton_8.setIconSize(QSize(50, 50))

        self.verticalLayout_5.addWidget(self.pushButton_8)

        self.pushButton_10 = QPushButton(self.widget_12)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setMinimumSize(QSize(50, 50))
        icon1 = QIcon()
        icon1.addFile(u"icons/arrow-left.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_10.setIcon(icon1)
        self.pushButton_10.setIconSize(QSize(50, 50))

        self.verticalLayout_5.addWidget(self.pushButton_10)

        self.pushButton_11 = QPushButton(self.widget_12)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setMinimumSize(QSize(50, 50))
        icon2 = QIcon()
        icon2.addFile(u"icons/arrow-down-left.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_11.setIcon(icon2)
        self.pushButton_11.setIconSize(QSize(50, 50))

        self.verticalLayout_5.addWidget(self.pushButton_11)


        self.horizontalLayout_6.addWidget(self.widget_12)

        self.widget_13 = QWidget(self.widget_10)
        self.widget_13.setObjectName(u"widget_13")
        self.verticalLayout_6 = QVBoxLayout(self.widget_13)
        self.verticalLayout_6.setSpacing(10)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.pushButton_12 = QPushButton(self.widget_13)
        self.pushButton_12.setObjectName(u"pushButton_12")
        self.pushButton_12.setMinimumSize(QSize(50, 50))
        icon3 = QIcon()
        icon3.addFile(u"icons/arrow-up.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_12.setIcon(icon3)
        self.pushButton_12.setIconSize(QSize(50, 50))

        self.verticalLayout_6.addWidget(self.pushButton_12)

        self.pushButton_13 = QPushButton(self.widget_13)
        self.pushButton_13.setObjectName(u"pushButton_13")
        self.pushButton_13.setMinimumSize(QSize(50, 50))
        icon4 = QIcon()
        icon4.addFile(u"icons/zap-off.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_13.setIcon(icon4)
        self.pushButton_13.setIconSize(QSize(50, 50))

        self.verticalLayout_6.addWidget(self.pushButton_13)

        self.pushButton_14 = QPushButton(self.widget_13)
        self.pushButton_14.setObjectName(u"pushButton_14")
        self.pushButton_14.setMinimumSize(QSize(50, 50))
        icon5 = QIcon()
        icon5.addFile(u"icons/arrow-down.svg", QSize(), QIcon.Selected, QIcon.On)
        self.pushButton_14.setIcon(icon5)
        self.pushButton_14.setIconSize(QSize(50, 50))

        self.verticalLayout_6.addWidget(self.pushButton_14)


        self.horizontalLayout_6.addWidget(self.widget_13)

        self.widget_14 = QWidget(self.widget_10)
        self.widget_14.setObjectName(u"widget_14")
        self.verticalLayout_7 = QVBoxLayout(self.widget_14)
        self.verticalLayout_7.setSpacing(10)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.pushButton_15 = QPushButton(self.widget_14)
        self.pushButton_15.setObjectName(u"pushButton_15")
        self.pushButton_15.setMinimumSize(QSize(50, 50))
        icon6 = QIcon()
        icon6.addFile(u"icons/arrow-up-right.svg", QSize(), QIcon.Normal, QIcon.On)
        self.pushButton_15.setIcon(icon6)
        self.pushButton_15.setIconSize(QSize(50, 50))

        self.verticalLayout_7.addWidget(self.pushButton_15)

        self.pushButton_16 = QPushButton(self.widget_14)
        self.pushButton_16.setObjectName(u"pushButton_16")
        self.pushButton_16.setMinimumSize(QSize(50, 50))
        icon7 = QIcon()
        icon7.addFile(u"icons/arrow-right.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_16.setIcon(icon7)
        self.pushButton_16.setIconSize(QSize(50, 50))

        self.verticalLayout_7.addWidget(self.pushButton_16)

        self.pushButton_17 = QPushButton(self.widget_14)
        self.pushButton_17.setObjectName(u"pushButton_17")
        self.pushButton_17.setMinimumSize(QSize(50, 50))
        icon8 = QIcon()
        icon8.addFile(u"icons/arrow-down-right.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_17.setIcon(icon8)
        self.pushButton_17.setIconSize(QSize(50, 50))

        self.verticalLayout_7.addWidget(self.pushButton_17)


        self.horizontalLayout_6.addWidget(self.widget_14)


        self.verticalLayout_4.addWidget(self.widget_10, 0, Qt.AlignVCenter)

        self.widget_11 = QWidget(self.widget_8)
        self.widget_11.setObjectName(u"widget_11")
        self.horizontalLayout_8 = QHBoxLayout(self.widget_11)
        self.horizontalLayout_8.setSpacing(10)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.widget_15 = QWidget(self.widget_11)
        self.widget_15.setObjectName(u"widget_15")
        self.verticalLayout_8 = QVBoxLayout(self.widget_15)
        self.verticalLayout_8.setSpacing(10)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.pushButton_18 = QPushButton(self.widget_15)
        self.pushButton_18.setObjectName(u"pushButton_18")
        self.pushButton_18.setMinimumSize(QSize(50, 50))
        icon9 = QIcon()
        icon9.addFile(u"icons/rotate-ccw.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_18.setIcon(icon9)
        self.pushButton_18.setIconSize(QSize(50, 50))

        self.verticalLayout_8.addWidget(self.pushButton_18)


        self.horizontalLayout_8.addWidget(self.widget_15)

        self.widget_16 = QWidget(self.widget_11)
        self.widget_16.setObjectName(u"widget_16")
        self.verticalLayout_9 = QVBoxLayout(self.widget_16)
        self.verticalLayout_9.setSpacing(10)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.pushButton_20 = QPushButton(self.widget_16)
        self.pushButton_20.setObjectName(u"pushButton_20")
        self.pushButton_20.setMinimumSize(QSize(50, 50))
        icon10 = QIcon()
        icon10.addFile(u"icons/rotate-cw.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_20.setIcon(icon10)
        self.pushButton_20.setIconSize(QSize(50, 50))

        self.verticalLayout_9.addWidget(self.pushButton_20)


        self.horizontalLayout_8.addWidget(self.widget_16)


        self.verticalLayout_4.addWidget(self.widget_11, 0, Qt.AlignTop)

        self.widget_17 = QWidget(self.widget_8)
        self.widget_17.setObjectName(u"widget_17")
        self.verticalLayout_10 = QVBoxLayout(self.widget_17)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_4 = QLabel(self.widget_17)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font3)

        self.verticalLayout_10.addWidget(self.label_4)

        self.label_7 = QLabel(self.widget_17)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font3)

        self.verticalLayout_10.addWidget(self.label_7)

        self.label_8 = QLabel(self.widget_17)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font3)

        self.verticalLayout_10.addWidget(self.label_8)


        self.verticalLayout_4.addWidget(self.widget_17)


        self.horizontalLayout_5.addWidget(self.widget_8)

        self.widget_9 = QWidget(self.widget_6)
        self.widget_9.setObjectName(u"widget_9")
        self.verticalLayout_3 = QVBoxLayout(self.widget_9)
        self.verticalLayout_3.setSpacing(10)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalSlider = QSlider(self.widget_9)
        self.verticalSlider.setObjectName(u"verticalSlider")
        self.verticalSlider.setStyleSheet(u"QSlider::groove:verticall{\n"
"	border-radius: 8px;\n"
"	width: 20px;\n"
"	background-color: rgb(7, 30, 38);\n"
"}\n"
"QSlider::groove:verticall:hover{\n"
"	background-color: rgb(55,62,76);\n"
"}\n"
"QSlider::handle:verticall{\n"
"	height: 20px;\n"
"	border-radius: 10px;\n"
"	background-color: rgb(0, 122, 217);\n"
"}\n"
"QSlider::handle:verticall:hover{\n"
"	background-color: rgb(255, 170, 0);\n"
"}\n"
"QSlider::handle:verticall:pressed{\n"
"	background-color: rgb(255, 170, 0);\n"
"}")
        self.verticalSlider.setMaximum(10)
        self.verticalSlider.setOrientation(Qt.Vertical)

        self.verticalLayout_3.addWidget(self.verticalSlider)

        self.label_3 = QLabel(self.widget_9)
        self.label_3.setObjectName(u"label_3")
        font4 = QFont()
        font4.setPointSize(15)
        self.label_3.setFont(font4)

        self.verticalLayout_3.addWidget(self.label_3, 0, Qt.AlignHCenter)


        self.horizontalLayout_5.addWidget(self.widget_9)


        self.horizontalLayout_4.addWidget(self.widget_6, 0, Qt.AlignRight)


        self.horizontalLayout_3.addWidget(self.widget_5)


        self.verticalLayout.addWidget(self.widget_2)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(10, 10))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)

        self.verticalLayout.addWidget(self.frame, 0, Qt.AlignRight)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"MECANUM MOBILE ROBOT", None))
        self.pushButton.setText("")
        self.pushButton_2.setText("")
        self.pushButton_3.setText("")
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"CONNECT", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"UPDATE", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"PORT:", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"BAUDRATE:", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"MANUAL", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"AUTO", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"TRACKING", None))
        self.pushButton_19.setText(QCoreApplication.translate("MainWindow", u"MOVE AROUND", None))
        self.pushButton_21.setText(QCoreApplication.translate("MainWindow", u"FOLLOW WALL", None))
        self.label_2.setText("")
        self.pushButton_8.setText("")
        self.pushButton_10.setText("")
        self.pushButton_11.setText("")
        self.pushButton_12.setText("")
        self.pushButton_13.setText("")
        self.pushButton_14.setText("")
        self.pushButton_15.setText("")
        self.pushButton_16.setText("")
        self.pushButton_17.setText("")
        self.pushButton_18.setText("")
        self.pushButton_20.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Left:", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Right:", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Distance:", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"0", None))
    # retranslateUi

