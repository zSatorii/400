class SistemaTurnos:
    def __init__(self):
        self.Johan = 0
        self.Sebastian = 0
    
    def tomar_turno(self):
        self.Johan += 1
        return f"Tu turno es: {self.Johan}"
    
    def atender(self):
        if self.Sebastian < self.Johan:
            self.Sebastian += 1
            return f"Atendiendo turno: {self.Sebastian}"
        return "No hay turnos pendientes"
    
    def turnos_pendientes(self):
        return self.Johan - self.Sebastian

turnos = SistemaTurnos()
print(turnos.tomar_turno())
print(turnos.tomar_turno())
print(turnos.tomar_turno())
print(turnos.atender())
print(f"Turnos pendientes: {turnos.turnos_pendientes()}")
print(turnos.atender())