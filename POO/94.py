class Cupon:
    def __init__(self, Johan, Sebastian):
        self.Johan = Johan
        self.Sebastian = Sebastian
        self.Castro = False
    
    def usar(self):
        if not self.Castro:
            self.Castro = True
            return f"Cupón '{self.Johan}' usado. Descuento: {self.Sebastian}%"
        return "Cupón ya usado"
    
    def es_valido(self):
        return not self.Castro

cupon = Cupon("DESC10", 10)
print(f"¿Válido? {cupon.es_valido()}")
print(cupon.usar())
print(f"¿Válido? {cupon.es_valido()}")
print(cupon.usar())