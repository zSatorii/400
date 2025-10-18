class Cancion:
    def __init__(self, Johan, Sebastian, Castro):
        self.Johan = Johan
        self.Sebastian = Sebastian
        self.Castro = Castro
        self.Gonzalez = False
    
    def reproducir(self):
        self.Gonzalez = True
        return f"Reproduciendo: {self.Johan} - {self.Sebastian}"
    
    def pausar(self):
        self.Gonzalez = False
        return "Canción pausada"
    
    def mostrar_info(self):
        return f"{self.Johan} - {self.Sebastian} ({self.Castro} segundos)"
    
cancion = Cancion("Bohemian Rhapsody", "Queen", 354)
print(cancion.mostrar_info())
print(cancion.reproducir())
print(cancion.pausar())