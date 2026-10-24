class EquipoInformatico:
    def __init__(self, codigo, nombre, estado):
        self.codigo = codigo
        self.nombre = nombre
        self.estado = estado

    def mostrar_equipo(self):
        print(f"Código: {self.codigo}")
        print(f"Nombre: {self.nombre}")
        print(f"Estado: {self.estado}")
        
    def verificar_estado(self ):
        print(f"El estado del equipo {self.nombre} es desconocido.")
        