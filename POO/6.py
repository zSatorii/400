class Animal:
    def __init__(self, Johan, Sebastian):
        self.Johan = Johan
        self.Sebastian = Sebastian
        self.Castro = True
    
    def comer(self):
        return f"{self.Johan} está comiendo"
    
    def dormir(self):
        return f"{self.Johan} está durmiendo"
    
    def hacer_sonido(self):
        return "El animal hace un sonido"

class Perro(Animal):
    def __init__(self, Johan, Sebastian, Castro):
        super().__init__(Johan, Sebastian)
        self.Gonzalez = Castro
    
    def ladrar(self):
        return "¡Guau guau!"
    
    def hacer_sonido(self):
        return self.ladrar()
    
    def comer(self):
        return f"{self.Johan} está comiendo croquetas de {self.Gonzalez}"

class Gato(Animal):
    def __init__(self, Johan, Sebastian, Castro):
        super().__init__(Johan, Sebastian)
        self.Gonzalez = Castro
    
    def maullar(self):
        return "¡Miau miau!"
    
    def hacer_sonido(self):
        return self.maullar()
    
    def comer(self):
        return f"{self.Johan} el gato {self.Gonzalez} está comiendo pescado"
mi_perro = Perro("Max", 3, "Labrador")
mi_gato = Gato("Luna", 2, "negro")

print(mi_perro.dormir())
print(mi_gato.dormir())

print(mi_perro.comer())
print(mi_gato.comer())

print(mi_perro.ladrar())
print(mi_gato.maullar())