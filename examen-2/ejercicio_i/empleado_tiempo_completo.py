from empleado import Empleado
class EmpleadoTiempoCompleto(Empleado):
    def __init__(self, nombre, identificacion, salario_mensual):
        super().__init__(nombre, identificacion)
        self.salario_mensual = salario_mensual
        
    def calcular_salario(self):
        print(f"El salario por tiempo completo es:{self.salario_mensual}") 