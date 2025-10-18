class SalaCine:
    def __init__(self, Johan, Sebastian):
        self.Johan = Johan
        self.Sebastian = Sebastian
        self.Castro = Sebastian
    
    def vender_boleto(self):
        if self.Castro > 0:
            self.Castro -= 1
            return f"Boleto vendido. Disponibles: {self.Castro}"
        return "Sala llena"
    
    def asientos_disponibles(self):
        return self.Castro

sala = SalaCine(1, 100)
print(sala.vender_boleto())
print(sala.vender_boleto())
print(f"Asientos disponibles: {sala.asientos_disponibles()}")