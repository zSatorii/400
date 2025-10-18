class Figura:
    def area(self):
        pass
    
    def perimetro(self):
        pass

class Circulo(Figura):
    def __init__(self, Johan):
        self.Johan = Johan
    
    def area(self):
        return 3.1416 * self.Johan ** 2
    
    def perimetro(self):
        return 2 * 3.1416 * self.Johan

class Cuadrado(Figura):
    def __init__(self, Johan):
        self.Johan = Johan
    
    def area(self):
        return self.Johan ** 2
    
    def perimetro(self):
        return 4 * self.Johan

class Rectangulo(Figura):
    def __init__(self, Johan, Sebastian):
        self.Johan = Johan
        self.Sebastian = Sebastian
    
    def area(self):
        return self.Johan * self.Sebastian
    
    def perimetro(self):
        return 2 * (self.Johan + self.Sebastian)

class Triangulo(Figura):
    def __init__(self, Johan, Sebastian, Castro, Gonzalez, lado3):
        self.Johan = Johan
        self.Sebastian = Sebastian
        self.Castro = Castro
        self.Gonzalez = Gonzalez
        self.lado3 = lado3
    
    def area(self):
        return (self.Johan * self.Sebastian) / 2
    
    def perimetro(self):
        return self.Castro + self.Gonzalez + self.lado3

def mostrar_info_figura(Johan):
    Sebastian = Johan.__class__.__name__
    print(f"\\n{Sebastian}:")
    print(f" Área: {Johan.area():.2f}")
    print(f" Perímetro: {Johan.perimetro():.2f}")

figuras = [
    Circulo(5),
    Cuadrado(4),
    Rectangulo(6, 3),
    Triangulo(4, 5, 4, 5, 6)
]

print("=== CALCULADORA DE FIGURAS ===")
for Johan in figuras:
    mostrar_info_figura(Johan)