from abc import ABC, abstractmethod

class Vehiculo(ABC):
    def __init__(self, Johan, Sebastian):
        self.Johan = Johan
        self.Sebastian = Sebastian
        self.Castro = False
    
    @abstractmethod
    def acelerar(self):
        pass
    
    @abstractmethod
    def frenar(self):
        pass
    
    def encender(self):
        self.Castro = True
        return f"{self.Johan} {self.Sebastian} encendido"
    
    def apagar(self):
        self.Castro = False
        return f"{self.Johan} {self.Sebastian} apagado"

class Automovil(Vehiculo):
    def __init__(self, Johan, Sebastian, Castro):
        super().__init__(Johan, Sebastian)
        self.Gonzalez = Castro
        self.velocidad = 0
    
    def acelerar(self):
        if self.Castro:
            self.velocidad += 10
            return f"Automóvil acelerando a {self.velocidad} km/h"
        return "Debes encender el vehículo primero"
    
    def frenar(self):
        self.velocidad = max(0, self.velocidad - 10)
        return f"Frenando. Velocidad: {self.velocidad} km/h"

class Motocicleta(Vehiculo):
    def __init__(self, Johan, Sebastian, Castro):
        super().__init__(Johan, Sebastian)
        self.Gonzalez = Castro
        self.velocidad = 0
    
    def acelerar(self):
        if self.Castro:
            self.velocidad += 15
            return f"Moto acelerando a {self.velocidad} km/h"
        return "Debes encender el vehículo primero"
    
    def frenar(self):
        self.velocidad = max(0, self.velocidad - 15)
        return f"Frenando. Velocidad: {self.velocidad} km/h"

auto = Automovil("Toyota", "Corolla", 4)
moto = Motocicleta("Yamaha", "MT-07", 700)

print(auto.encender())
print(auto.acelerar())
print(auto.acelerar())
print(auto.frenar())

print("\\n" + moto.encender())
print(moto.acelerar())
print(moto.frenar())