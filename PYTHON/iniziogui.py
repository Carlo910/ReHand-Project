import sys

import time

import logging
import numpy as np
import csv
import pickle
#import pandas as pd
#from sklearn.ensemble import RandomForestClassifier

from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
# from PyQt5.QtGui import *
import sys

'''
from PyQt5 import QtCore
from PyQt5.QtCore import Qt
'''
from PyQt5.QtCore import (

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

CONN_STATUS = False

## Set port##


class SerialWorkerSignals(QObject):
    device_port = pyqtSignal(str)
    packet = pyqtSignal(list)
    prediction = pyqtSignal(list)
    batt = pyqtSignal(int)
    status = pyqtSignal(str, int)


class SerialWorker(QRunnable):

    def __init__(self, serial_port_name):

        self.is_killed = False
        super().__init__()
        # init port, params and signals
        self.port = serial.Serial()
        self.port_name = 'COM10'
        self.baudrate = 9600  # hard coded but can be a global variable, or an input param
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
                    while (CONN_STATUS == True):
                        char = 'Y'
                        self.port.write(char.encode('utf-8'))
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
            logging.info("Reading {} on port {}.".format(
                pacchetto, self.port_name))
        except:
            logging.info("Could not read {} on port {}.".format(
                pacchetto, self.port_name))

        valore = list(pacchetto)
        if (pacchetto[0] == 160 and pacchetto[9] == 192):
            valore = list(pacchetto[1:9])
            self.final = []
            i = 0
            while (i < len(valore) - 1):
                self.final.append((valore[i] << 8) + valore[i+1])
                i += 2
            print(self.final)
            self.signals.packet.emit(self.final)

            #load
            with open('rf_model.pkl', 'rb') as f:
               modello=pickle.load(f)

            self.final = np.array(self.final)
            self.predizione = modello.predict(self.final.reshape(1,-1))
            self.predizione = list(self.predizione)
            print(self.predizione)
            self.signals.prediction.emit(self.predizione)

        elif (pacchetto[0] == 170 and pacchetto[9] == 255):
            self.valore_batt=((pacchetto[1] << 8) + pacchetto[2])
            print(self.valore_batt)
            print("Sto stampando batteria")
            self.signals.batt.emit(self.valore_batt)

    @pyqtSlot()
    def killed(self):
        global CONN_STATUS
        if self.is_killed and CONN_STATUS:
            CONN_STATUS = False
            self.signals.device_port.emit(self.port_name)
            char = 'N'
            self.port.write(char.encode('utf-8'))
        logging.info("Killing the process")


class MainWindow(QMainWindow):
    def __init__(self):

        # define worker
        self.serial_worker = SerialWorker(None)

        super(MainWindow, self).__init__()
        self.w = None
        # title and geometry
        self.setWindowTitle("Progetto 3")
        width = 1920
        height = 1080
        self.setMinimumSize(width, height)

        # create thread handler
        self.threadpool = QThreadPool()
        # self.threadpool1 = QThreadPool()

        self.connected = CONN_STATUS
        self.initUI()
        self.flag_gioco= 0
        self.flag_statistiche = 0
        self.count = 0

    def initUI(self):

        self.start_btn = QPushButton(
            text="START",
            checkable=True
        )
        # layout
        self.start_btn.setFont(QtGui.QFont('Arial', 30))
        self.button_hlay = QHBoxLayout()
        self.button_hlay.addWidget(self.start_btn)
        self.button_hlay.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # button_hlay.addWidget(self.win_btn)
        self.start_btn.setFixedSize(300, 300)
        self.vlay = QVBoxLayout()
        self.vlay.addLayout(self.button_hlay)
        self.widget = QWidget()
        self.widget.setLayout(self.vlay)
        self.setCentralWidget(self.widget)

        self.start_btn.clicked.connect(self.on_click)

    def on_click(self, checked):
        if checked:
            self.serial_worker.signals.device_port.connect(
                self.connected_device)
            self.serial_worker.signals.status.connect(
                self.check_serialport_status)

            
            # execute the worker
            self.threadpool.start(self.serial_worker)
        else:
            # kill thread
            self.serial_worker.is_killed = True
            self.serial_worker.killed()

    def check_serialport_status(self, port_name, status):
        if status == 0:
            self.start_btn.setChecked(False)
        elif status == 1:
            # enable all the widgets on the interface
            self.initUI2()
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

    ## FINE FINESTRA HOME ##

    ## INIZIO FINESTRA SCELTA GIOCO##

    def initUI2(self):

        self.titolo2 = QLabel("Seleziona l'opzione eseguendo il gesto in figura")
        self.titolo2.setFont(QtGui.QFont('Arial', 30))
        self.titolo2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.opzione1_btn = QLabel("Gioco Arco")
        self.opzione1_btn.setFont(QtGui.QFont('Arial', 70))
        self.opzione1_btn.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.opzione2_btn = QLabel("Statistiche")
        self.opzione2_btn.setFont(QtGui.QFont('Arial', 70))
        self.opzione2_btn.setAlignment(Qt.AlignmentFlag.AlignCenter)

         # layout
        self.button1_hlay2 = QHBoxLayout()
        self.icona_indice = QLabel("")
        pixmap = QtGui.QPixmap("indice.png")
        self.icona_indice.setPixmap(pixmap)
        self.icona_indice.resize(pixmap.width(), pixmap.height())
        self.icona_indice.setAlignment(Qt.AlignmentFlag.AlignTrailing)
        self.button1_hlay2.addWidget(self.icona_indice)
        self.button1_hlay2.addWidget(self.opzione1_btn)
        
        #self.icona_indice.setAlignment(Qt.AlignmentFlag.AlignTrailing)
        
        #self.opzione1_btn.setFixedSize()
        self.button2_hlay2 = QHBoxLayout()
        self.icona_indice_medio = QLabel("")
        pixmap = QtGui.QPixmap("indice_medio.png")
        self.icona_indice_medio.setPixmap(pixmap)
        self.icona_indice_medio.resize(pixmap.width(), pixmap.height())
        self.icona_indice_medio.setAlignment(Qt.AlignmentFlag.AlignTrailing)
        self.button2_hlay2.addWidget(self.icona_indice_medio)
        self.button2_hlay2.addWidget(self.opzione2_btn)
       
        
        #self.opzione2_btn.setFixedSize(500, 100)

        self.vlay2 = QVBoxLayout()
        self.vlay2.addWidget(self.titolo2)
        self.vlay2.addLayout(self.button1_hlay2)
        self.vlay2.addLayout(self.button2_hlay2)

        self.widget2 = QWidget()
        self.widget2.setLayout(self.vlay2)
        self.setCentralWidget(self.widget2)

        #self.serial_worker.signals.packet.connect(self.handle_packet_option)
        self.serial_worker.signals.prediction.connect(self.handle_packet_option)
        self.serial_worker.signals.batt.connect(self.handle_batt_status)
    
    def handle_batt_status(self, batt):
        print(batt)
        self.perc_batt = (batt*7.4)/65535
        print("valore perc batt", self.perc_batt)


    def handle_packet_option(self, prediction):
        print('sono qui 11', prediction)
        if(prediction[0] == 3 and self.flag_gioco == 0 and self.flag_statistiche == 0):
        #if (packet[0] > 7000 and packet[1] < 5500 and packet[2] > 4000 and packet[3] > 5500 and self.flag_gioco == 0 and self.flag_statistiche == 0):
            # self.createButton()
            self.initUIGioco()
            self.flag_gioco= 1
            self.flag_statistiche = 0

        elif(prediction[0] == 4 and self.flag_gioco == 0 and self.flag_statistiche == 0):
        #elif (packet[0] > 7000 and packet[1] < 5500 and packet[2] < 4000 and packet[3] > 5500 and self.flag_statistiche == 0 and self.flag_gioco== 0):
            self.initUI4()
            self.flag_statistiche = 1
            self.flag_gioco= 0

        elif(prediction==2 and self.flag_gioco == 1 and self.flag_statistiche == 1):
        #elif (packet[0] > 6000 and packet[1] > 8000 and packet[2] > 8000 and packet[3] > 7000 and (self.flag_gioco== 1 or self.flag_statistiche == 1)):
            self.flag_gioco= 0
            self.flag_statistiche = 0
            self.initUI2()
            self.count = 0
           
        else:
            pass


    
    def initUIGioco(self):
        
        
        self.titolo3=QLabel("GIOCO ARCO")
        self.sottotitolo3=QLabel("Riproduci il gesto mostrato in figura")
        self.layout3=QVBoxLayout()
        self.layout3.addWidget(self.titolo3)
        self.layout3.addWidget(self.sottotitolo3)
        self.titolo3.setFont(QtGui.QFont('Arial', 30))
        self.titolo3.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.sottotitolo3.setFont(QtGui.QFont('Arial', 16))
        self.sottotitolo3.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        
       
       
        #Layout
       
        self.widget3 = QWidget()
        self.widget3.setLayout(self.layout3)
        self.setCentralWidget(self.widget3)

        self.layout_immagine1 = QHBoxLayout()
        self.layout_immagine2 = QHBoxLayout()
        self.layout_immagine3 = QHBoxLayout()
        self.layout3.addLayout(self.layout_immagine1)
        self.layout3.addLayout(self.layout_immagine2)
        self.layout3.addLayout(self.layout_immagine3)

        #inizializzazione immagine 
        self.mano_aperta=QLabel("")
        pixmap=QtGui.QPixmap("mano1.png")
        self.mano_aperta.setPixmap(pixmap)
        self.mano_aperta.resize(pixmap.width(),pixmap.height())
        self.mano_aperta.setAlignment(Qt.AlignmentFlag.AlignLeft)

        
        self.mano_semi=QLabel("")
        pixmap=QtGui.QPixmap("mano2.png")
        self.mano_semi.setPixmap(pixmap)
        self.mano_semi.resize(pixmap.width(),pixmap.height())
        self.mano_semi.setAlignment(Qt.AlignmentFlag.AlignLeft)
       

        self.mano_chiusa=QLabel("")
        pixmap=QtGui.QPixmap("mano3.png")
        self.mano_chiusa.setPixmap(pixmap)
        self.mano_chiusa.resize(pixmap.width(),pixmap.height())
        self.mano_chiusa.setAlignment(Qt.AlignmentFlag.AlignLeft)

    
        self.arco1=QLabel("")
        pixmap=QtGui.QPixmap("arco1.png")
        self.arco1.setPixmap(pixmap)
        self.arco1.resize(pixmap.width(),pixmap.height())
        self.arco1.setAlignment(Qt.AlignmentFlag.AlignRight)

        self.arco2=QLabel("")
        pixmap=QtGui.QPixmap("arco2.png")
        self.arco2.setPixmap(pixmap)
        self.arco2.resize(pixmap.width(),pixmap.height())
        self.arco2.setAlignment(Qt.AlignmentFlag.AlignRight)
        
        self.arco3=QLabel("")
        pixmap=QtGui.QPixmap("arco3.png")
        self.arco3.setPixmap(pixmap)
        self.arco3.resize(pixmap.width(),pixmap.height())
        self.arco3.setAlignment(Qt.AlignmentFlag.AlignRight)


        #ricezione segnale
        #self.serial_worker.signals.packet.connect(self.gioco)
        self.serial_worker.signals.prediction.connect(self.gioco)

    def gioco(self, prediction):
        print('sono qui', prediction)
        if(self.flag_gioco==1 and self.count==0):
            self.layout_immagine1.addWidget(self.mano_aperta)
            self.count = 1
        elif(self.flag_gioco==1 and self.count==1):
            if(prediction[0] == 0):
            #if(packet[0]<5000 and packet[1]<5000 and packet[2]<6500 and packet[3]<3000):         
                self.layout_immagine1.addWidget(self.arco1)
                self.count = 2
        elif(self.flag_gioco==1 and self.count==2):
            time.sleep(0.05)
            self.layout_immagine2.addWidget(self.mano_semi)
            self.count = 3
        elif(self.flag_gioco== 1 and self.count == 3):
            if(prediction[0]==1):
            #if(packet[0]<5000 and packet[1]<5000 and packet[2]<6500 and packet[3]>3000):
                self.layout_immagine2.addWidget(self.arco2)
                self.count = 4
        elif(self.flag_gioco== 1 and self.count == 4):
            time.sleep(0.05)
            self.layout_immagine3.addWidget(self.mano_chiusa)
            self.count=5
        elif(self.flag_gioco== 1 and self.count == 5):
            if(prediction[0] == 2):
            #if(packet[0] < 5000 and packet[1] > 8000 and packet[2] > 8000 and packet[3] > 7000):
                self.layout_immagine3.addWidget(self.arco3)

        
    def initUI4(self):

        self.titolo4=QLabel("          STATISTICHE")
        #self.titolo3.setAlignment(Qt)
        self.layout4=QHBoxLayout()
        self.layout4.addWidget(self.titolo4)
        self.titolo4.setFont(QtGui.QFont('Arial', 30))

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

