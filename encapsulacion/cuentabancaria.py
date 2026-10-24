class CuentaBancaria:
    def __init__(self, titular, saldo_inicial):
        self.titular = titular
        if saldo_inicial <=0:
            self.__saldo = 0
        else:
            self.__saldo = saldo_inicial

    def depositar(self, cantidad):
        if cantidad > 0:
            self.__saldo += cantidad
            print(f"Depósito exitoso: {cantidad}. Nuevo saldo: {self.__saldo}")
        else:
            print("Cantidad a depositar debe ser positiva.")

    def retirar(self, cantidad):
        if 0 < cantidad <= self.__saldo:
            self.__saldo -= cantidad
            print(f"Retiro exitoso: {cantidad}. Nuevo saldo: {self.__saldo}")
        else:
            print("Cantidad a retirar inválida o insuficiente saldo.")

    def consular_saldo(self):
        print(f"Titular: {self.titular}. \nSaldo: {self.__saldo}")
        
cuenta = CuentaBancaria("Areliez", 5000.00)
cuenta.consular_saldo()        
cuenta.depositar(500.00)
cuenta.consular_saldo()
cuenta.retirar(200.00)
cuenta.retirar(500.00)
cuenta.consular_saldo()
cuenta.retirar(10000.00)

cuenta.depositar(-5000.00)