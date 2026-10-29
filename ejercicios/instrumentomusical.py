from abc import ABC, abstractmethod

class InstrumentoMusical(ABC):
    
    @abstractmethod
    def producir_sonido(self):
        pass
    
class Guitarra(InstrumentoMusical):
    
    def producir_sonido(self):
        print("La guitarra produce un sonido mediante sus cuerdas.")
        
class Flauta(InstrumentoMusical):
    
    def producir_sonido(self):
        print("La flauta produce un sonido mediante el soplo de aire.")
        
class Tambor(InstrumentoMusical):
    
    def producir_sonido(self):
        print("El tambor produce un sonido mediante vibraciones de la membrana.")      
          
# Crear una instancia de Guitarra y llamar al método producir_sonido
guitarra=Guitarra()
guitarra.producir_sonido()

flauta=Flauta()
flauta.producir_sonido()

tambor=Tambor()
tambor.producir_sonido()