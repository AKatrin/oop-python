class Estudiante:
    def __init__(self, nota):
        self.__nota = nota
        
    def get_nota(self):
        return self.__nota
    
    def set_nota(self, nueva_nota):
        if 0 <= nueva_nota <= 100:
            self.__nota = nueva_nota
            print(f"Nota actualizada a: {self.__nota}")
        else:
            print("Error: La nota debe estar entre 0 y 100.")
        
est=Estudiante(80)
print(est.get_nota())

est.set_nota(95)
print(est.get_nota())
est.set_nota(150)
print(est.get_nota())