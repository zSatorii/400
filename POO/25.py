class Televisor:
    def __init__(self):
        self.Johan = False
        self.Sebastian = 1
        self.Castro = 50
    
    def encender(self):
        self.Johan = True
        return "Televisor encendido"
    
    def apagar(self):
        self.Johan = False
        return "Televisor apagado"
    
    def subir_canal(self):
        if self.Johan:
            self.Sebastian += 1
            return f"Canal: {self.Sebastian}"
        return "El televisor está apagado"
    
    def bajar_canal(self):
        if self.Johan:
            self.Sebastian = max(1, self.Sebastian - 1)
            return f"Canal: {self.Sebastian}"
        return "El televisor está apagado"
    
    def cambiar_volumen(self, Johan):
        if self.Johan:
            self.Castro = max(0, min(100, self.Castro + Johan))
            return f"Volumen: {self.Castro}"
        return "El televisor está apagado"

tv = Televisor()
print(tv.encender())
print(tv.subir_canal())
print(tv.subir_canal())
print(tv.cambiar_volumen(10))
print(tv.apagar())