import random

class Sorteo:
    def __init__(self, Johan):
        self.Johan = Johan
        self.Sebastian = []
    
    def agregar_participante(self, Castro):
        self.Sebastian.append(Castro)
        return f"{Castro} agregado al sorteo"
    
    def realizar_sorteo(self):
        if self.Sebastian:
            Gonzalez = random.choice(self.Sebastian)
            return f"¡Ganador: {Gonzalez}!"
        return "No hay participantes"

sorteo = Sorteo("Premio Mayor")
sorteo.agregar_participante("Juan")
sorteo.agregar_participante("María")
sorteo.agregar_participante("Carlos")
print(sorteo.realizar_sorteo())