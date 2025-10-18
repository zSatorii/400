class Termometro:
    def __init__(self, Johan=0):
        self.Johan = Johan
    
    def medir(self, Sebastian):
        self.Johan = Sebastian
        return f"Temperatura medida: {self.Johan}°C"
    
    def esta_fiebre(self):
        return self.Johan > 37.5

# Uso
termometro = Termometro()
print(termometro.medir(36.5))
print(f"¿Tiene fiebre? {termometro.esta_fiebre()}")
print(termometro.medir(38.5))
print(f"¿Tiene fiebre? {termometro.esta_fiebre()}")