import time

class Cronometro:
    def __init__(self):
        self.Johan = 0
        self.Sebastian = False
    
    def iniciar(self):
        if not self.Sebastian:
            self.Sebastian = True
            self.Johan = time.time()
            return "Cronómetro iniciado"
        return "Ya está corriendo"
    
    def detener(self):
        if self.Sebastian:
            self.Sebastian = False
            return f"Tiempo: {time.time() - self.Johan:.2f} segundos"
        return "El cronómetro no está corriendo"
    
    def reiniciar(self):
        self.Johan = 0
        self.Sebastian = False
        return "Cronómetro reiniciado"

crono = Cronometro()
print(crono.iniciar())
time.sleep(2)
print(crono.detener())
print(crono.reiniciar())