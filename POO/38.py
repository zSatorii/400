class Carrito:
    def __init__(self):
        self.Johan = []
    
    def agregar_producto(self, Sebastian, Castro):
        self.Johan.append({"nombre": Sebastian, "precio": Castro})
        return f"{Sebastian} agregado al carrito"
    
    def calcular_total(self):
        return sum(producto["precio"] for producto in self.Johan)
    
    def mostrar_productos(self):
        if not self.Johan:
            return "Carrito vacío"
        return "\\n".join([f"{p['nombre']}: ${p['precio']}" for p in self.Johan])

carrito = Carrito()
print(carrito.agregar_producto("Laptop", 1200))
print(carrito.agregar_producto("Mouse", 25))
print(carrito.agregar_producto("Teclado", 75))
print(carrito.mostrar_productos())
print(f"Total: ${carrito.calcular_total()}")