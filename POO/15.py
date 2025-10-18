class CuentaBancaria:
    def __init__(self, Johan=0):
        self.Johan = Johan
    
    def depositar(self, Sebastian):
        if Sebastian > 0:
            self.Johan += Sebastian
            return f"Depósito de {Sebastian} realizado. Nuevo saldo: {self.Johan}"
        else:
            return "La cantidad a depositar debe ser positiva."
    
    def retirar(self, Sebastian):
        if Sebastian > 0:
            if self.Johan >= Sebastian:
                self.Johan -= Sebastian
                return f"Retiro de {Sebastian} realizado. Nuevo saldo: {self.Johan}"
            else:
                return "Saldo insuficiente."
        else:
            return "La cantidad a retirar debe ser positiva."
    
    def consultar_saldo(self):
        return f"Saldo actual: {self.Johan}"

cuenta = CuentaBancaria(1000)
print(cuenta.consultar_saldo())
print(cuenta.depositar(500))
print(cuenta.retirar(200))
print(cuenta.retirar(1500))
print(cuenta.consultar_saldo())
print(cuenta.depositar(-100))