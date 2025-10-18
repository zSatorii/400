class Lampara:
    def __init__(self):
        self.Johan = False
        self.Sebastian = 0
    
    def encender(self):
        self.Johan = True
        return "Lámpara encendida"
    
    def apagar(self):
        self.Johan = False
        return "Lámpara apagada"
    
    def ajustar_intensidad(self, Johan):
        if self.Johan:
            self.Sebastian = max(0, min(100, Johan))
            return f"Intensidad: {self.Sebastian}%"
        return "Enciende la lámpara primero"

lampara = Lampara()
print(lampara.encender())
print(lampara.ajustar_intensidad(75))
print(lampara.ajustar_intensidad(120))
print(lampara.apagar())
print(lampara.ajustar_intensidad(50))