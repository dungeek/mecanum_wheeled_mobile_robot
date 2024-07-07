#!/usr/bin/env python3
import sys
from PySide2.QtCore import (QThread,Signal,QObject)
from ui_untitled import Ui_MainWindow
from event_custom import event_custom
from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtWidgets import QShortcut
import time
class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        # self.showFullScreen()
        self.show()
        self.events=event_custom(self)
        self.source='http://192.168.0.108/cam-mid.jpg'
        self.model='yolov8l.pt'
        self.baudratesDIC = {
        '1200':1200,
        '2400':2400,
        '4800':4800,
        '9600':9600,
        '19200':19200,
        '38400':38400,
        '57600':57600,
        '115200':115200
        }
        self.ui.comboBox_2.addItems(self.baudratesDIC.keys())
        self.ui.comboBox_2.setCurrentText('9600')
        self.ui.pushButton_3.clicked.connect(self.Close)
        self.ui.pushButton_2.clicked.connect(self.maximize_restore)
        self.ui.pushButton.clicked.connect(lambda: self.showMinimized())
        self.events.update_ports(self.ui.comboBox)
        self.ui.pushButton_5.clicked.connect(self.update_ports)
        self.ui.pushButton_4.clicked.connect(self.connect_ports)
        self.ui.pushButton_6.clicked.connect(self.events.manual_mode)
        self.ui.pushButton_7.clicked.connect(self.events.auto)
        self.ui.pushButton_9.clicked.connect(self.events.tracking)
        self.ui.pushButton_19.clicked.connect(self.events.move_around)
        self.ui.verticalSlider.valueChanged.connect(self.speed_change)
        self.ui.pushButton_21.clicked.connect(self.events.follow_wall)
        self.mode='0'
        self.run_camera()
        self.resize()
        self.timer=time.time()


        def moveWindow(event):
            if event.buttons() == Qt.LeftButton:
                self.ui.pushButton_2.setChecked(True)
                self.showNormal()
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()
        self.ui.widget.mouseMoveEvent = moveWindow
    def mousePressEvent(self,event):
        self.dragPos =event.globalPos()
    def keyPressEvent(self, event):
        self.key_text = event.text()
        self.events.read_direction(self.key_text)
        if self.key_text=='4':
            self.events.car_stop()
    def Close(self):
        self.events.Close()
    def resize(self):
        self.events.resize(self.ui.frame)
    def maximize_restore(self):
        self.events.maximize_restore(self.ui.pushButton_2)
    def update_ports(self):
        self.events.update_ports(self.ui.comboBox)
    def connect_ports(self):
        port = self.ui.comboBox.currentText()
        baud = self.ui.comboBox_2.currentText()
        self.events.connect_ports(port, baud,self.ui.pushButton_4)
    def run_camera(self):
        self.events.run_camera(self.source,self.model,self.ui.label_2)
    def speed_change(self):
        self.events.car_speed(self.ui.verticalSlider.value())
        self.ui.label_3.setText(str(self.ui.verticalSlider.value()))
if __name__ == "__main__":
    app=QApplication(sys.argv)
    window=MainWindow()
    sys.exit(app.exec_())
