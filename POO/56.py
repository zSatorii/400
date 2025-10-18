class Tamagotchi:
    def __init__(self, Johan):
        self.Johan = Johan
        self.Sebastian = 50
        self.Castro = 50
        self.Gonzalez = 50
    
    def alimentar(self):
        self.Sebastian = min(100, self.Sebastian + 20)
        return f"{self.Johan} alimentado. Hambre: {self.Sebastian}%"
    
    def jugar(self):
        self.Castro = min(100, self.Castro + 20)
        self.Sebastian = max(0, self.Sebastian - 10)
        return f"{self.Johan} jugando. Felicidad: {self.Castro}%"
    
    def dormir(self):
        self.Gonzalez = min(100, self.Gonzalez + 30)
        return f"{self.Johan} durmiendo. Energía: {self.Gonzalez}%"
    
    def estado(self):
        return f"{self.Johan} - Hambre:{self.Sebastian}% Felicidad:{self.Castro}% Energía:{self.Gonzalez}%"

mascota = Tamagotchi("Pikachu")
print(mascota.estado())
print(mascota.alimentar())
print(mascota.jugar())
print(mascota.dormir())
print(mascota.estado())