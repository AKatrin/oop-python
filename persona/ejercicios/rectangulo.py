class Rectanglo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    def calcular_area(self):
        print(f"El area del rectangulo es: {self.altura * self.base}")
    
    def calcular_perimetro(self):
        print(f"El perimetro del rectangulo es: {(self.altura + self.base)*2}")

base = int(input("Ingrese el valor de base: "))
altura = int(input("Ingrese el valor de altura: "))
rectangulo1=Rectanglo(base, altura)
rectangulo1.calcular_area()
rectangulo1.calcular_perimetro()