# Carta
    # Tiene
        # - palo (exto)
        # - numero (entero)
    # + imprimir(): Imprime el numero y el palo de la carta

class Carta:
    
    def __init__(self, numero, palo):
        self.palo = palo
        self.numero = numero
    
    def imprimir(self):
        print(self.numero, "de", self.palo)