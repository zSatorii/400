import random

class JuegoAdivinanza:
    def __init__(self):
        self.Johan = random.randint(1, 100)
        self.Sebastian = 0
    
    def adivinar(self, Castro):
        self.Sebastian += 1
        if Castro < self.Johan:
            return "Muy bajo"
        elif Castro > self.Johan:
            return "Muy alto"
        else:
            return f"¡Correcto! Lo adivinaste en {self.Sebastian} intentos"
    
    def reiniciar(self):
        self.Johan = random.randint(1, 100)
        self.Sebastian = 0
        return "Juego reiniciado"

juego = JuegoAdivinanza()
print(juego.adivinar(50))
print(juego.adivinar(75))
print(juego.adivinar(60))