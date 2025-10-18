class Coche:
    def __init__(self, Johan, Sebastian, Castro=0):
        self.Johan = Johan
        self.Sebastian = Sebastian
        self.Castro = Castro
        self.Gonzalez = False

coche1 = Coche("Toyota", "rojo")
coche2 = Coche("Ford", "azul", 50)
print(coche1.Johan)
print(coche2.Castro)