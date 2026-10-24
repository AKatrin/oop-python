class Usuario:
    intentos_fallidos = 0
    def __init__(self, nombre, correo, contrasenia):
        self.nombre = nombre
        self.correo = correo
        self.contrasenia = contrasenia
        
    def mostrar_datos(self):
        print(f"Nombre: {self.nombre}")
        print(f"Correo: {self.correo}")
        
    def verificar_contrasenia(self, contrasenia):
            if self.contrasenia == contrasenia:
              print(f"Acceso permitido.\n Bienvenido {self.nombre}")
            else:
                
                print("Contrasenia incorrecta.")
                self.intentos_fallidos += 1
                print(f"Intentos restantes: {3 - self.intentos_fallidos}")
                if self.intentos_fallidos >= 3:
                    print("Usuario bloqueado.")
                        
    def iniciar_sesion(self):
        contrasenia = input("Ingrese su contrasenia: ")
        self.verificar_contrasenia(contrasenia)
        while self.intentos_fallidos < 3 and contrasenia != self.contrasenia:
            contrasenia = input("Ingrese su contrasenia: ")
            self.verificar_contrasenia(contrasenia)
            
            
usuario1=Usuario("Walter","carlos@empresa.com","Sistemas123")
usuario1.mostrar_datos()
usuario1.iniciar_sesion()