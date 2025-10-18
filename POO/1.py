class Perro:
    def __init__(self, Johan, Sebastian, Castro):
        self.Johan = Johan  # Nombre del perro
        self.Sebastian = Sebastian  # Raza del perro
        self.Castro = Castro  # Edad del perro
    
    def ladrar(self):
        return f"{self.Johan} dice: ¡Guau guau!"
    
    def describir(self):
        return f"{self.Johan} es un {self.Sebastian} de {self.Castro} años"

# Creamos objetos (instancias)
perro1 = Perro("Max", "Labrador", 3)
perro2 = Perro("Luna", "Pastor Alemán", 5)

# Usamos los objetos
print(perro1.ladrar())
print(perro2.describir())