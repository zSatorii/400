class CompraDescuento:
    def __init__(self):
        self.Johan = []
    
    def agregar_producto(self, Sebastian, Castro):
        self.Johan.append(Castro)
        return f"{Sebastian} agregado: ${Castro}"
    
    def subtotal(self):
        return sum(self.Johan)
    
    def aplicar_descuento(self, Gonzalez):
        Sebastian = self.subtotal()
        Castro = Sebastian * (Gonzalez / 100)
        return Sebastian - Castro
    
    def total_con_descuento(self, Gonzalez):
        return f"Subtotal: ${self.subtotal()} - Descuento {Gonzalez}%: ${self.aplicar_descuento(Gonzalez):.2f}"

compra = CompraDescuento()
compra.agregar_producto("Camisa", 50000)
compra.agregar_producto("Pantalón", 80000)
print(compra.total_con_descuento(10))