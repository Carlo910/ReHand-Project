import serial

THRESHOLD = 80


from enum import Enum
class Gesture(Enum):
    CACCA = [0,0XFF,0,0]
    PUZZETTA = [0,0,0,0]

class Packet():
    
    lista = list()
    gestures = list()

    def __init__(self, pacchetto : bytes) -> None:
        self.lista = list(pacchetto)

    #def getList(self):
        """
        newLista = list()
        for number in self.lista:

            if number == 160 or number == 192:
                continue
            elif number > THRESHOLD:
                newLista.append(1)
            else:
                newLista.append(0)
        self.gestures = newLista
        """
        #return self.lista[1:4]
    """
    def isOpponibile(self) -> bool:
        if self.gestures[1] == 1:
            return True
        else:
            return False
    """
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
    