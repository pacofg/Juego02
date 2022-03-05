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
        numero_t = self.convertir_numero_a_letras()
        print(numero_t, "de", self.palo)
        
    def convertir_numero_a_letras(self):
        valor = ""
        
        if (self.numero == 11):
            valor = "J"
        elif(self.numero == 12):
            valor = "Q"
        elif(self.numero == 13):
            valor = "K"
        elif(self.numero == 1):
            valor = "As"
        else:
            valor = str(self.numero)
        
        return valor

    def obtener_numero(self):
         # Las figuras valen 10
        return 10 if self.numero > 10 else self.numero

def main():
    carta = Carta(11, "Tréboles")
    carta.imprimir()
    carta = Carta(12, "Tréboles")
    carta.imprimir()
    carta = Carta(13, "Tréboles")
    carta.imprimir()
    carta = Carta(1, "Tréboles")
    carta.imprimir()
    carta = Carta(7, "Tréboles")
    carta.imprimir()

if __name__ == "__main__":
    main()