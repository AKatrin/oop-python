from abc import ABC, abstractmethod

class Vehiculo(ABC):
    
    @abstractmethod
    def moverse(self):
        pass
    
class Automovil(Vehiculo):
    
    def moverse(self):
        print("El automóvil se mueve acelerando sobre 4 ruedas.")
        
class Bicicleta(Vehiculo):
    
    def moverse(self):
        print("La bicicleta se mueve pedaleando.")
        
class Motocicleta(Vehiculo):
    
    def moverse(self):
        print("La motocicleta se mueve acelerando sobre dos ruedas.")        
        
class Avion(Vehiculo):
    
    def moverse(self):
        print("El avión se mueve volando por el aire.")
        
        
auto=Automovil()
bici=Bicicleta()
moto=Motocicleta()
avion=Avion()

auto.moverse()
bici.moverse()
moto.moverse() 
avion.moverse()