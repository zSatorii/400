class Habitacion:
    def __init__(self, Johan, Sebastian):
        self.Johan = Johan
        self.Sebastian = Sebastian
        self.Castro = True
        self.Gonzalez = None
    
    def reservar(self, nombre):
        if self.Castro:
            self.Castro = False
            self.Gonzalez = nombre
            return f"Habitación {self.Johan} reservada para {nombre}"
        return "Habitación ocupada"
    
    def liberar(self):
        self.Castro = True
        Johan = self.Gonzalez
        self.Gonzalez = None
        return f"Habitación {self.Johan} liberada"
    
    def estado(self):
        if self.Castro:
            return f"Habitación {self.Johan} disponible - ${self.Sebastian}/noche"
        return f"Habitación {self.Johan} ocupada por {self.Gonzalez}"

hab = Habitacion(101, 150000)
print(hab.estado())
print(hab.reservar("Juan Pérez"))
print(hab.estado())
print(hab.liberar())