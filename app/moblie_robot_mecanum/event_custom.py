
import serial, serial.tools.list_ports
import cv2 
from PySide2.QtWidgets import *
from custom_serial import SerialThread
from yolov8_custom import yolov8
from PySide2 import QtGui
from PySide2 import QtCore,QtGui,QtWidgets
from PySide2.QtGui import *
import time
class event_custom():
	def __init__(self,window):
		super().__init__()
		self.window =window
		self.time=time.time()
		self.list_key=['q','w','e','a','s','d','z','x','c','v','b']
		self.direction='4'
		self.direction_old='4'
		self.stop=False
		self.manual=False
		self.speed_list={'0':'4','10':'5','9':'6','8':'7','7':'8','6':'9','5':'0','4':'t','3':'y','2':'u','1':'i'}
	def Close(self):
		self.yolov8_thread.quit()
		self.window.close()
	def resize(self,frame):
		self.sizegrip = QSizeGrip(frame)
		self.sizegrip.setStyleSheet("QSizeGrip { width: 10px; height: 10px; margin: 5px} QSizeGrip:hover { background-color: rgb(50, 42, 94)}")
		self.sizegrip.setToolTip("Resize Window")
	def maximize_restore(self,button):
		if button.isChecked()==False:
			self.window.showMaximized()
			button.setToolTip("Restore")
		else:
			self.window.showNormal()
			button.setToolTip("Maximize")
	def update_ports(self,comboBox):
		self.portlist = [port.device for port in serial.tools.list_ports.comports()]
		comboBox.clear()
		comboBox.addItems(self.portlist)
	def connect_ports(self,port, baud, button):
		if(button.isChecked()):
			self.serial_thread = SerialThread(port,baud)
			self.serial_thread.data_received.connect(self.update_terminal)
			self.serial_thread.start()
			try:
				if(self.serial_thread.serial_port.is_open):
					button.setText('DISCONNECT')
			except:
				button.setChecked(False)
				print("Error")
		else:
			self.serial_thread.serial_port.close()
			self.serial_thread.quit()
			self.serial_thread = None
			button.setText('CONNECT')
	def run_camera(self,source,model,frame_img):
		self.frame_img=frame_img
		self.yolov8_thread = yolov8(source,model)
		self.yolov8_thread.data_received.connect(self.update_image)
		self.yolov8_thread.start()
	def update_terminal(self,data):
		self.Send_direction()
		try:
			self.window.ui.label_4.setText("Left:       "+str(data[1]))
			self.window.ui.label_7.setText("Right:      "+str(data[0]))
			self.window.ui.label_8.setText("Distance: "+str(data[2:None]))
		except:
			print('Error')
	def update_image(self,image):
		self.show_webcam(image,self.frame_img)
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
	def read_direction(self,direction):
		self.direction=direction
		self.time=time.time()
	def Send_direction(self):
		if self.direction in self.list_key:
			if time.time()-self.time<0.1:
				self.set_sheet_button_off(self.window.ui.pushButton_13)
				if self.direction=='q':
					self.set_sheet_button_on(self.window.ui.pushButton_8)
				elif self.direction=='w':
					self.set_sheet_button_on(self.window.ui.pushButton_12)
				elif self.direction=='e':
					self.set_sheet_button_on(self.window.ui.pushButton_15)
				elif self.direction=='a':
					self.set_sheet_button_on(self.window.ui.pushButton_10)
				elif self.direction=='d':
					self.set_sheet_button_on(self.window.ui.pushButton_16)
				elif self.direction=='z':
					self.set_sheet_button_on(self.window.ui.pushButton_11)
				elif self.direction=='x':
					self.set_sheet_button_on(self.window.ui.pushButton_14)
				elif self.direction=='c':
					self.set_sheet_button_on(self.window.ui.pushButton_17)
				elif self.direction=='v':
					self.set_sheet_button_on(self.window.ui.pushButton_18)
				elif self.direction=='b':
					self.set_sheet_button_on(self.window.ui.pushButton_20)

				if self.direction!=self.direction_old:
					if self.manual==True:
						self.serial_thread.write_data(self.direction)
					# print(self.direction)
					# self.set_sheet_button(1)
					self.direction_old=self.direction
				self.stop=True
			elif self.stop==True:
				self.direction='4'
				self.direction_old='4'
				self.set_sheet_button_off(self.window.ui.pushButton_8)
				self.set_sheet_button_off(self.window.ui.pushButton_12)
				self.set_sheet_button_off(self.window.ui.pushButton_15)
				self.set_sheet_button_off(self.window.ui.pushButton_10)
				self.set_sheet_button_off(self.window.ui.pushButton_16)
				self.set_sheet_button_off(self.window.ui.pushButton_11)
				self.set_sheet_button_off(self.window.ui.pushButton_14)
				self.set_sheet_button_off(self.window.ui.pushButton_17)
				self.set_sheet_button_off(self.window.ui.pushButton_18)
				self.set_sheet_button_off(self.window.ui.pushButton_20)
				self.set_sheet_button_on(self.window.ui.pushButton_13)
				if self.manual==True:
					self.serial_thread.write_data('4')
				# print('4')
				self.stop=False
	def manual_mode(self):
		try:
			if self.manual==False:
				self.yolov8_thread.mode(True)
				self.manual=True
			else:
				self.yolov8_thread.mode(False)
				self.manual=False
		except:
			print("Error")
	def tracking(self):
		try:
			self.manual=False
			self.serial_thread.write_data('2')
		except:
			print("Error")
	def auto(self):
		try:
			self.manual=False
			self.serial_thread.write_data('3')
		except:
			print("Error")
	def move_around(self):
		try:
			self.manual=False
			self.serial_thread.write_data('1')
		except:
			print("Error")
	def set_sheet_button_on(self,button):
		button.setStyleSheet(u"*{\n"
		"padding-left:5px;\n"
		"padding-top:5px;\n"
		"background-color:rgba(105,118,132,200);\n"
		"}\n")
	def set_sheet_button_off(self,button):
		button.setStyleSheet(u"QPushButton{\n"
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
		"}\n")
	def car_stop(self):
		try:
			self.serial_thread.write_data('4')
		except:
			print('Error')
	def car_speed(self,speed):
		speed=str(speed)
		try:
			self.serial_thread.write_data(self.speed_list[speed])
			print(speed)
		except:
			print('Error')

	def follow_wall(self):
		try:
			self.serial_thread.write_data('n')
		except:
			print('Error')