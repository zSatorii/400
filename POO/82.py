class PedidoRestaurante:
    def __init__(self, Johan):
        self.Johan = Johan
        self.Sebastian = []
        self.Castro = "pendiente"
    
    def agregar_item(self, Gonzalez, precio):
        self.Sebastian.append({"item": Gonzalez, "precio": precio})
        return f"{Gonzalez} agregado"
    
    def calcular_total(self):
        return sum(item["precio"] for item in self.Sebastian)
    
    def cambiar_estado(self, Gonzalez):
        self.Castro = Gonzalez
        return f"Estado: {self.Castro}"

pedido = PedidoRestaurante("Mesa 5")
print(pedido.agregar_item("Pizza", 25000))
print(pedido.agregar_item("Gaseosa", 5000))
print(f"Total: ${pedido.calcular_total()}")
print(pedido.cambiar_estado("en preparación"))