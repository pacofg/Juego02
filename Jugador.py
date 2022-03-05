# Debe contener cartas (instancias)
# Tener la capacidad de solicitar cartas (jugar)
# Imprimir sus cartas
# Poder sumar el valor de sus cartas

from mailbox import NoSuchMailboxError
from socket import CAN_BCM_RX_STATUS
from Interfaz import Interfaz
from Mazo import Mazo

class Jugador:
    def __init__(self, nombre, cartas = []):
        self.nombre = nombre
        self.cartas = cartas
        
    def asignar_cartas(self, cartas):
        self.cartas = cartas
        
    def imprimir(self):
        print(self.nombre, "estas son sus cartas")
        for carta in self.cartas:
            carta.imprimir()
        
        print ("Suma: ", self.sumar_cartas())
        
    def sumar_cartas(self):
        suma = 0
         # Un as vale 1 o 11, según le convenga al jugador
        aces = 0
        for carta in self.cartas:
            valor = carta.obtener_numero()
            if (valor == 1):
                aces += 1
                
            suma += valor
        
        if (aces > 0 and suma + 10 <= 21):
            suma += 10
        
        return suma
    