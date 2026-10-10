class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def mostrar_datos(self):
        print(f"Nombre de persona es: {self.nombre}")
        print(f"Edad de {self.nombre} es {self.edad}")

nombre = str(input("Ingrese el nombre: "))
edad = str(input("Ingrese la edad: "))
persona1 = Persona(nombre, edad)
persona1.mostrar_datos()
nombre = str(input("Ingrese el nombre: "))
edad = str(input("Ingrese la edad: "))
persona2 = Persona(nombre, edad)
persona2.mostrar_datos()