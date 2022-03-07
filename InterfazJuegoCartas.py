from email.mime import image
from tkinter import *

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
                
         # Mostramos la ventan
        self.ventana.mainloop()
         # Cualquier cosa que tengamos despues ya no se vera


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
        


def main():
    interfaz = InterfazJuegoCartas()
    
if __name__ == "__main__":
    main()