import random

class Moneda:
    def __init__(self):
        self.Johan = "cara"
    
    def lanzar(self):
        self.Johan = random.choice(["cara", "cruz"])
        return self.Johan
    
    def obtener_resultado(self):
        return self.Johan

# Uso
moneda = Moneda()
print("Lanzando moneda 10 veces:")
caras = 0
cruces = 0
for i in range(10):
    resultado = moneda.lanzar()
    print(f"Lanzamiento {i+1}: {resultado}")
    if resultado == "cara":
        caras += 1
    else:
        cruces += 1
print(f"\\nCaras: {caras}, Cruces: {cruces}")