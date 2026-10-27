from figura_geometrica import FiguraGeometrica
class Rectangulo(FiguraGeometrica):
    def __init__(self, base, altura):
        super().__init__("Rectángulo")
        self.base = base
        self.altura = altura

    def calcular_area(self):
        area = (self.base * self.altura)
        print(f"El area del {self.nombre} es: {round(area, 2)}")
        