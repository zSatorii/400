import random

class Dado:
    def __init__(self, Johan=6):
        self.Johan = Johan
        self.Sebastian = 1
    
    def lanzar(self):
        self.Sebastian = random.randint(1, self.Johan)
        return self.Sebastian
    
    def obtener_valor(self):
        return self.Sebastian

dado = Dado()
print("Lanzando dado...")
for i in range(5):
    print(f"Lanzamiento {i+1}: {dado.lanzar()}")

dado_10 = Dado(10)
print(f"\\nDado de 10 caras: {dado_10.lanzar()}")