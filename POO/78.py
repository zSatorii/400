class TanqueCombustible:
    def __init__(self, Johan):
        self.Johan = Johan
        self.Sebastian = 0
    
    def llenar(self, Castro):
        if self.Sebastian + Castro <= self.Johan:
            self.Sebastian += Castro
            return f"Tanque llenado. Nivel: {self.Sebastian}L"
        return "Excede capacidad"
    
    def usar(self, Castro):
        if self.Sebastian >= Castro:
            self.Sebastian -= Castro
            return f"Combustible usado. Quedan: {self.Sebastian}L"
        return "Combustible insuficiente"
    
    def porcentaje(self):
        return (self.Sebastian / self.Johan) * 100

tanque = TanqueCombustible(50)
print(tanque.llenar(30))
print(f"Nivel: {tanque.porcentaje():.1f}%")
print(tanque.usar(10))