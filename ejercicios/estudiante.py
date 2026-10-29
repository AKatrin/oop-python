class Estudiante:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        
est_1=Estudiante("Juan", 20)
print(f"Nombre: {est_1.nombre}, Edad: {est_1.edad}")
est_1.edad = 21

print(f"Nombre: {est_1.nombre}, Edad: {est_1.edad}")        