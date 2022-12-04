import serial
import csv

def main():
    # initialization
    sample=0
    ser = serial.Serial()
    ser.baudrate = 9600
    ser.port = 'COM5'

    #da usare la prima volta
    '''
    with open('dataset.csv', mode='w',newline='') as csv_file:
        nomecolonne=['dito1', 'dito2', 'dito3','dito4']
        writer = csv.DictWriter(csv_file,fieldnames=nomecolonne)
        writer.writeheader()
    '''
    

    while(not ser.is_open):
        try:
            ser.open()
        except:
            print("Didn't connect, trying again")
            
    while(ser.is_open and sample<100):
        dato = ser.read(10)
        print(dato, type(dato))
        sample += 1

        if(dato[0]==160 and dato[9]==192): 
            valore=list(dato[1:9])
            final = []
            i = 0
            while(i < len(valore) - 1):
                final.append((valore[i] << 8) + valore[i+1])
                i += 2
            print(final)
            print(sample)

            
            with open('dataset.csv', mode='a', newline='') as f_object: 
                writer = csv.writer(f_object)
                writer.writerow(final)
            
     
        
if __name__ == "__main__":
    main()
    