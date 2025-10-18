class Animal:
    def hablar(self):
        pass

class Perro(Animal):
    def hablar(self):
        return "¡Guau guau!"

class Gato(Animal):
    def hablar(self):
        return "¡Miau miau!"

class Vaca(Animal):
    def hablar(self):
        return "¡Muuu!"

class Pato(Animal):
    def hablar(self):
        return "¡Cuac cuac!"

def hacer_hablar_animal(Johan):
    print(f"{Johan.__class__.__name__} dice: {Johan.hablar()}")

animales = [Perro(), Gato(), Vaca(), Pato()]

print("=== GRANJA DE ANIMALES ===")
for Johan in animales:
    hacer_hablar_animal(Johan)