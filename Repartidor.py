# El repartidor crea una baraja que sera unica para todos los jugadores,
# se la ira pasando segun la necesiten
from Mazo import Mazo
from Jugador import Jugador

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
            if(resultado > valor and resultado < 0):
                valor = resultado
                ganador = i
            
            print("La suma de", i, "es",suma)
            
            self.resultados.append(resultado)
        
        
        print("Los resultado son", self.resultados, self.jugadores[ganador].nombre)



j1 = Jugador("Jugador-1")
j2 = Jugador("Jugador-2")
repartidor = Repartidor([j1,j2])
repartidor.jugar()