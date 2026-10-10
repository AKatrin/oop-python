class EstudiantePromediado:
    def __init__(self, nombre, nota1, nota2):
        self.nombre = nombre
        self.nota1 = nota1
        self.nota2 = nota2

    def calcular_promedio(self):
        promedio = (self.nota1 + self.nota2) // 2
        if promedio > 51 or promedio == 51:
            print(f" El estudiante {self.nombre} aprobo con {promedio}")
        else:
            print(f" El estudiante {self.nombre} reprobo con {promedio}")

nombre = str(input("Ingrese el nombre: "))
nota1 = int(input("Ingrese la nota 1: "))
nota2 = int(input("Ingrese la nota 2: "))

estudiante = EstudiantePromediado(nombre, nota1, nota2)
estudiante.calcular_promedio()