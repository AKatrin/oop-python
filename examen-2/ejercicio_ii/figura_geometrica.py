class FiguraGeometrica:
    def __init__(self, nombre):
        self.nombre = nombre

    def calcular_area(self):
        raise NotImplementedError("El método area() debe ser implementado por la subclase.")
    
