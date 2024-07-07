from PySide2.QtCore import (QThread,Signal,QObject)
import serial
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
            if self.serial_port.in_waiting > 0:
                self.data = self.serial_port.readline().decode()
            self.data_received.emit(self.data)
    def write_data(self, data):
        data=str(data)
        self.serial_port.write(data.encode())