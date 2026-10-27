class CuentaBancaria:
    
    def __init__(self, titular, numero_de_cuenta, saldo):
        self.titular = titular
        self.numero_de_cuenta = numero_de_cuenta
        self.set_saldo(saldo)

    def set_saldo(self, saldo):
        if saldo >= 0:
            self.__saldo = saldo
        else:
            print(f"Error en el saldo {saldo}. El saldo no puede ser negativo, vuelva a intentar")
        
    def depositar(self, cantidad):
        if cantidad > 0:
            self.__saldo += cantidad
            print(f"Se ha depositado {cantidad}. Nuevo saldo: {self.__saldo}")
        else:
            print(f"Error en la cantidad {cantidad}. La cantidad a depositar debe ser positiva.")

    def retirar(self, cantidad):
        if 0 < cantidad <= self.__saldo:
            self.__saldo -= cantidad
            print(f"Se ha retirado {cantidad}. Nuevo saldo: {self.__saldo}")
        else:
            print(f"La cantidad a retirar {cantidad} debe ser positiva y no puede exceder el saldo disponible.")

    def get_saldo(self):
        print(f"Saldo: { self.__saldo}")
        
    def mostrar_informacion(self):
        print(f"Titular: {self.titular}, \nNúmero de cuenta: {self.numero_de_cuenta}, \nSaldo: {self.__saldo}")
        

cuenta_one = CuentaBancaria("Juan Perez", "123456789", 10000.00)
cuenta_one.mostrar_informacion()
cuenta_one.depositar(5000)
cuenta_one.retirar(3000)
cuenta_one.retirar(20000)  # Intento de retirar más del saldo disponible
cuenta_one.depositar(-100)  # Intento de depositar una cantidad negativa           
cuenta_one.get_saldo() 


cuenta_two = CuentaBancaria("Maria Lopez", "987654321", -2000.00)