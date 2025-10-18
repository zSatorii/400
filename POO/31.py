class Calendario:
    def __init__(self, Johan, Sebastian, Castro):
        self.Johan = Johan
        self.Sebastian = Sebastian
        self.Castro = Castro
    
    def mostrar_fecha(self):
        return f"{self.Johan:02d}/{self.Sebastian:02d}/{self.Castro}"
    
    def es_bisiesto(self):
        if self.Castro % 4 == 0 and (self.Castro % 100 != 0 or self.Castro % 400 == 0):
            return True
        return False

fecha = Calendario(18, 10, 2025)
print(fecha.mostrar_fecha())
print(f"¿Es bisiesto? {fecha.es_bisiesto()}")
fecha2 = Calendario(29, 2, 2024)
print(fecha2.mostrar_fecha())
print(f"¿Es bisiesto? {fecha2.es_bisiesto()}")