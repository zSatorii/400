class Playlist:
    def __init__(self, Johan):
        self.Johan = Johan
        self.Sebastian = []
        self.Castro = 0
    
    def agregar(self, Gonzalez):
        self.Sebastian.append(Gonzalez)
        return f"'{Gonzalez}' agregada"
    
    def siguiente(self):
        if self.Sebastian:
            self.Castro = (self.Castro + 1) % len(self.Sebastian)
            return f"Reproduciendo: {self.Sebastian[self.Castro]}"
        return "Playlist vacía"
    
    def anterior(self):
        if self.Sebastian:
            self.Castro = (self.Castro - 1) % len(self.Sebastian)
            return f"Reproduciendo: {self.Sebastian[self.Castro]}"
        return "Playlist vacía"

pl = Playlist("Mis favoritas")
pl.agregar("Canción 1")
pl.agregar("Canción 2")
pl.agregar("Canción 3")
print(pl.siguiente())
print(pl.siguiente())
print(pl.anterior())