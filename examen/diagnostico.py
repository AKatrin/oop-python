class Diagnostico:
    def __init__(self, problemas_detectados, costo_por_problema):
        self.problemas_detectados = problemas_detectados
        self.costo_por_problema = costo_por_problema

    def mostrar_problemas(self):
        print("Problemas detectados:")
        for problema in self.problemas_detectados:
            print(f"- {problema}")
            
    def calcular_costo_total(self):
        total = len(self.problemas_detectados) * self.costo_por_problema
        print(f"Costo total del diagnóstico: Bs. {total:.2f}")     