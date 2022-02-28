 # Importamos del archivo Carta la clase Carta
from Carta import Carta

class Mazo:

    def __init__(self):
        self.carta1 = Carta(7, "Diamantes")
        self.carta2 = Carta(4, "Espadas")
    
    def imprimir(self):
        self.carta1.imprimir()
        self.carta2.imprimir()
    

mazo1 = Mazo()
mazo1.imprimir()