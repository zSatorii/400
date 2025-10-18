class SensorMovimiento:
    def __init__(self, Johan):
        self.Johan = Johan
        self.Sebastian = False
        self.Castro = 0
    
    def detectar_movimiento(self):
        self.Sebastian = True
        self.Castro += 1
        return f"¡Movimiento detectado! Total: {self.Castro}"
    
    def resetear(self):
        self.Sebastian = False
        return "Sensor reseteado"
    
    def estado(self):
        return "Activo" if self.Sebastian else "Inactivo"

sensor = SensorMovimiento("Entrada Principal")
print(sensor.detectar_movimiento())
print(f"Estado: {sensor.estado()}")
print(sensor.resetear())