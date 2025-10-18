class Mascota:
    def __init__(self, Johan, Sebastian):
        self.Johan = Johan
        self.Sebastian = Sebastian
        self.Castro = "Feliz"
    
    def alimentar(self):
        self.Castro = "Satisfecho"
        return f"{self.Johan} ha sido alimentado y ahora está {self.Castro}."
    
    def jugar(self):
        self.Castro = "Animado"
        return f"{self.Johan} ha jugado y ahora está {self.Castro}."
    
    def dormir(self):
        self.Castro = "Durmiendo"
        return f"{self.Johan} se ha dormido y ahora está {self.Castro}."
    
    def mostrar_estado(self):
        return f"{self.Johan}, tu {self.Sebastian}, está {self.Castro}."

mascota1 = Mascota("Max", "Perro")
print(mascota1.mostrar_estado())
print(mascota1.alimentar())
print(mascota1.mostrar_estado())
print(mascota1.jugar())
print(mascota1.mostrar_estado())
print(mascota1.dormir())
print(mascota1.mostrar_estado())
print(mascota1.alimentar())

mascota2 = Mascota("Luna", "Gato")
print(mascota2.mostrar_estado())
print(mascota2.jugar())
print(mascota2.dormir())
print(mascota2.mostrar_estado())