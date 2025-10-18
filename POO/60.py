class MaquinaCafe:
    def __init__(self):
        self.Johan = 100
        self.Sebastian = 100
        self.Castro = 100
    
    def hacer_cafe(self):
        if self.Johan >= 10 and self.Sebastian >= 30:
            self.Johan -= 10
            self.Sebastian -= 30
            return f"Café listo. Café:{self.Johan}g Agua:{self.Sebastian}ml"
        return "Ingredientes insuficientes"
    
    def hacer_capuchino(self):
        if self.Johan >= 10 and self.Sebastian >= 30 and self.Castro >= 20:
            self.Johan -= 10
            self.Sebastian -= 30
            self.Castro -= 20
            return f"Capuchino listo. Café:{self.Johan}g Agua:{self.Sebastian}ml Leche:{self.Castro}ml"
        return "Ingredientes insuficientes"
    
    def rellenar(self):
        self.Johan = 100
        self.Sebastian = 100
        self.Castro = 100
        return "Máquina rellenada"

maquina = MaquinaCafe()
print(maquina.hacer_cafe())
print(maquina.hacer_capuchino())
print(maquina.rellenar())