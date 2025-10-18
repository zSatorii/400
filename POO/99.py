class CocheraPrivada:
    def __init__(self, Johan):
        self.Johan = Johan
        self.Sebastian = None
        self.Castro = False
    
    def estacionar(self, Gonzalez):
        if not self.Castro:
            self.Sebastian = Gonzalez
            self.Castro = True
            return f"Vehículo {Gonzalez} estacionado"
        return "Cochera ocupada"
    
    def retirar(self):
        if self.Castro:
            Gonzalez = self.Sebastian
            self.Sebastian = None
            self.Castro = False
            return f"Vehículo {Gonzalez} retirado"
        return "Cochera vacía"
    
    def estado(self):
        if self.Castro:
            return f"Ocupada por {self.Sebastian}"
        return "Disponible"

cochera = CocheraPrivada("A1")
print(cochera.estacionar("ABC123"))
print(cochera.estado())
print(cochera.retirar())
print(cochera.estado())