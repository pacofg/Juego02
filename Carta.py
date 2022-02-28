class Carta:
    
    def __init__(self, numero, palo):
        self.palo = palo
        self.numero = numero
    
    def imprimir(self):
        print(self.numero, "de", self.palo)

 # Esto genera una instancia d la clase Carta
carta1 = Carta(10, "Diamantes")
carta1.imprimir()

carta1 = Carta(7, "Espadas")
carta1.imprimir()