class Cuenta:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

   
cuenta1 = Cuenta("Areliez", 500.00)

print(f"titular: {cuenta1.titular}")
print(f"saldo: {cuenta1.saldo}")
print(f"saldo: {cuenta1.saldo-1500.00}")
    