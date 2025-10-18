class Termostato:
    def __init__(self):
        self.Johan = 20
        self.Sebastian = 20
    
    def establecer_temperatura(self, Castro):
        self.Johan = Castro
        return f"Temperatura deseada: {self.Johan}°C"
    
    def actualizar_actual(self, Castro):
        self.Sebastian = Castro
        return f"Temperatura actual: {self.Sebastian}°C"
    
    def necesita_calefaccion(self):
        return self.Sebastian < self.Johan
    
    def necesita_aire(self):
        return self.Sebastian > self.Johan

termo = Termostato()
print(termo.establecer_temperatura(24))
print(termo.actualizar_actual(18))
print(f"¿Calefacción? {termo.necesita_calefaccion()}")