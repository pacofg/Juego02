 # Importamos del archivo Carta la clase Carta
from Carta import Carta
import random

class Mazo:

    def __init__(self):
         # Lista para almacenar los objetos Carta creados
        self.cartas = []
        self.crear_mazo()
    
    def crear_mazo(self):
        simbolos = ["Tréboles", "Diamantes", "Corazones", "Espadas"]
        for j in range(0, 4):
            for i in range(1, 14):
                carta = Carta(i, simbolos[j])
                 # Guardamos la carta en la lista
                self.cartas.append(carta)

    def revolver(self):
        # Vamos a intercambiar al menos una vez todoas las cartas de la lista
        # Iteramos sobre el índice de las celdas, no sobre el contenido
        for celda in range(len(self.cartas)):            
             # Entero aleatorio entre 0 y 51 que cambiara en cada iteracion
            aleatorio = random.randint(0,51)  
             # temp = c[x]
             # c[x] = c[y]
             # c[y] = temp
            temporal = self.cartas[celda]
            self.cartas[celda] = self.cartas[aleatorio]
            self.cartas[aleatorio] = temporal
            
    def imprimir(self):
         # Iteramos sobre los objetos Carta de la lista
        for instanciaCarta in self.cartas:
            instanciaCarta.imprimir()
                
    
    
mazo1 = Mazo()
mazo1.imprimir()
print("::::::::::::::::::::::::::::::")
mazo1.revolver()
mazo1.imprimir()