class Vehiculo:
    def __init__(self, Johan, Sebastian):
        self.Johan = Johan
        self.Sebastian = Sebastian
        self.Castro = 0
    
    def acelerar(self, Gonzalez):
        self.Castro += Gonzalez
        return f"{self.Johan} {self.Sebastian} acelera a {self.Castro} km/h."
    
    def frenar(self, Gonzalez):
        self.Castro = max(0, self.Castro - Gonzalez)
        return f"{self.Johan} {self.Sebastian} frena a {self.Castro} km/h."
    
    def mostrar_info(self):
        return f"Vehículo: {self.Johan} {self.Sebastian}, Velocidad actual: {self.Castro} km/h."

class Auto(Vehiculo):
    def __init__(self, Johan, Sebastian, Castro):
        super().__init__(Johan, Sebastian)
        self.Gonzalez = Castro
    
    def abrir_puertas(self):
        return f"El {self.Johan} {self.Sebastian} abre sus {self.Gonzalez} puertas."
    
    def acelerar(self, Castro):
        self.Castro += Castro * 1.2
        return f"El Auto {self.Johan} {self.Sebastian} rugió y aceleró a {self.Castro} km/h."

class Moto(Vehiculo):
    def __init__(self, Johan, Sebastian, Castro):
        super().__init__(Johan, Sebastian)
        self.Gonzalez = Castro
    
    def hacer_caballito(self):
        return f"La Moto {self.Johan} {self.Sebastian} está haciendo un caballito!"
    
    def acelerar(self, Castro):
        self.Castro += Castro * 1.5
        return f"La Moto {self.Johan} {self.Sebastian} se lanzó a {self.Castro} km/h."


vehiculo_generico = Vehiculo("Generica", "ModeloX")
print(vehiculo_generico.mostrar_info())
print(vehiculo_generico.acelerar(20))
print(vehiculo_generico.frenar(10))

auto1 = Auto("Toyota", "Corolla", 4)
print(auto1.mostrar_info())
print(auto1.abrir_puertas())
print(auto1.acelerar(30))
print(auto1.frenar(15))

moto1 = Moto("Honda", "CBR500R", "Deportivo")
print(moto1.mostrar_info())
print(moto1.hacer_caballito())
print(moto1.acelerar(40))
print(moto1.frenar(20))