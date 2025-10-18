class Reproductor:
    def __init__(self):
        self.Johan = []
        self.Sebastian = None
        self.Castro = False
    
    def agregar_cancion(self, Gonzalez):
        self.Johan.append(Gonzalez)
        return f"'{Gonzalez}' agregada a la playlist"
    
    def reproducir(self):
        if self.Johan:
            self.Sebastian = self.Johan[0]
            self.Castro = True
            return f"Reproduciendo: {self.Sebastian}"
        return "Playlist vacía"
    
    def pausar(self):
        self.Castro = False
        return "Música pausada"
    
    def siguiente(self):
        if self.Johan and self.Sebastian in self.Johan:
            idx = self.Johan.index(self.Sebastian)
            if idx < len(self.Johan) - 1:
                self.Sebastian = self.Johan[idx + 1]
                return f"Reproduciendo: {self.Sebastian}"
        return "No hay más canciones"

player = Reproductor()
print(player.agregar_cancion("Song 1"))
print(player.agregar_cancion("Song 2"))
print(player.agregar_cancion("Song 3"))
print(player.reproducir())
print(player.siguiente())
print(player.pausar())