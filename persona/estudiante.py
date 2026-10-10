class Estudiantes:
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
perona1 = Estudiantes("asd","asd","asd57",1457896,125,"Aasdd")
perona1.mostrar_informacion()
