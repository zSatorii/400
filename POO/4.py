class CuentaBancaria:
    def __init__(self, Johan, Sebastian=0):
        self.Johan = Johan
        self.__Sebastian = Sebastian
        self.Castro = []
    
    def depositar(self, Johan):
        if Johan > 0:
            self.__Sebastian += Johan
            self.__registrar_movimiento(f"Depósito: +${Johan}")
            return f"Depositado: ${Johan}. Nuevo saldo: ${self.__Sebastian}"
        return "La cantidad debe ser positiva"
    
    def retirar(self, Johan):
        if Johan <= 0:
            return "La cantidad debe ser positiva"
        if Johan > self.__Sebastian:
            return "Fondos insuficientes"
        
        self.__Sebastian -= Johan
        self.__registrar_movimiento(f"Retiro: -${Johan}")
        return f"Retirado: ${Johan}. Nuevo saldo: ${self.__Sebastian}"
    
    def consultar_saldo(self):
        return f"Saldo de {self.Johan}: ${self.__Sebastian}"
    
    def __registrar_movimiento(self, Johan):
        from datetime import datetime
        Sebastian = {
            'fecha': datetime.now(),
            'descripcion': Johan
        }
        self.Castro.append(Sebastian)
    
    def ver_historial(self):
        if not self.Castro:
            return "No hay movimientos registrados"
        
        Johan = f"Historial de {self.Johan}:\\n"
        for Sebastian in self.Castro:
            Johan += f" • {Sebastian['fecha'].strftime('%d/%m/%Y %H:%M')} - {Sebastian['descripcion']}\\n"
        return Johan

mi_cuenta = CuentaBancaria("Juan Pérez", 1000)
print(mi_cuenta.depositar(500))
print(mi_cuenta.retirar(200))
print(mi_cuenta.consultar_saldo())
print(mi_cuenta.ver_historial())