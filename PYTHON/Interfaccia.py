import sys

import time

import logging
import numpy as np
import csv 

from PyQt5 import QtCore
from PyQt5.QtCore import (
    QObject,
    QThreadPool, 
    QRunnable, 
    pyqtSignal, 
    pyqtSlot
)

from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QPushButton,
    QComboBox,
    QHBoxLayout,
    QVBoxLayout,
    QWidget,
)

import serial
import serial.tools.list_ports

CONN_STATUS=False

class MainWindow(QMainWindow):
    def __init__(self):
        
        super(MainWindow, self).__init__()
        self.w = None
        # title and geometry
        self.setWindowTitle("Progetto 3")
        width = 600
        height = 420
        self.setMinimumSize(width, height)

        self.connected=CONN_STATUS
        self.createButton()
        self.initUI()
        

    def initUI(self):
        
        # layout
        self.button_hlay = QHBoxLayout()
        self.button_hlay.addWidget(self.conn_btn)
        #button_hlay.addWidget(self.win_btn)
        self.conn_btn.setFixedSize(200, 200)
        self.vlay = QVBoxLayout()
        self.vlay.addLayout(self.button_hlay)
      # vlay.addLayout(led_hlay)
        self.widget = QWidget()
        self.widget.setLayout(self.vlay)
        self.setCentralWidget(self.widget)


    def createButton(self):

        self.conn_btn = QPushButton(
            text = "Start",
            checkable = True
        )
        

        self.conn_btn.clicked.connect(self.on_click)

    def on_click(self,checked):
        global CONN_STATUS

        if checked:
            self.ser = serial.Serial()
            self.ser.baudrate = 9600
            self.ser.port = 'COM4'

            if not CONN_STATUS:
                try:
                    self.ser.open()
                    if self.ser.is_open():
                        CONN_STATUS=True
                except:
                    print("Didn't connect, trying again")

            while(CONN_STATUS):
                self.read_packet()
        else:
            CONN_STATUS=False
            self.ser.close()
            #self.hide()

    def read_packet(self):
        try: 
            pacchetto = self.ser.read(10)
            print(pacchetto, type(pacchetto))
        except:
            print("Ricezione non riuscita")

        valore = list(pacchetto)
        if(pacchetto[0]==160 and pacchetto[9]==192):
            valore=list(pacchetto[1:9])
            self.final = []
            i = 0
            while(i < len(valore) - 1):
                self.final.append((valore[i] << 8) + valore[i+1])
                i += 2
            print(self.final)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())
         