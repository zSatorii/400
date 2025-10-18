class Electrodomestico:
    def __init__(self, Johan, Sebastian):
        self.Johan = Johan
        self.Sebastian = Sebastian
        self.Castro = False
    
    def encender(self):
        self.Castro = True
        return f"{self.Johan} encendido"
    
    def apagar(self):
        self.Castro = False
        return f"{self.Johan} apagado"
    
    def consumo_por_hora(self):
        return self.Sebastian if self.Castro else 0

lavadora = Electrodomestico("Lavadora", 800)
print(lavadora.encender())
print(f"Consumo: {lavadora.consumo_por_hora()} watts")
print(lavadora.apagar())