# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitledZFgfRN.ui'
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
        # MainWindow.resize(1335, 795)
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


        self.horizontalLayout_3.addWidget(self.widget_4, 0, Qt.AlignLeft|Qt.AlignTop)

        self.widget_5 = QWidget(self.widget_2)
        self.widget_5.setObjectName(u"widget_5")
        sizePolicy.setHeightForWidth(self.widget_5.sizePolicy().hasHeightForWidth())
        self.widget_5.setSizePolicy(sizePolicy)
        self.horizontalLayout_4 = QHBoxLayout(self.widget_5)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_2 = QLabel(self.widget_5)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_4.addWidget(self.label_2)


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
        self.label.setText(QCoreApplication.translate("MainWindow", u"CAR", None))
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
        self.label_2.setText("")
    # retranslateUi

