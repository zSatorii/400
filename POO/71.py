class BancoSimple:
    def __init__(self, Johan):
        self.Johan = Johan
        self.Sebastian = {}
    
    def crear_cuenta(self, Castro, Gonzalez=0):
        self.Sebastian[Castro] = Gonzalez
        return f"Cuenta {Castro} creada con ${Gonzalez}"
    
    def deposito(self, Castro, Gonzalez):
        if Castro in self.Sebastian:
            self.Sebastian[Castro] += Gonzalez
            return f"Depósito exitoso. Saldo: ${self.Sebastian[Castro]}"
        return "Cuenta no existe"
    
    def consultar(self, Castro):
        if Castro in self.Sebastian:
            return f"Saldo de cuenta {Castro}: ${self.Sebastian[Castro]}"
        return "Cuenta no existe"

banco = BancoSimple("MiBanco")
print(banco.crear_cuenta("001", 1000))
print(banco.deposito("001", 500))
print(banco.consultar("001"))