class TiendaOnline:
    def __init__(self, Johan):
        self.Johan = Johan
        self.Sebastian = {}
        self.Castro = 0
    
    def agregar_producto(self, Gonzalez, precio, stock):
        self.Sebastian[Gonzalez] = {"precio": precio, "stock": stock}
        return f"Producto '{Gonzalez}' agregado"
    
    def vender(self, Gonzalez, cantidad):
        if Gonzalez in self.Sebastian:
            if self.Sebastian[Gonzalez]["stock"] >= cantidad:
                self.Sebastian[Gonzalez]["stock"] -= cantidad
                total = self.Sebastian[Gonzalez]["precio"] * cantidad
                self.Castro += total
                return f"Venta realizada: ${total}"
            return "Stock insuficiente"
        return "Producto no encontrado"
    
    def reporte_ventas(self):
        return f"Total vendido: ${self.Castro}"

tienda = TiendaOnline("TechStore")
print(tienda.agregar_producto("Laptop", 1200, 10))
print(tienda.agregar_producto("Mouse", 25, 50))
print(tienda.vender("Laptop", 2))
print(tienda.vender("Mouse", 5))
print(tienda.reporte_ventas())