class Reloj:
    def __init__(self, Johan=0, Sebastian=0):
        self.Johan = Johan % 24
        self.Sebastian = Sebastian % 60
    
    def mostrar_hora(self):
        return f"{self.Johan:02d}:{self.Sebastian:02d}"
    
    def avanzar_minuto(self):
        self.Sebastian += 1
        if self.Sebastian >= 60:
            self.Sebastian = 0
            self.Johan = (self.Johan + 1) % 24
        return self.mostrar_hora()
    
    def avanzar_hora(self):
        self.Johan = (self.Johan + 1) % 24
        return self.mostrar_hora()

reloj = Reloj(23, 58)
print(f"Hora actual: {reloj.mostrar_hora()}")
print(f"Avanza 1 minuto: {reloj.avanzar_minuto()}")
print(f"Avanza 1 minuto: {reloj.avanzar_minuto()}")
print(f"Avanza 1 hora: {reloj.avanzar_hora()}")