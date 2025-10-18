class Bateria:
    def __init__(self):
        self.Johan = 100
    
    def usar(self, Sebastian):
        self.Johan = max(0, self.Johan - Sebastian)
        return f"Batería: {self.Johan}%"
    
    def cargar(self, Sebastian):
        self.Johan = min(100, self.Johan + Sebastian)
        return f"Batería: {self.Johan}%"
    
    def esta_baja(self):
        return self.Johan < 20

# Uso
bateria = Bateria()
print(bateria.usar(30))
print(bateria.usar(50))
print(f"¿Batería baja? {bateria.esta_baja()}")
print(bateria.cargar(40))