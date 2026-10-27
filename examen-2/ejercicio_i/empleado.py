class Empleado:
    def __init__(self, nombre, identifiacion):
        self.nombre = nombre
        self.identificacion = identifiacion

    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}, \nIdentificacion:{self.identificacion}")
