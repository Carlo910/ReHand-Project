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

logging.basicConfig(format="%(message)s", level=logging.INFO)

CONN_STATUS=False

##Set port##
class SerialWorkerSignals(QObject):
    device_port = pyqtSignal(str)
    packet = pyqtSignal(list)
    status = pyqtSignal(str, int)
    

class SerialWorker(QRunnable):
    
    def __init__(self,serial_port_name):
      
        self.is_killed = False
        super().__init__()
        # init port, params and signals
        self.port = serial.Serial()
        self.port_name = 'COM4'
        self.baudrate = 9600 # hard coded but can be a global variable, or an input param
        self.signals = SerialWorkerSignals()

    @pyqtSlot()
    def run(self):
       
        global CONN_STATUS

        if not CONN_STATUS:
            try:
                self.port = serial.Serial(port=self.port_name, baudrate=self.baudrate,
                                        write_timeout=0, timeout=2)                
                if self.port.is_open:
                    CONN_STATUS = True
                    self.signals.status.emit(self.port_name, 1)
                    time.sleep(0.01)
                    self.sample = 0
                    while(CONN_STATUS == True):
                        self.read_packet() 
            except serial.SerialException:
                logging.info("Error with port {}.".format(self.port_name))
                self.signals.status.emit(self.port_name, 0)
                time.sleep(0.01)

    @pyqtSlot()
    def read_packet(self):
        try: 
            pacchetto = self.port.read(10)
            print(pacchetto, type(pacchetto))
            logging.info("Reading {} on port {}.".format(pacchetto , self.port_name))
        except:
            logging.info("Could not read {} on port {}.".format( pacchetto, self.port_name))

        valore = list(pacchetto)
        if(pacchetto[0]==160 and pacchetto[9]==192):
            valore=list(pacchetto[1:9])
            self.final = []
            i = 0
            while(i < len(valore) - 1):
                self.final.append((valore[i] << 8) + valore[i+1])
                i += 2
            print(self.final)
            self.signals.packet.emit(self.final)

    @pyqtSlot()
    def killed(self):
        
        global CONN_STATUS
        if self.is_killed and CONN_STATUS:
            CONN_STATUS = False
            self.signals.device_port.emit(self.port_name)

        logging.info("Killing the process")




class MainWindow(QMainWindow):
    def __init__(self):
        
        # define worker
        self.serial_worker= SerialWorker(None)

        super(MainWindow, self).__init__()
        self.w = None
        # title and geometry
        self.setWindowTitle("Progetto 3")
        width = 600
        height = 420
        self.setMinimumSize(width, height)

        # create thread handler
        self.threadpool = QThreadPool()

        self.connected = CONN_STATUS
        self.createButton()
        self.initUI()
        

    def initUI(self):
        
        # layout
        self.button_hlay = QHBoxLayout()
        self.button_hlay.addWidget(self.conn_btn)
        self.button_hlay.addWidget(self.camp_btn)
        #button_hlay.addWidget(self.win_btn)
        self.conn_btn.setFixedSize(200, 200)
        self.camp_btn.setFixedSize(200, 200)
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
        
        self.camp_btn=QPushButton(
            text='campiona qui',
            checkable=True
        )

        self.conn_btn.clicked.connect(self.on_click)
        self.camp_btn.clicked.connect(self.campionaqui)

    def on_click(self,checked):
        if checked:
            
            #self.hide()
            if self.w==None:
                self.w=AnotherWindow()
                self.w.show()

    def campionaqui(self,checked):
        if checked:
            self.serial_worker.signals.device_port.connect(self.connected_device)
            self.serial_worker.signals.status.connect(self.check_serialport_status)
            # execute the worker
            self.threadpool.start(self.serial_worker)
        else:
            #kill thread
            self.serial_worker.is_killed = True
            self.serial_worker.killed()

    def check_serialport_status(self, port_name, status):
        if status == 0:
            self.conn_btn.setChecked(False)
        elif status == 1:
            # enable all the widgets on the interface
          
            logging.info("Connected to port {}".format(port_name))
    

    def connected_device(self, port_name):
        """!
        @brief Checks on the termination of the serial worker.
        """
        logging.info("Port {} closed.".format(port_name))   


    def ExitHandler(self):
        """!
        @brief Kill every possible running thread upon exiting application.
        """
        self.serial_worker.is_killed = True
        self.serial_worker.killed()   

class AnotherWindow(QMainWindow):
    def __init__(self):
        
        # define worker
        self.serial_worker= SerialWorker(None)

        super(AnotherWindow, self).__init__()
        self.w = MainWindow()
        # title and geometry
        self.setWindowTitle("Progetto 3")
        width = 600
        height = 420
        self.setMinimumSize(width, height)

        # create thread handler
        self.threadpool = QThreadPool()

        self.connected = CONN_STATUS
        self.createButton2()
        self.initUI2()
    
    def initUI2(self):
         # layout
        self.button_hlay = QHBoxLayout()
        self.button_hlay.addWidget(self.close_btn)
        self.button_hlay.addWidget(self.ciao_btn)
        self.button_hlay.addWidget(self.iniziocamp_btn)
        self.close_btn.setFixedSize(200, 200)
        self.vlay = QVBoxLayout()
        self.vlay.addLayout(self.button_hlay)
      # vlay.addLayout(led_hlay)
        self.widget = QWidget()
        self.widget.setLayout(self.vlay)
        self.setCentralWidget(self.widget)

    def createButton2(self):        
        self.close_btn = QPushButton(
            text = "Close new window"
        )

        self.ciao_btn = QPushButton(
            text = "Receive",
            
        )

        self.iniziocamp_btn=QPushButton(
            text= "Finestra 3",
            checkable=True
        )

        self.close_btn.clicked.connect(self.on_click2)
        self.ciao_btn.clicked.connect(self.ricevuto)
        self.iniziocamp_btn.clicked.connect(self.campiona)
        
    def on_click2(self):
        
        self.hide()
        self.w.show()

    
    def ricevuto(self):
            print("tutto bene sono qui")
           # self.threadpool.start(self.serial_worker)
            self.serial_worker.signals.packet.connect(self.handle_packet)
    
    def campiona(self,checked):
        if checked:
            self.serial_worker.signals.device_port.connect(self.connected_device)
            self.serial_worker.signals.status.connect(self.check_serialport_status)
            # execute the worker
            self.threadpool.start(self.serial_worker)
        else:
            #kill thread
            self.serial_worker.is_killed = True
            self.serial_worker.killed()

    def check_serialport_status(self, port_name, status):
        if status == 0:
            self.iniziocamp_btn.setChecked(False)
        elif status == 1:
            # enable all the widgets on the interface
          
            logging.info("Connected to port {}".format(port_name))
    

    def connected_device(self, port_name):
        """!
        @brief Checks on the termination of the serial worker.
        """
        logging.info("Port {} closed.".format(port_name))   


    def ExitHandler(self):
        """!
        @brief Kill every possible running thread upon exiting application.
        """
        self.serial_worker.is_killed = True
        self.serial_worker.killed()     
    
        
            
            
    def handle_packet(self,packet):
        if packet[0]>0:
            print("Ho ricevuto\n\n\n\n\n")
        else:
            print("Non ho ricevuto\n\n\n\n")


        

           

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainWindow()
    y=AnotherWindow()
    app.aboutToQuit.connect(y.ExitHandler)
    w.show()
    sys.exit(app.exec_())
