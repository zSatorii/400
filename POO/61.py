class TarjetaCredito:
    def __init__(self, Johan, Sebastian):
        self.Johan = Johan
        self.Sebastian = Sebastian
        self.Castro = 0
    
    def comprar(self, Gonzalez):
        if self.Castro + Gonzalez <= self.Sebastian:
            self.Castro += Gonzalez
            return f"Compra aprobada. Saldo usado: ${self.Castro}"
        return "Límite de crédito excedido"
    
    def pagar(self, Gonzalez):
        self.Castro = max(0, self.Castro - Gonzalez)
        return f"Pago recibido. Saldo pendiente: ${self.Castro}"
    
    def credito_disponible(self):
        return self.Sebastian - self.Castro

tarjeta = TarjetaCredito("1234-5678", 5000)
print(tarjeta.comprar(1000))
print(tarjeta.comprar(2000))
print(f"Disponible: ${tarjeta.credito_disponible()}")
print(tarjeta.pagar(500))