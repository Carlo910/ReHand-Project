import sys

import time

import logging
import numpy as np
import csv 

from PyQt5 import QtCore
from PyQt5.QtCore import (
    Qt,
    QObject,
    QThreadPool, 
    QRunnable, 
    pyqtSignal, 
    pyqtSlot
)
from PyQt5 import QtGui

from PyQt5.QtGui import QPixmap

from PyQt5.QtWidgets import (
    QLabel,
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
        self.port_name = 'COM7'
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
        #self.threadpool1 = QThreadPool()

        self.connected = CONN_STATUS
        self.initUI()
        self.flag1=0
        self.flag2=0
        self.flaggioco=0

    def initUI(self):
        
        
        self.start_btn = QPushButton(
            text = "Start",
            checkable = True
        )
        # layout
        self.button_hlay = QHBoxLayout()
        self.button_hlay.addWidget(self.start_btn)
       
        #button_hlay.addWidget(self.win_btn)
        self.start_btn.setFixedSize(200, 200)
        self.vlay = QVBoxLayout()
        self.vlay.addLayout(self.button_hlay)
        self.widget = QWidget()
        self.widget.setLayout(self.vlay)
        self.setCentralWidget(self.widget)

        self.start_btn.clicked.connect(self.on_click)
        

    def on_click(self,checked):
        if checked:
            self.serial_worker.signals.device_port.connect(self.connected_device)
            self.serial_worker.signals.status.connect(self.check_serialport_status)
            self.initUI2()
            # execute the worker
            self.threadpool.start(self.serial_worker)
        else:
            #kill thread
            self.serial_worker.is_killed = True
            self.serial_worker.killed()
            
    def check_serialport_status(self, port_name, status):
        if status == 0:
            self.start_btn.setChecked(False)
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
    

    ##FINE FINESTRA HOME ##
    
    ##INIZIO FINESTRA SCELTA GIOCO##

    def initUI2(self):

        self.opzione1_btn=QPushButton(
            text= "Alza l'indice",
            checkable=True
        )


        self.opzione2_btn=QPushButton(
            text= "Alza indice e medio",
            checkable=True
        )
         # layout
        button_hlay2 = QHBoxLayout()
        button_hlay2.addWidget(self.opzione1_btn)
        button_hlay2.addWidget(self.opzione2_btn)
        #self.opzione1_btn.setFixedSize(200, 200)
        vlay2 = QVBoxLayout()
        vlay2.addLayout(button_hlay2)
      # vlay.addLayout(led_hlay)
        self.widget2 = QWidget()
        self.widget2.setLayout(vlay2)
        self.setCentralWidget(self.widget2)

        
        #load immagine
        self.immagine=QLabel("Immagine")
        pixmap=QtGui.QPixmap("ossa-della-mano.png")
        self.immagine.setPixmap(pixmap)
        #self.immagine.setScaledContents(True)
        self.immagine.resize(pixmap.width(),pixmap.height())
        
         
        self.serial_worker.signals.packet.connect(self.handle_packet_option)
     
    def handle_packet_option(self, packet): 
        if (packet[0]>5000 and packet[1]<7000 and packet[2]>5000 and packet[3]>5000 and self.flag1==0):
            #self.createButton()
            self.initUI3()
            self.flag1=1
            self.flag2=0
            self.flaggioco=True
         

        
        elif(packet[0]>5000 and packet[1]<5000 and packet[2]<5000 and packet[3]>5000 and self.flag2==0 and self.flaggioco==False):
            self.initUI4()
            self.flag2=1
            self.flag1=0

        elif(packet[0]>6000 and packet[1]>6000 and packet[2]>6000 and packet[3]>6000 and (self.flag1==1 or self.flag2==1)):
            self.flag1=0
            self.flag2=0
            self.immagine.hide()
            self.initUI2()
            self.flaggioco=0
        else:
            pass
    
    def initUI3(self):
        
        
        self.titolo3=QLabel("                                               GIOCO ARCO")
        #self.titolo3.setAlignment(Qt)
        self.layout3=QHBoxLayout()
        self.layout3.addWidget(self.titolo3)
       
        #Layout
       
        self.widget3 = QWidget()
        self.widget3.setLayout(self.layout3)
        self.setCentralWidget(self.widget3)
        
    def initUI3(self):
        
        
        self.titolo4=QLabel("                                                STATISTICHE")
        #self.titolo3.setAlignment(Qt)
        self.layout4=QHBoxLayout()
        self.layout4.addWidget(self.titolo4)
       
        #Layout
       
        self.widget4 = QWidget()
        self.widget4.setLayout(self.layout4)
        self.setCentralWidget(self.widget4)
        


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainWindow()
    app.aboutToQuit.connect(w.ExitHandler)
    w.show()
    sys.exit(app.exec_())

