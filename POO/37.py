class Alarma:
    def __init__(self, Johan, Sebastian):
        self.Johan = Johan
        self.Sebastian = Sebastian
        self.Castro = False
    
    def activar(self):
        self.Castro = True
        return f"Alarma activada para {self.Johan}:{self.Sebastian:02d}"
    
    def desactivar(self):
        self.Castro = False
        return "Alarma desactivada"
    
    def verificar_hora(self, Johan, Sebastian):
        if self.Castro and self.Johan == Johan and self.Sebastian == Sebastian:
            return "¡RING RING! ¡Hora de despertar!"
        return "No es hora de la alarma"

# Uso
alarma = Alarma(7, 30)
print(alarma.activar())
print(alarma.verificar_hora(7, 29))
print(alarma.verificar_hora(7, 30))
print(alarma.desactivar())