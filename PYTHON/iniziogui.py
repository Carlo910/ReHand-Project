import sys

import time

import logging
import numpy as np
import csv
import pickle

from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QTimer, QDateTime

import sys
from PyQt5 import QtWidgets
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import pandas as pd
import matplotlib.pyplot as plt

from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg

from PyQt5.QtCore import (

    QObject,
    QThreadPool,
    QRunnable,
    pyqtSignal,
    pyqtSlot
)

from PyQt5 import QtGui, QtCore


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
        self.setWindowTitle("RE-HAND")
        width = 1920
        height = 1000
        self.setMinimumSize(width, height)

        # create thread handler
        self.threadpool = QThreadPool()
       
        self.connected = CONN_STATUS

        self.initUI()
        self.flag_gioco= 0
        self.flag_statistiche = 0
        self.count = 0
        self.count_timer =0
        self.timernuovo=0
        self.flag_gioco_terminato=0
        self.today=QDateTime.currentDateTime()
        self.date_str = self.today.toString()

    def initUI(self):

    

        self.start_btn = QPushButton(
            text="START",
            checkable=True
        )

        # layout
        self.start_btn.setFont(QtGui.QFont('Arial', 30))
        self.Hlayout_start = QHBoxLayout()
        self.Hlayout_start.addWidget(self.start_btn)
        self.Hlayout_start.setAlignment(Qt.AlignmentFlag.AlignCenter)

       
        self.start_btn.setFixedSize(300, 300)
        self.Vlayout_start = QVBoxLayout()
        self.Vlayout_start.addLayout(self.Hlayout_start)
        self.widget_start = QWidget()
        self.widget_start.setLayout(self.Vlayout_start)
        self.setCentralWidget(self.widget_start)

        self.start_btn.clicked.connect(self.on_click)

    def on_click(self, checked):
        if checked:
            self.serial_worker.signals.device_port.connect(self.connected_device)
            self.serial_worker.signals.status.connect(self.check_serialport_status)

            
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

    ## INIZIO FINESTRA OPZIONI##

    def initUI2(self):
        
        self.layoutV_scelta = QVBoxLayout()
        self.layoutH_batteria=QHBoxLayout()
        self.layoutH_scelta = QHBoxLayout()


        self.titolo_scelta= QLabel("Seleziona l'opzione desidarata, svolgendo il gesto rappresentato")
        self.titolo_scelta.setFont(QtGui.QFont('Arial', 30))
        

        self.layoutH_scelta.addWidget(self.titolo_scelta)
        self.layoutH_scelta.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.layoutH_scelta.setSpacing(50)
        

        self.grid_scelta = QGridLayout()
        self.setLayout(self.grid_scelta)
        self.grid_scelta.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.grid_scelta.setContentsMargins(50,50,50,150)

        #inizializzazione immagine 
        self.icona_batteria=QLabel("")
        pixmap=QtGui.QPixmap("Immagini/100.png")
        self.icona_batteria.setPixmap(pixmap)
        self.icona_batteria.resize(pixmap.width(),pixmap.height())
        self.icona_batteria.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.layoutH_batteria.addWidget(self.icona_batteria)
        self.icona_batteria.setMargin(50)

        self.indice=QLabel("")
        pixmap=QtGui.QPixmap("Immagini/indice.png")
        self.indice.setPixmap(pixmap)
        self.indice.resize(pixmap.width(),pixmap.height())
     
        self.indice_medio=QLabel("")
        pixmap=QtGui.QPixmap("Immagini/indice_medio.png")
        self.indice_medio.setPixmap(pixmap)
        self.indice_medio.resize(pixmap.width(),pixmap.height())
        
        self.opzione1_btn=QLabel("Gioco Arco")
        self.opzione1_btn.setFont(QtGui.QFont('Arial', 30))
        self.opzione2_btn=QLabel("Statistiche")
        self.opzione2_btn.setFont(QtGui.QFont('Arial', 30))


        self.grid_scelta.addWidget(self.indice,1,1)
        self.grid_scelta.addWidget(self.opzione1_btn,1,2)
        self.grid_scelta.setVerticalSpacing(100)
        self.grid_scelta.addWidget(self.indice_medio, 2,1)
        self.grid_scelta.addWidget(self.opzione2_btn,2,2)

        self.layoutV_scelta.addLayout(self.layoutH_batteria)
        self.layoutV_scelta.addLayout(self.layoutH_scelta)
        self.layoutV_scelta.addLayout(self.grid_scelta)
        self.widget_scelta = QWidget()
        self.widget_scelta.setLayout(self.layoutV_scelta)
        self.setCentralWidget(self.widget_scelta)
    
        self.serial_worker.signals.packet.connect(self.handle_packet_option)

        self.serial_worker.signals.batt.connect(self.handle_batt_status)

        self.timerprova = QTimer()
        self.timerprova.timeout.connect(self.count_timeprova)
        self.timerprova.start(1000)
    
    def count_timeprova(self):
        self.timernuovo=self.timernuovo+1

    
    def handle_batt_status(self, batt):
        print(batt)
        print(self.timernuovo)
        self.perc_batt = (batt*7.4)/65535
        print("valore perc batt", self.perc_batt)
        if(self.timernuovo>0 and self.timernuovo<300):
            self.icona_batteria.setPixmap(QtGui.QPixmap("Immagini/100.png"))
        elif(self.timernuovo>300 and self.timernuovo<600):
            self.icona_batteria.setPixmap(QtGui.QPixmap("Immagini/75.png"))
        elif(self.timernuovo>600 and self.timernuovo<900):
            self.icona_batteria.setPixmap(QtGui.QPixmap("Immagini/50.png"))
        elif(self.timernuovo==9):
            self.icona_batteria.setPixmap(QtGui.QPixmap("Immagini/25.png"))
        elif(self.timernuovo==11):
            self.icona_batteria.setPixmap(QtGui.QPixmap("Immagini/0.png"))



    def handle_packet_option(self, packet):
        if (packet[0] > 7000 and packet[1] < 5500 and packet[2] > 5000 and packet[3] > 5000 and self.flag_gioco == 0 and self.flag_statistiche == 0):
          
            self.initUIGioco()
            self.flag_gioco= 1
            self.flag_statistiche = 0
            self.checkpoint=0

        elif(packet[0] > 7000 and packet[1] < 5500 and packet[2] < 7000 and packet[3] > 2500 and self.flag_statistiche == 0 and self.flag_gioco== 0):
            self.initUIStatistiche()
            self.flag_statistiche = 1
            self.flag_gioco= 0

        elif(packet[0] > 7000 and packet[1] < 5500 and packet[2] > 5000 and packet[3] > 5000 and (self.flag_statistiche == 1 or (self.flag_gioco== 1 and self.flag_gioco_terminato==1))):
            self.flag_gioco= 0
            self.flag_statistiche = 0
            self.initUI2()
            self.count = 0
            self.flag_gioco_terminato=0
            self.count_timer=0
           
        else:
            pass


    
    def initUIGioco(self):
        
        self.layoutV_gioco = QVBoxLayout()
        self.layoutH_batteria_gioco=QHBoxLayout()
        self.layoutH_gioco = QHBoxLayout()
        self.grid_gioco = QGridLayout()
        self.layoutH_fine_gioco = QHBoxLayout()
        self.layout_uscita_gioco = QGridLayout()
        self.grid_gioco.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.layout_uscita_gioco.setAlignment(Qt.AlignmentFlag.AlignBottom)
       
        self.icona_batteria=QLabel("")
        pixmap=QtGui.QPixmap("Immagini/100.png")
        self.icona_batteria.setPixmap(pixmap)
        self.icona_batteria.resize(pixmap.width(),pixmap.height())
        self.icona_batteria.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.layoutH_batteria_gioco.addWidget(self.icona_batteria)
        self.icona_batteria.setMargin(50)

        self.titolo_gioco = QLabel("Riproduci il gesto mostrato in figura")
        self.titolo_gioco.setFont(QtGui.QFont('Arial', 30))
        self.titolo_gioco.setMaximumSize(1920,70)
        self.titolo_gioco.setMinimumSize(1920,70)
        self.titolo_gioco.setMargin(550)

        self.termine_gioco = QLabel("Complimenti! Hai completato il gioco")
        self.termine_gioco.setFont(QtGui.QFont('Arial', 30))
        self.termine_gioco.setMaximumSize(1920,100)
        self.termine_gioco.setMinimumSize(1920,100)
        self.termine_gioco.setMargin(620)

        self.uscita_gioco = QLabel("Esci")
        self.uscita_gioco.setFont(QtGui.QFont('Arial', 10))
        self.uscita_gioco.setMaximumSize(1920,100)
        self.uscita_gioco.setMinimumSize(1920,100)
        
    
       
        self.mano_aperta=QLabel("")
        pixmap=QtGui.QPixmap("Immagini/mano1.png")
        self.mano_aperta.setPixmap(pixmap)
        self.mano_aperta.resize(pixmap.width(),pixmap.height())

        self.arco1=QLabel("")
        pixmap=QtGui.QPixmap("Immagini/arco1.png")
        self.arco1.setPixmap(pixmap)
        self.arco1.resize(pixmap.width(),pixmap.height())
        
        self.pollicesu=QLabel("")
        pixmap=QtGui.QPixmap("Immagini/pollicesu.png")
        self.pollicesu.setPixmap(pixmap)
        self.pollicesu.resize(pixmap.width(),pixmap.height())
       
        self.layoutH_gioco.addWidget(self.titolo_gioco)
        self.layoutH_gioco.setSpacing(10)
        
        self.grid_gioco = QGridLayout()
        self.grid_gioco.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.layout_uscita_gioco.addWidget(self.pollicesu,1,1)
        self.layout_uscita_gioco.addWidget(self.uscita_gioco,1,2)
        
        
        self.layoutV_gioco.addLayout(self.layoutH_batteria_gioco)
        self.layoutV_gioco.addLayout(self.layoutH_gioco)
        self.layoutV_gioco.addLayout(self.grid_gioco)
        self.layoutV_gioco.addLayout(self.layoutH_fine_gioco)
        self.layoutV_gioco.addLayout(self.layout_uscita_gioco)
       
        
        self.widget_gioco = QWidget()
        self.widget_gioco.setLayout(self.layoutV_gioco)
        self.setCentralWidget(self.widget_gioco)


        #ricezione segnale
        self.serial_worker.signals.prediction.connect(self.gioco)

    def gioco(self, prediction):

        if(self.flag_gioco==1 and self.count==0):
            self.grid_gioco.addWidget(self.mano_aperta,1,1)
            self.grid_gioco.setHorizontalSpacing(100)
            self.count = 1
            self.timer = QTimer()
            self.timer.timeout.connect(self.count_time)
            self.timer.start(1000)
        elif(self.flag_gioco==1 and self.count==1):
            if(prediction[0] == 0):
                self.grid_gioco.addWidget(self.arco1, 1,2)
                self.count = 2
        elif(self.flag_gioco==1 and self.count==2):
            time.sleep(1)
            #self.grid_gioco.addWidget(self.mano_semi,1,2)
            #self.grid_gioco.setHorizontalSpacing(100)
            self.mano_aperta.setPixmap(QtGui.QPixmap("Immagini/mano2.png"))
            self.count = 3
        elif(self.flag_gioco== 1 and self.count == 3):
            if(prediction[0]==1):
                #self.grid_gioco.addWidget(self.arco2,2,2)
                self.arco1.setPixmap(QtGui.QPixmap("Immagini/arco2.png"))
                self.count = 4
        elif(self.flag_gioco== 1 and self.count == 4):
            time.sleep(1)
            #self.grid_gioco.addWidget(self.mano_chiusa,1,3)
            #self.grid_gioco.setHorizontalSpacing(100)
            self.mano_aperta.setPixmap(QtGui.QPixmap("Immagini/mano3.png"))
            self.count=5
        elif(self.flag_gioco== 1 and self.count == 5):
            if(prediction[0] == 2):
                #self.grid_gioco.addWidget(self.arco3,2,3)
                self.arco1.setPixmap(QtGui.QPixmap("Immagini/arco3.png"))
                time.sleep(0.05)
                self.timer.stop()
                self.today=QDateTime.currentDateTime()
                self.date_str = self.today.toString("yyyy-MM-dd hh:mm:ss.ssss")
                row=[self.date_str,self.count_timer]
                print("Stostampando")
                print(row)
                if (self.checkpoint==0):
                    with open('data_register.csv', mode='a', newline='') as f_object: 
                        writer = csv.writer(f_object)
                        writer.writerow(row)
                        self.checkpoint=1
                self.termine_gioco.setText("Hai completato il gioco in {} s".format(self.count_timer))
                self.layoutH_fine_gioco.addWidget(self.termine_gioco)
                self.flag_gioco_terminato=1
                
                
                
        
        if(self.count_timer>30):
            self.flag_gioco_terminato=1
            self.termine_gioco.setText("Esci dal gioco! Riprova!")
            self.layoutH_fine_gioco.addWidget(self.termine_gioco)
        else:
            pass

        #elif(self.flag_gioco==1 and self.count==5):
         #   self.layoutH_fine_gioco.addWidget(self.termine_gioco)

    def count_time(self):
        self.count_timer = self.count_timer + 1
        print("stampo il valore del timer")
        print(self.count_timer)
        
    def initUIStatistiche(self):
        
        self.layoutV_statitiche=QVBoxLayout()
        self.layoutH_titolo_statistiche=QHBoxLayout()
        self.layout_grafico=QHBoxLayout()

        self.titolo_statistihe=QLabel("STATISTICHE")
        self.titolo_statistihe.setFont(QtGui.QFont('Arial', 30))
        self.titolo_statistihe.setMaximumSize(1920,70)
        self.titolo_statistihe.setMinimumSize(1920,70)
        self.titolo_statistihe.setMargin(550)
        
        self.layoutH_titolo_statistiche.addWidget(self.titolo_statistihe)
        
        self.plot()
        #self.m = PlotCanvas(self, width=5, height=4)
        self.layout_grafico.addWidget(self.fig.canvas)
        #self.m.move(0,0)

        self.layoutV_statitiche.addLayout(self.layoutH_titolo_statistiche)
        self.layoutV_statitiche.addLayout(self.layout_grafico)
        self.widget_statistiche=QWidget()
        self.widget_statistiche.setLayout(self.layoutV_statitiche)
        self.setCentralWidget(self.widget_statistiche)

        
    def plot(self):
                df=pd.read_csv('data_register.csv', header=0, parse_dates=['data'], infer_datetime_format=True)
                date = df.drop(['time'], axis = 1).values
                time= df['time'].values

                self.end = self.today.toPyDateTime()
                self.start7 = self.today.addDays(-7)
                self.start7 = self.start7.toPyDateTime()

                print("data cazz0", self.start7)


                selected_rows = df[(df['data']>=self.start7) & (df['data'] <= self.end)]

                print(type(date))

                date_str= np.array2string(date)

                #date = pd.date_range(start=self.today-10, end= self.today, freq='D')
                
                # Create a bar plot
                #plt.bar(date_str, time)
                self.fig, ax = plt.subplots()
                ax.bar(selected_rows['data'], selected_rows['time'])
                
                
                # Show the plot
                plt.xlabel('Data e ora')
                plt.ylabel('Tempo impiegato')
                plt.title('Bar Chart Ultimi 10 tentativi')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainWindow()
    app.aboutToQuit.connect(w.ExitHandler)
    w.show()
    sys.exit(app.exec_())

