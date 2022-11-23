import serial


from enum import Enum
class Gesture(Enum):
    POLLICE = [0,0XFF,0,0]
    APERTA = [0,0,0,0]

class Packet():
    
    lista = list()

    def __init__(self, pacchetto : bytes) -> None:
        self.lista = list(pacchetto)

    def getGesture(self) -> Gesture:
        return Gesture(self.lista[1:5])
                 


        



def main():
    # initialization
    ser = serial.Serial()
    ser.baudrate = 9600
    ser.port = 'COM7'
    while(not ser.is_open):
        try:
            ser.open()
        except:
            print("Didn't connect, trying again")
    #while(ser.is_open):
    dato = ser.read(6)
    print(dato, type(dato))
    packet = Packet(dato)
    #lista = packet.getList()
    #print(lista)
    #if packet.isOpponibile():
    #    print("callback to w")
    print(packet.getGesture())
        

    





if __name__ == "__main__":
    main()
    