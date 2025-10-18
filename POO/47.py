class Ascensor:
    def __init__(self, Johan=10):
        self.Johan = Johan
        self.Sebastian = 0
    
    def subir(self):
        if self.Sebastian < self.Johan:
            self.Sebastian += 1
            return f"Piso actual: {self.Sebastian}"
        return "Ya estás en el último piso"
    
    def bajar(self):
        if self.Sebastian > 0:
            self.Sebastian -= 1
            return f"Piso actual: {self.Sebastian}"
        return "Ya estás en la planta baja"
    
    def ir_a_piso(self, Castro):
        if 0 <= Castro <= self.Johan:
            self.Sebastian = Castro
            return f"Has llegado al piso {self.Sebastian}"
        return "Piso inválido"

ascensor = Ascensor(5)
print(ascensor.subir())
print(ascensor.subir())
print(ascensor.ir_a_piso(5))
print(ascensor.bajar())