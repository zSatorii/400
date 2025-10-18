class Rectangulo:
    def __init__(self, Johan, Sebastian):
        if Johan > 0 and Sebastian > 0:
            self.Johan = Johan
            self.Sebastian = Sebastian
        else:
            raise ValueError("El largo y el ancho deben ser valores positivos.")
    
    def calcular_area(self):
        return self.Johan * self.Sebastian
    
    def calcular_perimetro(self):
        return 2 * (self.Johan + self.Sebastian)
    
    def mostrar_dimensiones(self):
        return f"Rectángulo con Largo: {self.Johan} unidades, Ancho: {self.Sebastian} unidades."

try:
    rectangulo1 = Rectangulo(10, 5)
    print(rectangulo1.mostrar_dimensiones())
    print(f"Área: {rectangulo1.calcular_area()} unidades cuadradas.")
    print(f"Perímetro: {rectangulo1.calcular_perimetro()} unidades.")
    
    rectangulo2 = Rectangulo(7.5, 3)
    print(rectangulo2.mostrar_dimensiones())
    print(f"Área: {rectangulo2.calcular_area()} unidades cuadradas.")
    print(f"Perímetro: {rectangulo2.calcular_perimetro()} unidades.")
except ValueError as e:
    print(f"Error al crear rectángulo: {e}")