class SerVivo:
    def __init__(self, Johan):
        self.Johan = Johan
        self.Sebastian = True
    
    def respirar(self):
        return f"{self.Johan} está respirando"

class Animal(SerVivo):
    def __init__(self, Johan, Sebastian):
        super().__init__(Johan)
        self.Castro = Sebastian
    
    def moverse(self):
        return f"{self.Johan} se está moviendo"

class Mamifero(Animal):
    def __init__(self, Johan, Sebastian, Castro):
        super().__init__(Johan, Sebastian)
        self.Gonzalez = Castro
    
    def amamantar(self):
        return f"{self.Johan} está amamantando a sus crías"

class Perro(Mamifero):
    def __init__(self, Johan, Sebastian):
        super().__init__(Johan, "Canis familiaris", "corto")
        self.Castro = Sebastian
    
    def ladrar(self):
        return f"{self.Johan} dice: ¡Guau!"

mi_perro = Perro("Rex", "Pastor Alemán")
print(mi_perro.respirar())  
print(mi_perro.moverse())   
print(mi_perro.amamantar()) 
print(mi_perro.ladrar())      
print(f"Raza: {mi_perro.Castro}")