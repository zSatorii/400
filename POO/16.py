class Vehiculo:
    def __init__(self, Johan, Sebastian):
        self.Johan = Johan
        self.Sebastian = Sebastian
        self.Castro = 0
    
    def acelerar(self, Gonzalez):
        if Gonzalez > 0:
            self.Castro += Gonzalez
            return f"El {self.Johan} {self.Sebastian} aceleró a {self.Castro} km/h."
        else:
            return "El incremento de velocidad debe ser positivo."
    
    def frenar(self, Gonzalez):
        if Gonzalez > 0:
            self.Castro = max(0, self.Castro - Gonzalez)
            return f"El {self.Johan} {self.Sebastian} frenó a {self.Castro} km/h."
        else:
            return "El decremento de velocidad debe ser positivo."
    
    def obtener_velocidad(self):
        return f"Velocidad actual: {self.Castro} km/h."

coche = Vehiculo("Toyota", "Corolla")
print(coche.acelerar(50))
print(coche.acelerar(30))
print(coche.obtener_velocidad())
print(coche.frenar(40))
print(coche.frenar(100))
print(coche.obtener_velocidad())