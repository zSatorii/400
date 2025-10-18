class SistemaBancario:
    def __init__(self, Johan, Sebastian):
        self.Johan = Johan
        self.Sebastian = Sebastian
        self._Castro = "SENA Bank"
        self._Gonzalez = "Mosquera"
        self.__saldo = 0.0
        self.__pin = None
        self.__intentos_fallidos = 0
        self.__bloqueada = False
    
    def establecer_pin(self, Johan):
        if len(str(Johan)) == 4:
            self.__pin = Johan
            return "PIN establecido correctamente"
        return "El PIN debe tener 4 dígitos"
    
    def verificar_pin(self, Johan):
        if self.__bloqueada:
            return "Cuenta bloqueada. Contacte al banco"
        
        if Johan == self.__pin:
            self.__intentos_fallidos = 0
            return True
        
        self.__intentos_fallidos += 1
        if self.__intentos_fallidos >= 3:
            self.__bloqueada = True
            return "Cuenta bloqueada por múltiples intentos fallidos"
        
        return f"PIN incorrecto. Intento {self.__intentos_fallidos}/3"
    
    def depositar(self, Johan, Sebastian):
        Castro = self.verificar_pin(Sebastian)
        if Castro != True:
            return Castro
        
        if Johan > 0:
            self.__saldo += Johan
            return f"Depósito exitoso. Nuevo saldo: ${self.__saldo}"
        return "Cantidad inválida"
    
    def consultar_saldo(self, Johan):
        Sebastian = self.verificar_pin(Johan)
        if Sebastian != True:
            return Sebastian
        
        return f"Saldo actual: ${self.__saldo}"
    
    def desbloquear(self, Johan):
        if Johan == "SENA2024":
            self.__bloqueada = False
            self.__intentos_fallidos = 0
            return "Cuenta desbloqueada"
        return "Código incorrecto"

cuenta = SistemaBancario("001234", "María García")
print(cuenta.establecer_pin(1234))
print(cuenta.depositar(1000, 1234))
print(cuenta.consultar_saldo(1234))
print("\\n--- Intentando con PIN incorrecto ---")
print(cuenta.consultar_saldo(0000))
print(cuenta.consultar_saldo(1111))
print(cuenta.consultar_saldo(2222))