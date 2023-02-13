import sys
import time
import logging
import numpy as np
import csv
import pickle
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets
import pandas as pd
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg 
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import datetime as dt
from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import (
    Qt, 
    QTimer, 
    QDateTime,
    QObject,
    QThreadPool,
    QRunnable,
    pyqtSignal,
    pyqtSlot
)

import serial
import serial.tools.list_ports

logging.basicConfig(format="%(message)s", level=logging.INFO)

CONN_STATUS = False

## Inizializzazione dei segnali ##

class SerialWorkerSignals(QObject):
    device_port = pyqtSignal(str)
    packet = pyqtSignal(list)
    batt = pyqtSignal(int)
    status = pyqtSignal(str, int)

## Gestione della comunicazione seriale, ricezione, elaborazione e ricostruzione dati ##
class SerialWorker(QRunnable):
    
    def __init__(self, serial_port_name):

        self.is_killed = False
        super().__init__()
        # Inizializzazione porta seriale, parametri e segnale 
        self.port = serial.Serial()
        self.port_name = 'COM10'
        self.baudrate = 9600 
        self.signals = SerialWorkerSignals()

    ## Connessione e lettura dati ##
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
                        # Invio carattere per segnalare la connessione, iniziare la trasmissione dei dati e gestione lampeggio led
                        char = 'Y' 
                        self.port.write(char.encode('utf-8'))
                        self.read_packet() 
            except serial.SerialException:
                logging.info("Error with port {}.".format(self.port_name))
                self.signals.status.emit(self.port_name, 0)
                time.sleep(0.01)
               
    ## Lettura e ricostruzione dei pacchetti ricevuti 
    @pyqtSlot()
    def read_packet(self):

        try:
            pacchetto = self.port.read(10)
        except:
            logging.info("Could not read {} on port {}.".format(
                pacchetto, self.port_name))

        valore = list(pacchetto)
        # Controllo pacchetto e ricostruzione valore dei quattro sensori flex
        if (pacchetto[0] == 160 and pacchetto[9] == 192):
            valore = list(pacchetto[1:9])
            self.final = []
            i = 0
            while (i < len(valore) - 1):
                self.final.append((valore[i] << 8) + valore[i+1])
                i += 2
            # Invio segnale alla MainWindow()
            self.signals.packet.emit(self.final)
        # Controllo pacchetto e ricostruzione valore tensione batteria 
        elif (pacchetto[0] == 170 and pacchetto[9] == 255):
            self.valore_batt=((pacchetto[1] << 8) + pacchetto[2])
            # Invio segnale alla MainWindow()
            self.signals.batt.emit(self.valore_batt)

    ## Interruzione connessione e interruzione trasmissione dati
    @pyqtSlot()
    def killed(self):
        global CONN_STATUS
        if self.is_killed and CONN_STATUS:
            CONN_STATUS = False
            self.signals.device_port.emit(self.port_name)
            # Invio carattere che segnala la fine della connessione e gestione lampeggio led
            char = 'N'
            self.port.write(char.encode('utf-8'))
        logging.info("Killing the process")

## Classe principale che contiene tutte le finestre dell'interfaccia grafica ##
class MainWindow(QMainWindow):
    def __init__(self):

        self.serial_worker = SerialWorker(None)

        super(MainWindow, self).__init__()
        #Titolo e geometria dell'applicazione
        self.setWindowTitle("RE-HAND")
        width = 1920
        height = 1000
        self.setMinimumSize(width, height)

        self.threadpool = QThreadPool()
       
        self.connected = CONN_STATUS

        # Visualizzazione prima finestra 
        self.initUI()
        # Dichiarazione flag per la gestione dell'applicazione 
        self.flag_gioco= 0
        self.flag_statistiche = 0
        self.count = 0
        self.count_timer =0
        self.timernuovo=0
        self.flag_gioco_terminato=0
        self.visualizza_statistiche = 1
        self.delay=0
        # Variabile per registrare la data e ora odierna
        self.today=QDateTime.currentDateTime()
        self.date_str = self.today.toString()

    ## PRIMA FINESTRA DI START ##
    def initUI(self):
        # Definizione layout
        self.Vlayout_start = QVBoxLayout()
        self.Hlayout_titolo_start = QHBoxLayout()
        self.Hlayout_inserisci_nome_utente=QHBoxLayout()
        self.Hlayout_inserisci_nome_utente.setContentsMargins(725,100,0,0)
        self.Hlayout_nome_utente=QHBoxLayout()
        self.Hlayout_start = QHBoxLayout()

        # Definizione  e design dei Widgets
        # Titolo
        self.titolo_start = QLabel("Re-Hand")
        self.titolo_start.setFont(QtGui.QFont('Arial', 100))
        self.titolo_start.setStyleSheet("QLabel { color : red; }")

        # Inserimento nome utente
        self.inserisci_nome=QLabel("Inserisci il tuo nome:")
        self.inserisci_nome.setFont(QtGui.QFont('Arial', 30))
        self.nome_utente_line=QLineEdit()
        self.nome_utente_line.setFont(QtGui.QFont('Arial', 30))
        self.nome_utente_line.setFixedSize(300,80)

        # Bottone di Start
        self.start_btn = QPushButton(
            text="START",
            checkable=False,    
        )

        self.start_btn.setFont(QtGui.QFont('Arial', 50))
        self.start_btn.setFixedSize(400, 250)
        self.start_btn.setStyleSheet("QPushButton { background-color : ; color : green; }")

        # MessageBox di avviso in caso l'utente non inserisca il nome 
        self.message_box_start= QMessageBox()
        self.message_box_start.setText("Inserisci prima il tuo nome ")
        self.message_box_start.setFont(QtGui.QFont('Arial', 25))
        self.message_box_start.setWindowTitle("AVVISO")

        # Aggiunta dei widgets ai layout orizzontali
        self.Hlayout_inserisci_nome_utente.addWidget(self.inserisci_nome)
        self.Hlayout_nome_utente.addWidget(self.nome_utente_line)
        self.Hlayout_titolo_start.addWidget(self.titolo_start)
        self.Hlayout_titolo_start.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.Hlayout_titolo_start.setContentsMargins(625,60,0,0)
        self.Hlayout_start.addWidget(self.start_btn)
        self.Hlayout_start.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.Hlayout_start.setContentsMargins(750,50,0,100)

        # Aggiunta dei layout orizzontale al layout verticale
        self.Vlayout_start.addLayout(self.Hlayout_titolo_start)
        self.Vlayout_start.addLayout(self.Hlayout_inserisci_nome_utente)
        self.Vlayout_start.addLayout(self.Hlayout_nome_utente)
        self.Vlayout_start.addLayout(self.Hlayout_start)

        # Aggiunta layout verticale al widget
        self.widget_start = QWidget()
        self.widget_start.setLayout(self.Vlayout_start)
        self.setCentralWidget(self.widget_start)

        # Connessione pulsante alla funzione on_click
        self.start_btn.clicked.connect(self.on_click)


    def on_click(self):
        # Controllo inserimento nome utente, salvataggio nome utente e connessione alla porta seriale
        if(self.nome_utente_line.text() != ""):
            self.nome_utente=str(self.nome_utente_line.text())
            self.serial_worker.signals.device_port.connect(self.connected_device)
            self.serial_worker.signals.status.connect(self.check_serialport_status)
            self.threadpool.start(self.serial_worker)
        elif(self.nome_utente_line.text() == ""):
        # Messaggio di errore se il nome utente non viene inserito
            self.message_box_start.exec_()
        
    # Verifinca status porta seriale e visualizzazione seconda finestra
    def check_serialport_status(self, port_name, status):
        if status == 0:
            self.start_btn.setChecked(False)
        elif status == 1:
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

    ## FINE FINESTRA  DI START ##

    ## INIZIO FINESTRA DI HOME ##

    def initUI2(self):
        # Definizione layout
        self.layoutV_scelta = QVBoxLayout()
        self.layoutH_batteria=QHBoxLayout()
        self.layoutH_scelta = QHBoxLayout()


        self.grid_scelta = QGridLayout()
        self.setLayout(self.grid_scelta)
        self.grid_scelta.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.grid_scelta.setContentsMargins(50,50,50,150)

        # Definizione widget 
        # Titolo
        self.titolo_scelta= QLabel("Ciao {}!\nSeleziona l'opzione desidarata, svolgendo il gesto rappresentato".format(self.nome_utente))
        self.titolo_scelta.setFont(QtGui.QFont('Arial', 30))

        # Inizializzazione immagini
        self.icona_batteria=QLabel("")
        pixmap=QtGui.QPixmap("Immagini/100.png")
        self.icona_batteria.setPixmap(pixmap)
        self.icona_batteria.resize(pixmap.width(),pixmap.height())
        self.icona_batteria.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.layoutH_batteria.addWidget(self.icona_batteria)
        self.icona_batteria.setMargin(35)

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
        
        # MessageBox di avviso se non ci sono abbastanza statistiche
        self.message_box = QMessageBox()
        self.message_box.setText("Completa due volte il gioco per visualizzare le statistiche")
        self.message_box.setFont(QtGui.QFont('Arial', 25))
        self.message_box.setWindowTitle("Avviso per {}".format(self.nome_utente))
        
        # Aggiunta widget ai layout
        self.layoutH_scelta.addWidget(self.titolo_scelta)
        self.layoutH_scelta.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.layoutH_scelta.setSpacing(50)
        self.grid_scelta.addWidget(self.indice,1,1)
        self.grid_scelta.addWidget(self.opzione1_btn,1,2)
        self.grid_scelta.setVerticalSpacing(100)
        self.grid_scelta.addWidget(self.indice_medio, 2,1)
        self.grid_scelta.addWidget(self.opzione2_btn,2,2)

        # Aggiunta layout al layout verticale
        self.layoutV_scelta.addLayout(self.layoutH_batteria)
        self.layoutV_scelta.addLayout(self.layoutH_scelta)
        self.layoutV_scelta.addLayout(self.grid_scelta)

        # Aggiunta del layout verticale al widget
        self.widget_scelta = QWidget()
        self.widget_scelta.setLayout(self.layoutV_scelta)
        self.setCentralWidget(self.widget_scelta)
        
        # Funzione ricezione e gestione dati sensori e valore batteria
        self.serial_worker.signals.packet.connect(self.handle_packet_option)
        self.serial_worker.signals.batt.connect(self.handle_batt_status)
    
    # Funzione della gestione batteria
    def handle_batt_status(self, batt):
        self.valore_batt = (batt*7.8)/65535
        print("valore perc batt", self.valore_batt)
        if(self.valore_batt>3.9):
            self.icona_batteria.setPixmap(QtGui.QPixmap("Immagini/100.png"))
        elif(self.valore_batt>3.8 and self.valore_batt<=3.9):
            self.icona_batteria.setPixmap(QtGui.QPixmap("Immagini/75.png"))
        elif(self.valore_batt>3.7 and self.valore_batt<=3.8):
            self.icona_batteria.setPixmap(QtGui.QPixmap("Immagini/50.png"))
        elif(self.valore_batt>3.6 and self.valore_batt<=3.7):
            self.icona_batteria.setPixmap(QtGui.QPixmap("Immagini/25.png"))
        elif(self.valore_batt<=3.6):
            self.icona_batteria.setPixmap(QtGui.QPixmap("Immagini/0.png"))

    # Riconoscimento gesti tramite il modello e utilizzo gesti per la visualizzazione delle schermate
    def handle_packet_option(self, packet):
        
        # Controllo sul numero minimo di esercizi svolti
        if (self.visualizza_statistiche ==1):
            df=pd.read_csv('data_register.csv', header=0)
            df=df[df['nome'] == self.nome_utente].reset_index(drop=True)
            num_rows=len(df.index)
            if(num_rows>1):
                self.visualizza_statistiche=0
            else:
                self.visualizza_statistiche=1                
        else:
            pass
        
        # Caricamento modello e predizione
        with open('rf_model_6gesti.pkl', 'rb') as f:
               modello=pickle.load(f)

        pacchetto = np.array(packet)
        self.predizione = modello.predict(pacchetto.reshape(1,-1))
        self.predizione = list(self.predizione)
        
        # Gestione scelte con la predizione 
        if(self.predizione[0]==4 and self.flag_gioco == 0 and self.flag_statistiche == 0):
            self.flag_gioco= 1
            self.flag_statistiche = 0
            self.checkpoint=0
            # Visualizzazione schermata del gioco
            self.initUIGioco()

        elif(self.predizione[0]==5 and self.flag_statistiche == 0 and self.flag_gioco== 0 and self.visualizza_statistiche==0 ):
            # Visualizzazione schermata delle statistiche
            self.initUIStatistiche()
            self.flag_statistiche = 1
            self.flag_gioco= 0

        elif(self.predizione[0] ==3 and (self.flag_statistiche == 1 or (self.flag_gioco== 1 and self.flag_gioco_terminato==1))):
            self.flag_gioco= 0
            self.flag_statistiche = 0
            # Visualizzazione schermata della HOME 
            self.initUI2()
            self.count = 0
            self.flag_gioco_terminato=0
            self.count_timer=0

        elif(self.predizione[0]==5 and self.flag_statistiche == 0 and self.flag_gioco== 0 and self.visualizza_statistiche==1):
            # MessageBox di avviso se non ci sono abbastanza esercizi svolti
            self.message_box.exec_()
                      
        else:
            pass
    
    ## FINE FINESTRA HOME ##
    
    ## INIZIO FINESTRA GIOCO ##
    def initUIGioco(self):
        # Definzione layout
        self.layoutV_gioco = QVBoxLayout()
        self.layoutH_batteria_gioco=QHBoxLayout()
        self.layoutH_gioco = QHBoxLayout()
        self.grid_gioco = QGridLayout()
        self.layoutH_fine_gioco = QHBoxLayout()
        self.layout_uscita_gioco = QGridLayout()
        self.layout_uscita_gioco.setAlignment(Qt.AlignmentFlag.AlignBottom)
        self.grid_gioco = QGridLayout()
        self.grid_gioco.setAlignment(Qt.AlignmentFlag.AlignCenter)
       
        # Definizione widgets
        # Icona batteria
        self.icona_batteria=QLabel("")
        pixmap=QtGui.QPixmap("Immagini/100.png")
        self.icona_batteria.setPixmap(pixmap)
        self.icona_batteria.resize(pixmap.width(),pixmap.height())
        self.icona_batteria.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.layoutH_batteria_gioco.addWidget(self.icona_batteria)
        self.icona_batteria.setMargin(35)

        # Istruzione del gioco
        self.titolo_gioco = QLabel("Riproduci il gesto mostrato in figura")
        self.titolo_gioco.setFont(QtGui.QFont('Arial', 30))
        self.titolo_gioco.setMaximumSize(1920,70)
        self.titolo_gioco.setMinimumSize(1920,70)
        self.titolo_gioco.setMargin(550)

        # Feedback di fine gioco
        self.termine_gioco = QLabel("")
        self.termine_gioco.setFont(QtGui.QFont('Arial', 30))
        self.termine_gioco.setMaximumSize(1920,100)
        self.termine_gioco.setMinimumSize(1920,100)
        
        # Icona tasto uscita 
        self.uscita_gioco = QLabel("Esci")
        self.uscita_gioco.setFont(QtGui.QFont('Arial', 15))
        self.uscita_gioco.setMaximumSize(1920,100)
        self.uscita_gioco.setMinimumSize(1920,100)

        self.pollicesu=QLabel("")
        pixmap=QtGui.QPixmap("Immagini/pollicesu.png")
        self.pollicesu.setPixmap(pixmap)
        self.pollicesu.resize(pixmap.width(),pixmap.height())

        # Caricamento immagini per il gioco 
        self.mano_aperta=QLabel("")
        pixmap=QtGui.QPixmap("Immagini/mano1.png")
        self.mano_aperta.setPixmap(pixmap)
        self.mano_aperta.resize(pixmap.width(),pixmap.height())

        self.arco1=QLabel("")
        pixmap=QtGui.QPixmap("Immagini/arco1.png")
        self.arco1.setPixmap(pixmap)
        self.arco1.resize(pixmap.width(),pixmap.height())
        
        # Aggiunta widget ai layout
        self.layoutH_gioco.addWidget(self.titolo_gioco)
        self.layoutH_gioco.setSpacing(10)
        self.layoutH_fine_gioco.addWidget(self.termine_gioco)
        self.layout_uscita_gioco.addWidget(self.pollicesu,1,1)
        self.layout_uscita_gioco.addWidget(self.uscita_gioco,1,2)
        
        # Aggiunta dei layout al layout verticale 
        self.layoutV_gioco.addLayout(self.layoutH_batteria_gioco)
        self.layoutV_gioco.addLayout(self.layoutH_gioco)
        self.layoutV_gioco.addLayout(self.grid_gioco)
        self.layoutV_gioco.addLayout(self.layoutH_fine_gioco)
        self.layoutV_gioco.addLayout(self.layout_uscita_gioco)
       
        # Aggiunta layout verticale al widget
        self.widget_gioco = QWidget()
        self.widget_gioco.setLayout(self.layoutV_gioco)
        self.setCentralWidget(self.widget_gioco)

        #Connessione e ricezione segnale per il gioco 
        self.serial_worker.signals.packet.connect(self.gioco)

    ## Funzione gestione gioco ##
    def gioco(self, packet):            
        #Caricamento modello per la predizione
        with open('rf_model_6gesti.pkl', 'rb') as f:
            modello=pickle.load(f)

        pacchetto = np.array(packet)

        # Gestione dei livelli del gioco
        if(self.flag_gioco==1 and self.count==0):
            self.grid_gioco.addWidget(self.mano_aperta,1,1)
            self.grid_gioco.setHorizontalSpacing(100)
            self.count = 1
            self.secondi=0
            self.timer = QTimer()
            self.timer.timeout.connect(self.count_time)
            self.timer.start(100)
        elif(self.flag_gioco==1 and self.count==1):
            self.predizione = modello.predict(pacchetto.reshape(1,-1))
            self.predizione = list(self.predizione)
            if(self.predizione[0] == 0):
                self.grid_gioco.addWidget(self.arco1, 1,2)
                self.count = 2
                self.delay=0
        elif(self.flag_gioco==1 and self.count==2):
            if(self.delay>0.7):
                self.mano_aperta.setPixmap(QtGui.QPixmap("Immagini/mano2.png"))
                self.count = 3
        elif(self.flag_gioco== 1 and self.count == 3):
            self.predizione = modello.predict(pacchetto.reshape(1,-1))
            self.predizione = list(self.predizione)
            if(self.predizione[0]==1):
                self.arco1.setPixmap(QtGui.QPixmap("Immagini/arco2.png"))
                self.count = 4
                self.delay=0
        elif(self.flag_gioco== 1 and self.count == 4):
            if(self.delay>0.7):
                self.mano_aperta.setPixmap(QtGui.QPixmap("Immagini/mano3.png"))
                self.count=5
        elif(self.flag_gioco== 1 and self.count == 5):
            self.predizione = modello.predict(pacchetto.reshape(1,-1))
            self.predizione = list(self.predizione)
            if(self.predizione[0] == 2):
                self.arco1.setPixmap(QtGui.QPixmap("Immagini/arco3.png"))
                self.timer.stop()
                self.today=QDateTime.currentDateTime()
                self.date_str = self.today.toString("yyyy-MM-dd hh:mm:ss")
                row=[self.nome_utente,self.date_str,self.count_timer]
                self.termine_gioco.setText("Complimenti {}! Hai completato il gioco in {} s".format(self.nome_utente,self.count_timer))
                self.termine_gioco.setAlignment(Qt.AlignmentFlag.AlignCenter)
                self.flag_gioco_terminato=1
                if (self.checkpoint==0):
                    with open('data_register.csv', mode='a', newline='') as f_object: 
                        writer = csv.writer(f_object)
                        writer.writerow(row)
                        self.checkpoint=1
                # Termine del gioco con salvataggio dei dati e risultati riguardanti il tempo impiegato
                
        # Gestione fallimento dell'esercizio
        if(self.count_timer>=30):
            row=[self.nome_utente,self.date_str,30]
            self.flag_gioco_terminato=1
            self.termine_gioco.setText("Esci dal gioco! Riprova!")
            self.termine_gioco.setAlignment(Qt.AlignmentFlag.AlignCenter)
            if (self.checkpoint==0):
                    with open('data_register.csv', mode='a', newline='') as f_object: 
                        writer = csv.writer(f_object)
                        writer.writerow(row)
                        self.checkpoint=1
        else:
            pass
    
    # Gestione tempo del gioco
    def count_time(self):
        self.secondi=self.secondi + 1
        if self.secondi==10:
            self.count_timer = self.count_timer + 1
            self.secondi=0
        self.delay=self.delay +0.1
    ## FINE FINESTRA GIOCO ##

    ## INIZIO FINESTRA STATISTICHE ##
    def initUIStatistiche(self):
        # Definizione layout
        self.layoutV_statistiche=QVBoxLayout()
        self.layoutV_statistiche.setSpacing(5)
        self.layoutH_batteria_statistiche=QHBoxLayout()
        self.layoutH_titolo_statistiche=QHBoxLayout()
        self.layoutH_titolo_statistiche.setContentsMargins(0,0,0,30)
        self.layout_grafico=QHBoxLayout()
        self.layoutH_risultati=QHBoxLayout()
        self.layoutH_risultati.setContentsMargins(0,20,0,0)
        self.layoutH_fallimenti=QHBoxLayout()
        self.layoutH_fallimenti.setContentsMargins(0,20,0,0)
        self.layout_uscita_statistiche = QGridLayout()
        self.layout_uscita_statistiche.setVerticalSpacing(20)

        # Funzione per visualizzazione del grafico
        self.plot()

        # Definizione Widgets
        # Titolo
        self.titolo_statistiche=QLabel("Statistiche di {}".format(self.nome_utente))
        self.titolo_statistiche.setFont(QtGui.QFont('Arial', 40))
        self.titolo_statistiche.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        # Icona batteria
        self.icona_batteria=QLabel("")
        pixmap=QtGui.QPixmap("Immagini/100.png")
        self.icona_batteria.setPixmap(pixmap)
        self.icona_batteria.resize(pixmap.width(),pixmap.height())
        self.icona_batteria.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.layoutH_batteria_statistiche.addWidget(self.icona_batteria)
        self.icona_batteria.setMargin(35)

        # Risultati
        self.risultato_migliore=QLabel("Tempo migliore in assoluto: {} s\nil {}".format(self.tempo_migliore, self.data_tempo_milgiore))
        self.risultato_migliore.setFont(QtGui.QFont('Arial', 30))
        self.risultato_migliore.setMaximumSize(1920,100)
        self.risultato_migliore.setMinimumSize(1920,100)

        self.risultato_peggiore=QLabel("Tempo peggiore in assoluto: {} s\nil {}".format(self.tempo_peggiore, self.data_tempo_peggiore))
        self.risultato_peggiore.setFont(QtGui.QFont('Arial', 30))
        self.risultato_peggiore.setMaximumSize(1920,100)
        self.risultato_peggiore.setMinimumSize(1920,100)

        self.fallimento=QLabel("Numero tentativi falliti: {}".format(self.count_fallimenti))
        self.fallimento.setFont(QtGui.QFont('Arial', 30))
        self.fallimento.setMaximumSize(1920,50)
        self.fallimento.setMinimumSize(1920,50)

        # Icona uscita
        self.uscita_statistiche = QLabel("Esci")
        self.uscita_statistiche.setFont(QtGui.QFont('Arial', 15))
        self.uscita_statistiche.setMaximumSize(1920,100)
        self.uscita_statistiche.setMinimumSize(1920,100)

        self.pollicesu=QLabel("")
        pixmap=QtGui.QPixmap("Immagini/pollicesu.png")
        self.pollicesu.setPixmap(pixmap)
        self.pollicesu.resize(pixmap.width(),pixmap.height())

        # Aggiunta widgets ai layout 
        self.layoutH_titolo_statistiche.addWidget(self.titolo_statistiche)
        self.layoutH_risultati.addWidget(self.risultato_migliore)
        self.layoutH_risultati.addWidget(self.risultato_peggiore)
        self.layoutH_fallimenti.addWidget(self.fallimento)
        self.layout_uscita_statistiche.addWidget(self.pollicesu,1,1)
        self.layout_uscita_statistiche.setHorizontalSpacing(10)
        self.layout_uscita_statistiche.addWidget(self.uscita_statistiche,1,2)

        # Aggiunta layout orizzontali al layout verticale
        self.layoutV_statistiche.addLayout(self.layoutH_batteria_statistiche)
        self.layoutV_statistiche.addLayout(self.layoutH_titolo_statistiche)
        self.layoutV_statistiche.addLayout(self.layout_grafico)
        self.layoutV_statistiche.addLayout(self.layoutH_risultati)
        self.layoutV_statistiche.addLayout(self.layoutH_fallimenti)
        self.layoutV_statistiche.addLayout(self.layout_uscita_statistiche)
        
        # Aggiunta layout verticale al widget
        self.widget_statistiche=QWidget()
        self.widget_statistiche.setLayout(self.layoutV_statistiche)
        self.setCentralWidget(self.widget_statistiche)

    ## Funzione per la creazione grafico ##
    def plot(self):
        # Lettura dati, controllo dell'utente e plot grafico
        df=pd.read_csv('data_register.csv', header=0)
        df=df[df['nome'] == self.nome_utente].reset_index(drop=True)
        data= df['data'].tail(10)
        time= df['durata'].tail(10)
        figure=plt.figure(figsize=(15,7))
        ax=figure.add_subplot(111)
        ax.barh(data,time)
        data = pd.to_datetime(data)
        data = [d.strftime('%Y-%m-%d') for d in data]
        plt.xticks(rotation=45)
        ax.set_yticklabels(data, rotation=0, ha='right')
        ax.set_xticks(range(0, max(time)+1))
        ax.axvline(x=30, color='red', linestyle='-', lw=1)
        figure.tight_layout()
        self.layout_grafico.addWidget(figure.canvas)
        
        df_range = df[(df['durata']>=0) & (df['durata']<30)]
        idx_tempo_peggiore = df_range['durata'].idxmax()
        self.tempo_peggiore= df_range.loc[idx_tempo_peggiore, 'durata']
        self.data_tempo_peggiore = df_range.loc[idx_tempo_peggiore, 'data']

        idx_tempo_migliore = df['durata'].idxmin()
        self.tempo_migliore= df.loc[idx_tempo_migliore, 'durata']
        self.data_tempo_milgiore = df.loc[idx_tempo_migliore, 'data']

        self.controllo_fallimenti= df['durata'].value_counts()
        self.count_fallimenti= self.controllo_fallimenti[30] if 30 in self.controllo_fallimenti else 0

        print(self.count_fallimenti)
## FINE FINESTRA GRAFICO ##

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainWindow()
    app.aboutToQuit.connect(w.ExitHandler)
    w.show()
    sys.exit(app.exec_())

