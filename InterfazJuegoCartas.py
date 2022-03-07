from email.mime import image
from tkinter import *
from turtle import width

class InterfazJuegoCartas:
    
    def __init__(self):
        self.ventana = Tk()
        self.ventana.geometry('1200x600')
        
         # Creamos un canvas del mismo tamaño que la ventana
        self.canvas = Canvas(self.ventana, width=1200, height=600)
         # Crea un bloque con los elementos del canvas
        self.canvas.pack()

         # Cargamos el fondo de la ventana
        self.dibujar_fondo()
                
         # Fondo de la carta como un poligono de fondo blanco y borde negro
        # self.dibujar_poligono([50,170,170,50], [55,55,230,230], fill='#FFFFFF', width=2, outline='#000000')
        self.dibujar_rectangulos(4, 50, 55, 120, 175, 5)
         # Dibujamos una carta
        self.dibujar_carta()
        
        self.dibujar_etiquetas()
                
         # Mostramos la ventan
        self.ventana.mainloop()
         # Cualquier cosa que tengamos despues ya no se vera

    def dibujar_etiquetas(self):
        etiqueta = Label(self.ventana, text="Computadora 1", background='Green', foreground='White', font='arial 15 bold')
        etiqueta.place(x=50, y=20)
        etiqueta = Label(self.ventana, text="Jugador 1", background='Green', foreground='White', font='arial 15 bold')
        etiqueta.place(x=50, y=360)
        
        
    def dibujar_rectangulos(self, cantidad, xInicio, yInicio, xTam, yTam, margen=10):
        for i in range(cantidad):
            self.dibujar_poligono([xInicio, xInicio+xTam, xInicio+xTam, xInicio], [yInicio, yInicio, yInicio+yTam, yInicio+yTam], fill='#FFFFFF', width=2, outline='#000000')
            xInicio = xInicio + xTam + margen
        
        
    def dibujar_poligono(self, x, y, **args):
        puntos = []
        for i in range(len(x)):
            puntos.append(x[i])
            puntos.append(y[i])
        
         # Punto inicial para cerra rel poligono
        puntos.append(x[0])
        puntos.append(y[0])
        
        return self.canvas.create_polygon(puntos, **args)    
        
    def dibujar_fondo(self):
         # Cargamos el archivo con la imagen a pintar
        fondo = PhotoImage(file='juegoCartas/fondo-verde.png')
        imagen = Label(image=fondo)
        imagen.image = fondo
        
         # Dibujamos la imagen en el canvas
         # Dibuja varias en diferentes posiciones para llenar la ventana
        self.canvas.create_image(300,200, image=fondo)
        self.canvas.create_image(300,400, image=fondo)
        self.canvas.create_image(900,200, image=fondo)
        self.canvas.create_image(900,400, image=fondo)
        
         # Creamos el adorno para el fondo
        adornos = PhotoImage(file='juegoCartas/adornos.png')
        imagen = Label(image=adornos)
         # Reescalamos la imagen 6 veces
        adornos = adornos.subsample(6)
        imagen.image = adornos
         # Lo incorpora al canvas, jugando con la posicion para dejarlo bien
        self.canvas.create_image(1100,500, image=adornos)
        
    def dibujar_carta(self, x=110, y=143, imagen='juegoCartas/2_de_espadas.png'):
        imagen_canvas = PhotoImage(file=imagen)
        imagen_canvas = imagen_canvas.subsample(2)
        imagen_label = Label(image=imagen_canvas)
        imagen_label.image = imagen_canvas
        self.canvas.create_image(x, y, image=imagen_canvas)

def main():
    interfaz = InterfazJuegoCartas()
    
if __name__ == "__main__":
    main()