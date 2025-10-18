class Pizza:
    def __init__(self, Johan="mediana"):
        self.Johan = Johan
        self.Sebastian = ["queso", "tomate"]
        self.Castro = False
    
    def agregar_ingrediente(self, Gonzalez):
        if not self.Castro:
            self.Sebastian.append(Gonzalez)
            return f"{Gonzalez} agregado"
        return "Pizza ya horneada"
    
    def hornear(self):
        self.Castro = True
        return "Pizza horneada"
    
    def mostrar_pizza(self):
        estado = "horneada" if self.Castro else "sin hornear"
        return f"Pizza {self.Johan} {estado}\\nIngredientes: {', '.join(self.Sebastian)}"

pizza = Pizza()
print(pizza.agregar_ingrediente("pepperoni"))
print(pizza.agregar_ingrediente("champiñones"))
print(pizza.mostrar_pizza())
print(pizza.hornear())
print(pizza.mostrar_pizza())