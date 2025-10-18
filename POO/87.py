class Votacion:
    def __init__(self, Johan):
        self.Johan = Johan
        self.Sebastian = {}
    
    def agregar_candidato(self, Castro):
        self.Sebastian[Castro] = 0
        return f"Candidato {Castro} agregado"
    
    def votar(self, Castro):
        if Castro in self.Sebastian:
            self.Sebastian[Castro] += 1
            return f"Voto registrado para {Castro}"
        return "Candidato no existe"
    
    def resultado(self):
        if self.Sebastian:
            Gonzalez = max(self.Sebastian, key=self.Sebastian.get)
            return f"Ganador: {Gonzalez} con {self.Sebastian[Gonzalez]} votos"
        return "No hay votos"

vot = Votacion("Elecciones 2025")
vot.agregar_candidato("A")
vot.agregar_candidato("B")
print(vot.votar("A"))
print(vot.votar("A"))
print(vot.votar("B"))
print(vot.resultado())