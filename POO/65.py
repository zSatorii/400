class Carta:
    def __init__(self, Johan, Sebastian):
        self.Johan = Johan  # número
        self.Sebastian = Sebastian  # palo
    
    def mostrar(self):
        return f"{self.Johan} de {self.Sebastian}"
    
    def valor(self):
        if self.Johan in ['J', 'Q', 'K']:
            return 10
        elif self.Johan == 'A':
            return 11
        return int(self.Johan)

carta1 = Carta('A', 'Corazones')
carta2 = Carta('K', 'Diamantes')
carta3 = Carta('7', 'Tréboles')
print(carta1.mostrar())
print(f"Valor: {carta1.valor()}")
print(carta2.mostrar())
print(f"Valor: {carta2.valor()}")