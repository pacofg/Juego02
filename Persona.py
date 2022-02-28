# Persona
    # Tiene
        # - nombre (texto)
        # - edad (entero)
    # + bautizar(): Daremos nombre a la persona
    # + saludar(): La persona se presenta
    # + cumplir años(): Incrementamos la edad en 1

class Persona:

    def __init__(self):
        self.nombre = ''
        self.edad = 0

    def bautizar(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def saludar(self):
        print("Hola me llamo", self.nombre, " y tengo", self.edad)

    def cumplir_anyos(self):
        self.edad = self.edad + 1