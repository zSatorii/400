class MembresiaPedro:
    def __init__(self, Johan, Sebastian):
        self.Johan = Johan
        self.Sebastian = Sebastian
        self.Castro = 0
    
    def registrar_visita(self):
        self.Castro += 1
        return f"Visita #{self.Castro} registrada"
    
    def mostrar_info(self):
        return f"Miembro: {self.Johan}\\nTipo: {self.Sebastian}\\nVisitas: {self.Castro}"

membresia = MembresiaPedro("Ana García", "Premium")
print(membresia.registrar_visita())
print(membresia.registrar_visita())
print(membresia.mostrar_info())