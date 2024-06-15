#!/usr/bin/env python3
import sys
from PySide2.QtCore import (QThread,Signal,QObject)
# from PySide2.QtGui import(QPixmap)
from PySide2 import QtCore,QtGui,QtWidgets
from PyQt5.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from ui_untitled import Ui_MainWindow
import serial
import numpy as np
import cv2
import serial, serial.tools.list_ports
from threading import Thread
from ultralytics import YOLO
import urllib.request
from PyQt5.QtGui import QKeyEvent

image=None
class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.showFullScreen()
        self.ui.pushButton_2.clicked.connect(self.maximize_restore)
        self.ui.pushButton_3.clicked.connect(self.close)
        self.ui.pushButton.clicked.connect(lambda: self.showMinimized())
        self.ui.pushButton_4.clicked.connect(self.connect)
        self.ui.pushButton_5.clicked.connect(self.update_ports)
        self.show()
        self.source="http://192.168.0.105/cam-mid.jpg "
        self.model="yolov8l.pt"
        # self.yolov8()
        self.resize()

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
        self.update_ports()
        self.ui.comboBox_2.addItems(self.baudratesDIC.keys())
        self.ui.comboBox_2.setCurrentText('9600')


        def moveWindow(event):
            if event.buttons() == Qt.LeftButton:
                self.ui.pushButton_2.setChecked(True)
                self.showNormal()
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()
        self.ui.widget.mouseMoveEvent = moveWindow

    def keyPressEvent(self, event):
        key_text = event.text()
        print(key_text)

    def show_webcam(self, cv_img,label):
        qt_img = self.convert_cv_qt(cv_img,label)
        label.setPixmap(qt_img)

    def convert_cv_qt(self, cv_img,label):
        rgb_image = cv2.cvtColor(cv_img, cv2.COLOR_BGR2RGB)
        h, w, ch = rgb_image.shape
        bytes_per_line = ch * w
        convert_to_Qt_format = QtGui.QImage(rgb_image.data, w, h, bytes_per_line, QtGui.QImage.Format_RGB888)
        p = convert_to_Qt_format.scaled(label.geometry().width(), label.geometry().height(), Qt.KeepAspectRatio)
        return QPixmap.fromImage(p)

    def mousePressEvent(self,event):
        self.dragPos =event.globalPos()

    def maximize_restore(self):
        if self.ui.pushButton_2.isChecked()==False:
            self.showMaximized()
            self.ui.pushButton_2.setToolTip("Restore")
        else:
            self.showNormal()
            self.ui.pushButton_2.setToolTip("Maximize")

    def resize(self):
        self.sizegrip = QSizeGrip(self.ui.frame)
        self.sizegrip.setStyleSheet("QSizeGrip { width: 10px; height: 10px; margin: 5px} QSizeGrip:hover { background-color: rgb(50, 42, 94)}")
        self.sizegrip.setToolTip("Resize Window")
    


        # Temperature vs time dynamic plot

    def update_ports(self):
        self.portlist = [port.device for port in serial.tools.list_ports.comports()]
        self.ui.comboBox.clear()
        self.ui.comboBox.addItems(self.portlist)

    def connect(self):
        if(self.ui.pushButton_4.isChecked()):
            port = self.ui.comboBox.currentText()
            baud = self.ui.comboBox_2.currentText()
            self.serial_thread = SerialThread(port,baud)
            self.serial_thread.data_received.connect(self.update_terminal)
            self.serial_thread.start()

            if(self.serial_thread.serial_port.is_open):
                self.ui.pushButton_4.setText('DISCONNECT')
            else:
                self.ui.pushButton_4.setChecked(False)
        else:
            if(self.serial_thread.serial_port.is_open):
                self.serial_thread.serial_port.close()
                self.serial_thread.quit()
                self.serial_thread = None
                self.ui.pushButton_4.setText('CONNECT')

    def yolov8(self):
        self.yolov8_thread = yolov8(self.source,self.model)
        self.yolov8_thread.data_received.connect(self.update_image)
        self.yolov8_thread.start()

    def update_image(self,point):
        global image
        self.show_webcam(image,self.ui.label_2)




class SerialThread(QThread, QObject):
    data_received = Signal(str)

    def __init__(self, port,baud):
        super().__init__()
        try:
            self.serial_port = serial.Serial(port, baud)
        except:
            pass
        self.data=''

    def run(self):
        while True:
            try:
                if self.serial_port.in_waiting > 0:
                    self.data = self.serial_port.readline().decode()
                    self.data_received.emit(self.data)
            except:
                break
    def write_data(self, data):
        self.serial_port.write(data.encode())

class yolov8(QThread, QObject):
    data_received = Signal(str)
    def __init__(self,source,model_name):
        super().__init__()
        self.data=''
        self.source=source
        self.model_name=model_name
    def open_camera(self,capture):  #kết nối camera
        cap = cv2.VideoCapture(capture)
        return cap

    def load_model(self,model_name):  # load model yolo
        model = YOLO(model_name)
        class_name = model.names
        return model, class_name

    def results_process(self,class_name, results, frame,ser=None):  #xử lý tọa độ vật thể
        boxes = results[0].boxes.cpu().numpy()
        class_id = boxes.cls
        conf = boxes.conf
        xyxy = boxes.xyxy
        count = 0
        point = np.array((0, 0, 0, 0))
        for id in class_id:
            name = class_name[id]
            conf_class = conf[count]
            xyxy_class = xyxy[count]
            if conf_class>0.5:
                frame, point = self.call_drawing(name, conf_class, xyxy_class, frame)
                count+=1
                cx = (point[0]+point[2])/2
        return frame, point

    def call_drawing(self,name, conf_class, xyxy_class, frame):  # fomat tọa độ và chữ
        conf_class = "{:.2f}".format(conf_class)
        text = str(name) + " " + str(conf_class)
        frame = self.drawing_box(frame, text, xyxy_class)
        return frame, xyxy_class

    def drawing_box(self,frame, text, xyxy):  # vẽ box và vã text
        font = cv2.FONT_HERSHEY_SIMPLEX
        color = (0, 0, 255)
        thickness = 2
        font_scale = 1
        x1, y1 = int(xyxy[0]), int(xyxy[1])
        x2, y2 = int(xyxy[2]), int(xyxy[3])
        cx = int((x1+x2)/2)
        cy = int((y1+y2)/2)
        # print(cx,cy)
        start_point = (x1, y1)
        end_point = (x2, y2)
        text_size,_ = cv2.getTextSize(text, font, font_scale, thickness)
        text_w, text_h = text_size
        cv2.rectangle(frame,(x1, y1 - text_h - 4),(x1 + text_w, y1),color, -1)
        cv2.rectangle(frame,start_point, end_point, color, thickness)
        cv2.putText(frame, text, (x1, y1 - 2), font, font_scale, (255, 255, 255),thickness)
        cv2.circle(frame, (cx, cy), 5, color, -1) 
        return frame

    def run(self): # hàm chính
        global image
        cap = self.open_camera(self.source)
        model, class_name = self.load_model(self.model_name)
        while True:
            try :
                if source >= 0:
                    _, frame = cap.read()
            except: 
                img_resp = urllib.request.urlopen(self.source)
                imgnp = np.array(bytearray(img_resp.read()),dtype=np.uint8)
                frame = cv2.imdecode(imgnp,-1)
            results = model(frame)  
            frame, point = self.results_process(class_name, results, frame)
            image=frame
            self.data_received.emit(self.data)

if __name__ == "__main__":
    app=QApplication(sys.argv)
    window=MainWindow()
    sys.exit(app.exec_())
