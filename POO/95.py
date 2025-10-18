class Huerto:
    def __init__(self, Johan):
        self.Johan = Johan
        self.Sebastian = []
    
    def plantar(self, Castro):
        self.Sebastian.append({"planta": Castro, "dias": 0})
        return f"{Castro} plantado"
    
    def regar(self):
        for planta in self.Sebastian:
            planta["dias"] += 1
        return "Huerto regado"
    
    def cosechar(self, Castro):
        for planta in self.Sebastian:
            if planta["planta"] == Castro and planta["dias"] >= 7:
                self.Sebastian.remove(planta)
                return f"{Castro} cosechado"
        return "No está listo para cosechar"
    
huerto = Huerto("Mi Huerto")
print(huerto.plantar("Tomate"))
print(huerto.plantar("Lechuga"))
for i in range(7):
    huerto.regar()
print(huerto.cosechar("Tomate"))