import serial

'''
from enum import Enum
class Gesture(Enum):
    POLLICE = [255,255,0,0]
    APERTA = [0,0,0,0]

class Packet():
    
    lista = list()

    def __init__(self, pacchetto : bytes) -> None:
        self.valore = list(pacchetto)

    def getGesture(self) -> Gesture:
        return Gesture(self.lista[1:5])
                
'''
def main():
    # initialization
    ser = serial.Serial()
    ser.baudrate = 9600
    ser.port = 'COM9'
    while(not ser.is_open):
        try:
            ser.open()
        except:
            print("Didn't connect, trying again")
    while(ser.is_open):
        dato = ser.read(10)
        print(dato, type(dato))
    #packet = Packet(dato)
    #lista = packet.getList()
    #print(lista)
    #if packet.isOpponibile():
    #    print("callback to w")
    #print(packet.getGesture())
        

if __name__ == "__main__":
    main()
    