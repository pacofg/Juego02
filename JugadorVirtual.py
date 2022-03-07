# Debe contener cartas (instancias)
# Tener la capacidad de solicitar cartas (jugar)
# Imprimir sus cartas
# Poder sumar el valor de sus cartas

from ctypes.wintypes import PUSHORT
from mailbox import NoSuchMailboxError
from socket import CAN_BCM_RX_STATUS
from Interfaz import Interfaz
from Mazo import Mazo

class JugadorVirtual:
    
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
    
    def imprimir_juego(self):
        cartas = ["_"]
        for i in range(1, len(self.cartas)):
            cartas.append(self.cartas[i].numero)
        print(cartas)
    
    def jugar(self, mazo):
         # Seguira la regla de pedir carta si su suma < 16
         
        while(self.sumar_cartas() < 16):
            self.cartas.append(mazo.obtener_siguiente_carta())
                
        self.imprimir_juego()
         # Devolvemos la suma de las cartas del jugador
        return self.sumar_cartas()


if __name__ == "__main__":
    mazo = Mazo()
    jugador1 = JugadorVirtual("Juan")
    jugador1.jugar(mazo)