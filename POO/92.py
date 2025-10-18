class Clima:
    def __init__(self, Johan):
        self.Johan = Johan
        self.Sebastian = 20
        self.Castro = 50
    
    def actualizar(self, Gonzalez, humedad):
        self.Sebastian = Gonzalez
        self.Castro = humedad
        return f"{self.Johan}: {self.Sebastian}°C, Humedad: {self.Castro}%"
    
    def esta_caluroso(self):
        return self.Sebastian > 30
    
    def esta_humedo(self):
        return self.Castro > 70

clima = Clima("Bogotá")
print(clima.actualizar(18, 65))
print(f"¿Caluroso? {clima.esta_caluroso()}")
print(f"¿Húmedo? {clima.esta_humedo()}")