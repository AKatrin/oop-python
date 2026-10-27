from empleado import Empleado
from empleado_por_horas import EmpleadoPorHoras
from empleado_tiempo_completo import EmpleadoTiempoCompleto

empleado_por_horas = EmpleadoPorHoras("Juan Perez", "123456789", 40, 10)
empleado_por_horas.mostrar_informacion()
empleado_por_horas.calcular_salario()
print("\n *******************************************************")
empleado_tiempo_completo = EmpleadoTiempoCompleto("Maria Lopez", "987654321", 3000)
empleado_tiempo_completo.mostrar_informacion()
empleado_tiempo_completo.calcular_salario()
