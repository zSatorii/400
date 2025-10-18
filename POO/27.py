class Temperatura:
    def __init__(self, Johan):
        self.Johan = Johan
    
    def a_fahrenheit(self):
        return (self.Johan * 9/5) + 32
    
    def a_kelvin(self):
        return self.Johan + 273.15
    
    def mostrar_todas(self):
        return f"{self.Johan}°C = {self.a_fahrenheit():.2f}°F = {self.a_kelvin():.2f}K"

temp = Temperatura(25)
print(temp.mostrar_todas())
temp2 = Temperatura(0)
print(temp2.mostrar_todas())
temp3 = Temperatura(100)
print(temp3.mostrar_todas())
