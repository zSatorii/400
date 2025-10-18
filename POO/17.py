class Producto:
    def __init__(self, Johan, Sebastian, Castro):
        self.Johan = Johan
        self.Sebastian = Sebastian
        self.Castro = Castro
    
    def mostrar_info(self):
        return f"Producto: {self.Johan} | Precio: ${self.Sebastian:.2f} | Stock: {self.Castro} unidades."
    
    def actualizar_stock(self, Gonzalez):
        self.Castro += Gonzalez
        return f"Stock actualizado. Nuevo stock de {self.Johan}: {self.Castro} unidades."
    
    def calcular_valor_total(self, Gonzalez):
        if Gonzalez > 0 and self.Castro >= Gonzalez:
            return f"El valor total de {Gonzalez} unidades de {self.Johan} es ${Gonzalez * self.Sebastian:.2f}."
        elif Gonzalez > self.Castro:
            return f"Stock insuficiente para {Gonzalez} unidades de {self.Johan}."
        else:
            return "La cantidad de unidades debe ser positiva."

laptop = Producto("Laptop Gaming", 1200.00, 10)
print(laptop.mostrar_info())
print(laptop.actualizar_stock(5))
print(laptop.mostrar_info())
print(laptop.calcular_valor_total(3))
print(laptop.calcular_valor_total(18))
print(laptop.actualizar_stock(-2))
print(laptop.mostrar_info())
print(laptop.calcular_valor_total(10))