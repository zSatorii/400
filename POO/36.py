class Ventilador:
    def __init__(self):
        self.Johan = False
        self.Sebastian = 0
    
    def encender(self):
        self.Johan = True
        self.Sebastian = 1
        return "Ventilador encendido - Velocidad 1"
    
    def apagar(self):
        self.Johan = False
        self.Sebastian = 0
        return "Ventilador apagado"
    
    def cambiar_velocidad(self, Johan):
        if self.Johan and 1 <= Johan <= 3:
            self.Sebastian = Johan
            return f"Velocidad: {self.Sebastian}"
        return "Ventilador apagado o velocidad inválida"

# Uso
ventilador = Ventilador()
print(ventilador.encender())
print(ventilador.cambiar_velocidad(2))
print(ventilador.cambiar_velocidad(3))
print(ventilador.apagar())