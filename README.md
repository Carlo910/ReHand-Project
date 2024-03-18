# AY2223_I_Project-3

Re-Hand Versione 1.0 13/02/2023

***
Short Description:

Re-Hand is a device that uses 4 flex sensors, mounted on a glove, to recognize gestures. It is designed to be used in rehabilitation, to train subjects who experience problems in perfoming the "grasping" movement. Rehabilitation is done through repetition of the "grasping" gesture by playing a game by carrying out precise instructions given on the screen.
Breve descrizione:

Itlian version: 
Re-Hand è un dispositivo che utilizza 4 flex sensors, montati su di un guanto, per riconoscere dei gesti. 
E' stato pensato per essere utilizzato in ambito riabilitativo, per allenare soggetti che riscontrano problemi nel perfomare il
movimento del "grasping". 
La riabilitazione viene effettuata tramite la ripetizione del gesto del "grasping" svolgendo un gioco eseguendo precise istruzioni fornite a schermo. 

***

Hardware:

A glove is used on which four flex sensors, from thumb to ring finger, are sewn onto the top of the fingers. To read the value measured by the sensors, four voltage dividers (one for each sensor) were made with four 2 kOhm resistors. A PSoC 5LP Dev Kit CY8CKIT-059 was used as the microcontroller. The device was designed as a wearable, so it is equipped with a bluetooth module for sensor data communication and a 3.7 V lipo battery for power supply, with an attached charging circuit.  A 3.3 V linear stabilizer was added to provide the microcontroller with a stabilized voltage, while the Bluetooth gets an unstabilized voltage since the minimum voltage required to power it is 3.6 V.
To check the battery charge level, two identical 1 kOhm resistors were added to read the drop voltage across them.
After prototyping the device, a PCB was made into which all components were soldered. See the 'Eagle' folder to view the model made for printing the PCB.  A case was made thanks to a 3D printer to contain all the hardware components (apart from the sensors and glove). In the 'SolidWorks' folder you can find the model made for printing. It is possible to conveniently turn the device on and off by pressing a switch on the top side of the case. To monitor the bluetooth connection, the user can refer to a red LED located on the side of the case, which flashes at a frequency of 0.2 Hz during bluetooth connection and turns solid once the connection is successfully occurred.

***
PsoC Creator 
The Psoc Creator IDE (Integrated Design Environment) was used to develop the project from the firmware side. 
Within the 'PSOC' folder can be found the 'Project3' workspace which contains the 'Project3' project where the code used to sample the data, average it and finally send it via Bluetooth to the connected device. 
For data sampling, the frequency of the interrupt timer was set to 10 Hz. Once a piece of data is received, it waits to have 10 samples in order to average them and then send them. In addition, every minute the
the battery charge value and then sent. Also managed within the code is the Bluetooth connection and its Led to display whether it has taken place (Led on) or not (Led flashes at 0.2 Hz). In addition, there is the project 'Project3_dataset' which was used to build the datasets for the development of the classifier. A different code is used to make data collection easier by simplifying the connection with the  device that receives the data.

***

Python

To use Re-Hand you need version 3.9 with various libraries to install on your virtual enviroment.
See the file 'requirements.txt' in the folder and run it in your virtual  
environment to install all the required libraries with their respective versions.
 
Upon launching the GUI.py code, the name of the Re-Hand project appears on the screen and the user will be asked to enter their name, thanks to which it will be possible to save performance data from different users. Next, the user can click  a start button, which allows the start of sampling the values of the four variable resistors. In case the user has not entered the name, he/she will not be able to access the second screen and an error message will be displayed on asscreen. Once the start button is pressed, a new screen is opened where the user can choose whether to play the game, or display on the screen some statistical data on the improvement in playing it. 

Thanks to a classifier, specifically a Random Forest, the device can recognize six gestures in total, three used to move through the different GUI windows and three for the rehabilitation task. In the file 'classification_6gestures.ipynb' it is possible to see how the model used for the classification of the gestures. The files 'dataset_training_6gesti.csv' and 'dataset_test_6gesti.csv' contain all the data used to
train and test the model which were collected using the code 'code_dataset.py'. In the file 'rf_model_6gesti.pkl' is saved the model trained on the datasets mentioned above and used to perform real-time prediction for gesture recognition while using the application.

By raising only the index finger (target 4), one enters the game window. At this point the user can start performing the gesture
of grasping, starting with the hand fully open (target 0), then trying to close it halfway (target 1) and finally closing the fist completely (target 2). While performing these gestures, the user will be able to see on the screen an image of a bow being drawn, progressively as the hand closes, until an arrow is fired. Once the game is finished, the time it took the user to complete the gesture is printed on the screen. In the event that the exercise is not performed correctly (time taken longer than 30 seconds) a message will be displayed on the screen a message inviting the user to exit the game and try again. By raising only the thumb while keeping the hand closed (target 3), you will exit the game screen and return to the main Home screen. 

At this point, by raising both index and average (target 5) you can enter the statistics screen, where a graph can be displayed on the screen showing the times in seconds in which the user has done the last ten exercises, if any, with the respective date so that any improvements can be visualized. The display of statistics is allowed only if the user has completed the game at least twice, otherwise an error message appears on the screen. The following graph also shows failed attempts by reporting a time of 30 seconds (the maximum attainable value), highlighted on the graph by a red line. The user's best result, absolute worst result (in case of success) and the number of failed attempts are also displayed. By raising only the thumb while keeping the hand closed (target 3), you exit the game screen to return to the main Home screen. 

***

Italian version:

Hardware:
Si utilizza un guanto su cui sono cuciti quattro flex sensors, dal pollice all'anulare, sulla parte superiore delle dita. Per leggere
il valore misurato dai sensori sono stati realizzati 4 partitori di tensione (uno per ogni sensore) con 4 resistenze da 2 kOhm.
Come microcontrollore è stato usato un PSoC 5LP Dev Kit CY8CKIT‐059.  
Il device è stato pensato come wearble, per cui è dotato di modulo bluetooth per la comunicazione dei dati dei sensori e di una batteria lipo a 3.7 V per
l'alimentazione, con annesso circuito di ricarica. 
E' stato aggiunto uno stabilizzatore lineare a 3.3 V per fornire al microcontrollore una tensione stabilizzata, mentre al modulo
bluetooth arriva una tensione non stabilizzata poichè la minima tensione richiesta per alimentarlo è di 3.6 V.
Per controllare il livello di carica della batteria sono state aggiunte due resistenze identiche da 1 kOhm per leggere la caduta
di tensione su di esse.
Dopo aver realizzato il dispositivo in via prototipale è stata realizzata una PCB in cui sono stati saldati tutti i componenti.
Vedere la cartella 'Eagle' per visualizzare il modello realizzato per la stampa della PCB. 
Per contenere tutti i componenti hardware (a parte i sensori e guanto) è stato realizzato un case grazie ad una stampante 3D. Nella
cartella 'SolidWorks' è possibile trovare la realizzazione del modello per la stampa.
E' possibile accendere e spegnere comodamente il dispositivo premendo un interruttore posto sul lato superiore del case.
Per monitorare la connessione del bluetooth, l'utente può fare riferimento a un led rosso posizionato lateralmente al case, il quale
lampeggia a una frequenza di 0,2 Hz durante la connessione del bluetooth e diventa fisso una volta che la connessione è correttamente
avvenuta.

***

PsoC Creator 
E' stato utilizzato il Psoc Creator IDE (Integrated Design Environment) per sviluppare il progetto dal lato firmware. 
All'interno della cartella 'PSOC' si può trovare il workspace 'Project3' il quale contiene il progetto 'Project3' dove si trova il 
codice utilizzato per campionare i dati, mediarli e infine inviarli tramite Bluetooth al dispositivo connesso. 
Per il campionamento dei dati è stata impostata la frequenza del timer dell'interrupt a 10 Hz. Una volta ricevuto un dato si attende
di avere 10 campioni per poter calcolare la media di questi ultimi e successivamente inviarli. In aggiunta ogni minuto viene misurato
il valore di carica della batteria e poi inviato.
All'interno del codice è gestita anche la connessione del Bluetooth e il relativo Led per visualizzare se è avvenuta (Led acceso)
oppure no (Led lampeggia a 0,2 Hz).
Inoltre è presente il progetto 'Project3_dataset' il quale è stato usato per la realizzazione dei dataset per lo sviluppo del 
classificatore. Viene usato un codice diverso per rendere la raccolta dei dati più agevole semplificando la connessione con il 
dispositivo che riceve i dati.

***

Python

Per utilizzare Re-Hand è necessaria la versione 3.9 con varie librerie da installare sul prorpio virtual enviroment.
Vedere nella cartella il file 'requirements.txt' e eseguirlo nel prorpio virtual  
environment per installare tutte le librerie necessarie con le rispettive versioni.
 
Lanciando il codice GUI.py appare a schermo il nome del progetto Re-Hand e verrà chiesto all'utente di inserire il proprio 
nome, grazie al quale sarà possibile salvare i dati delle prestazioni di diversi utenti. In seguito l'utente può cliccare 
un pulsante di start, che permette l'inizio del campionamento dei valori delle quattro resistenze variabili.
Nel caso in cui l'utente non abbia inserito il nome, non potrà accedere alla seconda schermata e verrà visualizzato a aschermo un messaggio di errore.
Una volta premuto il pulsante di start, viene aperta una nuova schermata dove l'utente può scegliere se svolgere il gioco, 
oppure visualizzare a schermo alcuni dati statistici sul miglioramento nello svolgimento dello stesso.

Grazie a un classificatore, in particolare un Random Forest, il dispositivo riesce a riconoscere sei gesti in totale,
tre utilizzati per muoversi attraverso le diverse finestre della GUI e tre per l'attività di riabilitazione.
Nel file 'classification_6gesti.ipynb' è possibile visualizzare come è stato realizzato il modello usato per la
classificatione dei gesti. I files 'dataset_training_6gesti.csv' e 'dataset_test_6gesti.csv' contengono tutti i dati usati per
allenare e testare il modello i quali sono stati raccolti utilizzando il codice 'codice_dataset.py'. Nel file 'rf_model_6gesti.pkl' è
salvato il modello allenato sui dataset citati sopra e usato per compiere la predizione i tempo reale per il riconoscimento dei gesti
durante l'utilizzo dell'applicazione.

Alzando solo l'indice (target 4), si entra nella finestra del gioco. A questo punto l'utente può iniziare a performare il gesto
del grasping, partendo con la mano completamente aperta (target 0), provando poi a chiuderla a metà (target 1) e infine
chiudendo completamente il pugno (target 2). Durante l'esecuzione di questi gesti, l'utente potrà visualizzare a schermo
l'immagine di un arco che viene tirato, progressivamente alla chiusura della mano, fino a scoccare una freccia. 
Una volta finito il gioco viene stampato a schermo il tempo che l'utente ha impiegato per completare il gesto.
Nel caso in cui l'esercizio non venga svolto correttamente (tempo di svolgimento superiore a 30 secondi) verrà visualizzato 
a schermo un messaggio che inviterà l'utente a uscire dal gioco e a riprovare. Alzano solo il pollice mantenendo la mano chiusa
(target 3), si esce dalla schermata del gioco per tornare nella schermata Home principale. 
 
A questo punto, alzando sia indice che medio (target 5) è possibile entrare nella schermata delle statistiche,
dove si può visualizzare a schermo un grafico che mostra i tempi in secondi in cui l'utente ha svolto gli ultimi dieci l'esercizi, se presenti, con la rispettiva
data in modo da poter visualizzare gli eventuali miglioramenti. La visualizzazione delle statistiche viene permessa solo se
l'utente ha completato almeno due volte il gioco, in caso contrario appare a schermo un messaggio di errore.
Il seguente grafico inoltre mostra anche i tentativi falliti riportando un tempo di 30 secondi (il massimo valore raggiungibile),
evidenziato sul grafico da una linea rossa.
Vengono inoltre visualizzati il risultato migliore, quello peggiore in assoluto dell'utente (in caso di successo) e il numero di tentativi falliti.
Alzano solo il pollice mantenendo la mano chiusa
(target 3), si esce dalla schermata del gioco per tornare nella schermata Home principale. 

