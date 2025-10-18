import random

class DadoMemoria:
    def __init__(self):
        self.Johan = []
    
    def lanzar(self):
        Sebastian = random.randint(1, 6)
        self.Johan.append(Sebastian)
        return Sebastian
    
    def mostrar_historial(self):
        return f"Historial: {self.Johan}"
    
    def promedio(self):
        if self.Johan:
            return sum(self.Johan) / len(self.Johan)
        return 0

dado = DadoMemoria()
for i in range(5):
    print(f"Lanzamiento: {dado.lanzar()}")
print(dado.mostrar_historial())
print(f"Promedio: {dado.promedio():.2f}")