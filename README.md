# AY2223_I_Project-3

Re-Hand Versione 1.0 13/02/2023

***
Breve descrizione:

Re-Hand è un dispositivo che utilizza 4 flex sensors, montati su di un guanto, per riconoscere dei gesti. 
E' stato pensato per essere utilizzato in ambito riabilitativo, per allenare soggetti che riscontrano problemi nel perfomare il
movimento del grasping. 
La riabilitazione viene effettuata tramite la ripetizione del gesto del grasping secondo precise istruzioni fornite a schermo 
tramite l'ausilio di un gioco. 

***

Hardware:

Si utilizza un guanto su cui sono cuciti quattro flex sensors, dal pollice all'anulare, sulla parte superiore delle dita. Per leggere
il valore misurato dai sensori sono stati realizzati 4 partitori di tensione (uno per ogni sensore) con 4 resistenze da 2 kOhm.
Come microcontrollore è stato usato un PSoC 5LP Dev Kit CY8CKIT‐059.  
E' un device werable, per cui è dotato di modulo bluetooth per la comunicazione dei dati dei sensori e batteria lipo a 3.7 V per
l'alimentazione, con annesso circuito di ricarica. 
E' stato aggiunto uno stabilizzatore lineare a 3.3 V per fornire al microcontrollore una tensione stabilizzata, mentre al modulo
bluetooth arriva una tensione non stabilizzata poichè la minima tensione richiesta per alimentarlo è di 3.6 V.
Per controllare il livello di carica della batteria sono state aggiunte due resistenze identiche da 1 kOhm per leggere la caduta
di tensione su di esse.
Dopo aver realizzato il dispositivo in via prototipale è stata realizzata una pcb in cui sono stati saldati tutti i componenti.
Vedere la cartella 'Eagle' per visualizzare il modello realizzato per la stampa della pcb. 
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
Vedere nella cartella 'Additional files' il file 'requirements.txt' e eseguirlo nel prorpio virual
environment per installare tutte le librerie necessarie con le rispettive versioni.
 
Lanciando il codice GUI.py appare a schermo il nome del progetto Re-Hand e verrà chiesto all'utente di inserire il proprio 
nome, grazie al quale sarà possibile salvare i dati delle prestazioni di diversi utenti. In seguito l'utente può cliccare 
un pulsante di start, che permette l'inizio del campionamento dei valori delle quattro resistenze.  
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
l'immagine di un arco che viene tirato, man mano che la mano si chiude, fino a scoccare una freccia. 
Una volta finito il gioco viene stampato a schermo il tempo che l'utente ha impiegato per completare il gesto.
Nel caso in cui l'esercizio non venga svolto correttamente (tempo di svolgimento superiore a 30 secondi) verrà visualizzato 
a schermo un messaggio che inviterà l'utente a uscire dal gioco e a riprovare. Alzano solo il pollice mantenendo la mano chiusa
(target 3), si esce dalla schermata del gioco per tornare nella schermata Home principale. 
 
A questo punto, alzando sia indice che medio (target 5) è possibile entrare nella schermata delle statistiche,
dove si può visualizzare a schermo un grafico che mostra i tempi in secondi in cui l'utente ha svolto l'esercizio con la ripettiva
data e ora in modo da poter visualizzare gli eventuali miglioramenti. La visualizzazione delle statistiche viene permessa solo se
l'utente ha completato almeno due volte il gioco. 
Il seguente grafico inoltre mostra anche i tentativi falliti riportanto un tempo di 30 secondi (il massimo valore raggiungibile),
questo valore limite è evidenziato da una linea rossa.
Vengono inoltre visualizzati il risultato migliore e peggiore in assoluto dell'utente.
