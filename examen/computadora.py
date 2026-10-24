class Computadora:
    def __init__(self, marca, procesador, memoria_ram, precio):
        self.marca = marca
        self.procesador = procesador
        self.memoria_ram = memoria_ram
        self.precio = precio
    
    def mostrar_informacion(self):
        print(f"Marca: {self.marca}")
        print(f"Procesador: {self.procesador}")
        print(f"Memoria RAM: {self.memoria_ram} GB")
        print(f"Precio: Bs. {self.precio:.2f}")
        
    def evaluar_rendimiento(self):
        rendimiento = ""
        if self.memoria_ram >= 16:
            rendimiento = "alto"
        elif self.memoria_ram >= 8 and self.memoria_ram < 16:
            rendimiento = "intermedio"
        else:
            rendimiento= "basico"
            
        print(f"Rendimiento {rendimiento}")    
        
    def calcular_costo_total(self, cantidad):
        total=0
        for i in range(cantidad):
            total += self.precio
        print(f"Costo de {cantidad} computadoras es: Bs. {total:.2f}")
        
        
computadora1 = Computadora("Dell", "Intel Core i3", 4, 3500.00)
computadora1.mostrar_informacion()
computadora1.evaluar_rendimiento()
computadora1.calcular_costo_total(3)
  
print("---------------------------------------")
computadora2 = Computadora("HP", "Intel Core i7", 16, 6500.00)  
computadora2.mostrar_informacion()
computadora2.evaluar_rendimiento()
computadora2.calcular_costo_total(2)