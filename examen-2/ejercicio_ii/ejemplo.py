from circulo import Circulo
from rectangulo import Rectangulo
from triangulo import Triangulo

circulo=Circulo(5.56)
circulo.calcular_area()

rectangulo=Rectangulo(4,6.456)
rectangulo.calcular_area()

triangulo=Triangulo(3,5.51)
triangulo.calcular_area()
print("************************************************************")
print("Ahora calculamos el area de todas las figuras en una lista")
lista_figuras=[circulo,rectangulo,triangulo]
for figura in lista_figuras:
    figura.calcular_area()
