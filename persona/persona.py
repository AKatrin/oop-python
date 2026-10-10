class Estudiante:
    def __init__(self, nombre, apellidos, ci, celular, edad, direccion):
        self.nombre = nombre
        self.apellidos = apellidos
        self.ci = ci
        self.celular = celular
        self.edad = edad
        self.direccion = direccion
    
    def mostrar_informacion(self):
        print(f"Su nombre es: {self.nombre}")
        print(f"Sus apellidos son: {self.apellidos}")
        print(f"Su ci es: {self.ci}")
        print(f"Su celular es: {self.celular}")
        print(f"Su edad es: {self.edad}")
        print(f"Su direccion es: {self.direccion}")

persona1 = Estudiante("Maria", "Castro", "54sd", 70707070, 18, "av. Villazon")        
persona1.mostrar_informacion()

persona2 = Estudiante("Marcos", "Vargas", "78954as", 77777777, 100, "av. America")        
persona2.mostrar_informacion()