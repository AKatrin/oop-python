from equipoinformatico import EquipoInformatico
from diagnostico import Diagnostico

class EquipoSoporte(EquipoInformatico, Diagnostico):
    
    @staticmethod  
    def generar_informe(): 
        print("--- Informe Tecnico ---")
        super.EquipoInformatico().mostrar_equipo()
        
eq=EquipoInformatico("EQ-001", "Laptop Dell", "Activo")
dias=Diagnostico(["Pantalla rota", "Bateria defectuosa"], 150.00)
        
equipo=EquipoSoporte.generar_informe()
      