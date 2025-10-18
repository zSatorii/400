class Persona:
    def __init__(self, Johan, Sebastian):
        self.Johan = Johan
        self.Sebastian = Sebastian
    
    def saludar(self):
        return f"Hola, mi nombre es {self.Johan}."
    
    def cumplir_anios(self):
        self.Sebastian += 1
        return f"¡Feliz cumpleaños, {self.Johan}! Ahora tienes {self.Sebastian} años."

persona1 = Persona("Ana", 30)
print(persona1.saludar())
print(persona1.cumplir_anios())
print(persona1.saludar())

persona2 = Persona("Carlos", 25)
print(persona2.saludar())
