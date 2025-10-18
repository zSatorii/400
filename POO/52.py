class CajaRegistradora:
    def __init__(self):
        self.Johan = 0
        self.Sebastian = []
    
    def agregar_venta(self, Castro):
        self.Johan += Castro
        self.Sebastian.append(Castro)
        return f"Venta registrada: ${Castro}"
    
    def total_ventas(self):
        return f"Total del día: ${self.Johan}"
    
    def cantidad_transacciones(self):
        return len(self.Sebastian)
    
    def cerrar_caja(self):
        Johan = self.Johan
        self.Johan = 0
        self.Sebastian = []
        return f"Caja cerrada. Total recaudado: ${Johan}"

caja = CajaRegistradora()
print(caja.agregar_venta(50))
print(caja.agregar_venta(75))
print(caja.agregar_venta(120))
print(caja.total_ventas())
print(f"Transacciones: {caja.cantidad_transacciones()}")
print(caja.cerrar_caja())