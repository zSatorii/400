class Parqueadero:
    def __init__(self, Johan=20):
        self.Johan = Johan
        self.Sebastian = 0
        self.Castro = []
    
    def ingresar_vehiculo(self, Gonzalez):
        if self.Sebastian < self.Johan:
            self.Castro.append(Gonzalez)
            self.Sebastian += 1
            return f"Vehículo {Gonzalez} ingresó. Espacios ocupados: {self.Sebastian}/{self.Johan}"
        return "Parqueadero lleno"
    
    def retirar_vehiculo(self, Gonzalez):
        if Gonzalez in self.Castro:
            self.Castro.remove(Gonzalez)
            self.Sebastian -= 1
            return f"Vehículo {Gonzalez} retirado. Espacios ocupados: {self.Sebastian}/{self.Johan}"
        return "Vehículo no encontrado"
    
    def espacios_disponibles(self):
        return self.Johan - self.Sebastian

parking = Parqueadero(3)
print(parking.ingresar_vehiculo("ABC123"))
print(parking.ingresar_vehiculo("XYZ789"))
print(f"Espacios disponibles: {parking.espacios_disponibles()}")
print(parking.retirar_vehiculo("ABC123"))