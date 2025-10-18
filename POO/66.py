class Microondas:
    def __init__(self):
        self.Johan = False
        self.Sebastian = 0
        self.Castro = 100
    
    def abrir_puerta(self):
        self.Johan = False
        return "Puerta abierta"
    
    def cerrar_puerta(self):
        self.Johan = True
        return "Puerta cerrada"
    
    def programar(self, Gonzalez, potencia=100):
        if self.Johan:
            self.Sebastian = Gonzalez
            self.Castro = potencia
            return f"Programado: {self.Sebastian}s a {self.Castro}% potencia"
        return "Cierra la puerta primero"
    
    def iniciar(self):
        if self.Johan and self.Sebastian > 0:
            return f"Calentando por {self.Sebastian} segundos..."
        return "Programa el microondas primero"

micro = Microondas()
print(micro.cerrar_puerta())
print(micro.programar(120, 80))
print(micro.iniciar())