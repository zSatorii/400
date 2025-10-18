class Bombilla:
    def __init__(self):
        self.Johan = False
        self.Sebastian = "blanco"
        self.Castro = 100
    
    def encender(self):
        self.Johan = True
        return "Bombilla encendida"
    
    def apagar(self):
        self.Johan = False
        return "Bombilla apagada"
    
    def cambiar_color(self, Gonzalez):
        if self.Johan:
            self.Sebastian = Gonzalez
            return f"Color cambiado a {self.Sebastian}"
        return "Enciende la bombilla primero"
    
    def ajustar_brillo(self, Gonzalez):
        if self.Johan:
            self.Castro = max(0, min(100, Gonzalez))
            return f"Brillo: {self.Castro}%"
        return "Enciende la bombilla primero"

bombilla = Bombilla()
print(bombilla.encender())
print(bombilla.cambiar_color("azul"))
print(bombilla.ajustar_brillo(50))
print(bombilla.apagar())