from figura_geometrica import FiguraGeometrica
class Triangulo(FiguraGeometrica):
    def __init__(self, base, altura):
        super().__init__("Triángulo")
        self.base = base
        self.altura = altura

    def calcular_area(self):
        area = (self.base * self.altura) / 2
        print(f"El area del {self.nombre} es:  {round(area, 2)}")