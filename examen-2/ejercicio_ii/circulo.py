from figura_geometrica import FiguraGeometrica
class Circulo(FiguraGeometrica):
    def __init__(self, radio):
        super().__init__("Círculo")
        self.radio = radio

    def calcular_area(self):
        area = 3.14 * (self.radio ** 2) 
        print(f"El area del {self.nombre} es: {round(area, 2)}")
  