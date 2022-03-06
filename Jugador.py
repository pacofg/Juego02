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
    
    def jugar(self, mazo):
        interfaz = Interfaz()
        solicitar = True
        titulo = "Opciones:\n1- Pedir Carta\n2- Quedarse\nValor:"
        
        while(solicitar and self.sumar_cartas() <= 21):
             # Le mostramos al jugador sus cartas
            self.imprimir()
             # Le solicitamos la accion a realizar
            valor = interfaz.solicitar_numero_entero(titulo)
            if(valor == 1):     # El jugador solicita una carta
                 # Se agrega a las cartas del jugador la que se le ha repartido
                self.cartas.append(mazo.obtener_siguiente_carta())
                 # Neva carta repartida
                self.cartas[-1].imprimir()
            elif(valor == 2):
                solicitar = False
                
         # Devolvemos la suma de las cartas del jugador
        return self.sumar_cartas()


if __name__ == "__main__":
    mazo = Mazo()
    jugador1 = Jugador("Juan")
    jugador1.jugar(mazo)