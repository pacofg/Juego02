class Carta:
    
    def __init__(self):
        self.palo = "Espadas"
        self.numero = 8
    
    def imprimir(self):
        print(self.numero, "de", self.palo)

 # Esto genera una instancia d la clase Carta
carta1 = Carta()
carta1.imprimir()