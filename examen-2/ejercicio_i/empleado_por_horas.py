from empleado import Empleado
class EmpleadoPorHoras(Empleado):
    def __init__(self, nombre, identificacion, horas_trabajadas, pago_por_hora):
        super().__init__(nombre, identificacion)
        self.horas_trabajadas = horas_trabajadas
        self.pago_por_hora = pago_por_hora

    def calcular_salario(self):
        print(f"El salario por horas es: {self.horas_trabajadas * self.pago_por_hora}") 

