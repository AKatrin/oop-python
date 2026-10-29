from abc import ABC, abstractmethod

class UsuarioDeSistema(ABC):
    
    @abstractmethod
    def mostrar_permisos(self):
        pass
    
class Administrador(UsuarioDeSistema):

    def mostrar_permisos(self):
        print("El administrador tiene permisos de edition, lectura, creacion, eliminar")
    
class UsuarioEstandar(UsuarioDeSistema):
    
    def mostrar_permisos(self):
        print("El usuario estandar  tiene permis de lectura y creacion")
    
class Invitado(UsuarioDeSistema):
    
    def mostrar_permisos(self):
        print("El invitado tiene solo permisos de lectura")
        
admin=Administrador()
estandar=UsuarioEstandar()
invitado=Invitado()

admin.mostrar_permisos()    
estandar.mostrar_permisos() 
invitado.mostrar_permisos()
        