# El repartidor crea una baraja que sera unica para todos los jugadores,
# se la ira pasando segun la necesiten
from Mazo import Mazo
from Jugador import Jugador
from JugadorVirtual import JugadorVirtual

class Repartidor:
    
    def __init__(self, lista_jugadores):
        self.jugadores = lista_jugadores
        self.resultados = []
        self.mazo = Mazo()
        
    def repartir_cartas(self):
        for jugador in self.jugadores:
             # A cada jugador le repartimos 2 cartas
            cartas = [self.mazo.obtener_siguiente_carta(), self.mazo.obtener_siguiente_carta()]
             # Le asignamos al jugador las cartas que le han tocado
            jugador.asignar_cartas(cartas)
            
    
    def jugar(self):
        ganador = 0
        valor = 0
         # Para empezar a jugar barajamos las cartas
        self.mazo.revolver()
         # Repartimos 2 cartas a cada jugador
        self.repartir_cartas()
        
        print("Juego iniciado hay:", len(self.jugadores))
        
        for i in range(len(self.jugadores)):
            suma = self.jugadores[i].jugar(self.mazo)
            resultado = 21 - suma
             # Gana el que este mas cerca de 21 sin pasarse
             # En caso de empate en la puntuacion ganara el que tenga menos cartas
            if(resultado > valor and resultado < 0 or (resultado == valor and 
                       len(self.jugadores[i].cartas) < len(self.jugadores[ganador].cartas))):
                valor = resultado
                ganador = i
            
            print("La suma de", i, "es",suma)
            
            self.resultados.append(resultado)
        
        
        print("Los resultado son", self.resultados, self.jugadores[ganador].nombre)



if __name__ == "__main__":
    j1 = Jugador("Jugador-1")
    j2 = JugadorVirtual("PC-1")
    repartidor = Repartidor([j1,j2])
    repartidor.jugar()