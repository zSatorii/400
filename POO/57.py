class Horno:
    def __init__(self):
        self.Johan = False
        self.Sebastian = 0
        self.Castro = 0
    
    def encender(self, Gonzalez):
        self.Johan = True
        self.Sebastian = Gonzalez
        return f"Horno encendido a {self.Sebastian}°C"
    
    def apagar(self):
        self.Johan = False
        self.Sebastian = 0
        return "Horno apagado"
    
    def cocinar(self, Johan):
        if self.Johan:
            self.Castro = Johan
            return f"Cocinando por {self.Castro} minutos"
        return "Enciende el horno primero"

horno = Horno()
print(horno.encender(180))
print(horno.cocinar(45))
print(horno.apagar())