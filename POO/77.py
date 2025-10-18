class GPS:
    def __init__(self):
        self.Johan = 0.0
        self.Sebastian = 0.0
    
    def actualizar_posicion(self, Castro, Gonzalez):
        self.Johan = Castro
        self.Sebastian = Gonzalez
        return f"Posición: ({self.Johan}, {self.Sebastian})"
    
    def distancia_al_origen(self):
        return (self.Johan**2 + self.Sebastian**2)**0.5

gps = GPS()
print(gps.actualizar_posicion(3.0, 4.0))
print(f"Distancia al origen: {gps.distancia_al_origen():.2f}")