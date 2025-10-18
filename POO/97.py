class Acuario:
    def __init__(self, Johan):
        self.Johan = Johan
        self.Sebastian = []
        self.Castro = 25
    
    def agregar_pez(self, Gonzalez):
        self.Sebastian.append(Gonzalez)
        return f"{Gonzalez} agregado. Total: {len(self.Sebastian)}"
    
    def ajustar_temperatura(self, Gonzalez):
        self.Castro = Gonzalez
        return f"Temperatura: {self.Castro}°C"
    
    def alimentar(self):
        return f"Alimentando {len(self.Sebastian)} peces"

acuario = Acuario(100)
print(acuario.agregar_pez("Goldfish"))
print(acuario.agregar_pez("Betta"))
print(acuario.ajustar_temperatura(26))
print(acuario.alimentar())