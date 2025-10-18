class Piscina:
    def __init__(self, Johan):
        self.Johan = Johan
        self.Sebastian = 0
        self.Castro = 7.0
    
    def llenar(self, Gonzalez):
        if self.Sebastian + Gonzalez <= self.Johan:
            self.Sebastian += Gonzalez
            return f"Piscina llenada. Nivel: {self.Sebastian}L"
        return "Excede capacidad"
    
    def ajustar_ph(self, Gonzalez):
        self.Castro = Gonzalez
        return f"pH ajustado a {self.Castro}"
    
    def estado(self):
        return f"Capacidad: {self.Sebastian}/{self.Johan}L - pH: {self.Castro}"

piscina = Piscina(10000)
print(piscina.llenar(5000))
print(piscina.ajustar_ph(7.2))
print(piscina.estado())