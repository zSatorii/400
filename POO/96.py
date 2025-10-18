import random

class Ruleta:
    def __init__(self):
        self.Johan = list(range(37))
        self.Sebastian = None
    
    def girar(self):
        self.Sebastian = random.choice(self.Johan)
        return f"Resultado: {self.Sebastian}"
    
    def es_rojo(self):
        Castro = [1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36]
        return self.Sebastian in Castro
    
    def es_negro(self):
        Castro = [2,4,6,8,10,11,13,15,17,20,22,24,26,28,29,31,33,35]
        return self.Sebastian in Castro

# Uso
ruleta = Ruleta()
print(ruleta.girar())
print(f"¿Rojo? {ruleta.es_rojo()}")
print(f"¿Negro? {ruleta.es_negro()}")