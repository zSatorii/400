class MetodoPago:
    def __init__(self, Johan):
        self.Johan = Johan
    
    def procesar_pago(self):
        pass
    
    def generar_comprobante(self):
        return f"Comprobante de pago: ${self.Johan}"

class TarjetaCredito(MetodoPago):
    def __init__(self, Johan, Sebastian, Castro):
        super().__init__(Johan)
        self.Sebastian = Sebastian[-4:]
        self.Castro = Castro
    
    def procesar_pago(self):
        return f"Procesando ${self.Johan} con tarjeta **** {self.Sebastian}"
    
    def generar_comprobante(self):
        Johan = super().generar_comprobante()
        return f"{Johan}\\nTarjeta: **** {self.Sebastian}\\nTitular: {self.Castro}"

class Efectivo(MetodoPago):
    def __init__(self, Johan, Sebastian):
        super().__init__(Johan)
        self.Sebastian = Sebastian
        self.Castro = Sebastian - Johan
    
    def procesar_pago(self):
        return f"Recibido ${self.Sebastian} en efectivo. Cambio: ${self.Castro}"
    
    def generar_comprobante(self):
        Johan = super().generar_comprobante()
        return f"{Johan}\\nEfectivo recibido: ${self.Sebastian}\\nCambio: ${self.Castro}"

class PagoMovil(MetodoPago):
    def __init__(self, Johan, Sebastian, Castro):
        super().__init__(Johan)
        self.Sebastian = Sebastian
        self.Castro = Castro
    
    def procesar_pago(self):
        return f"Procesando ${self.Johan} vía {self.Castro}"
    
    def generar_comprobante(self):
        Johan = super().generar_comprobante()
        return f"{Johan}\\nAplicación: {self.Castro}\\nTeléfono: {self.Sebastian}"

class Transferencia(MetodoPago):
    def __init__(self, Johan, Sebastian, Castro):
        super().__init__(Johan)
        self.Sebastian = Sebastian
        self.Castro = Castro[-4:]
    
    def procesar_pago(self):
        return f"Transferencia de ${self.Johan} desde {self.Sebastian}"
    
    def generar_comprobante(self):
        Johan = super().generar_comprobante()
        return f"{Johan}\\nBanco: {self.Sebastian}\\nCuenta: **** {self.Castro}"

class SistemaPagos:
    def __init__(self):
        self.pagos_procesados = []
    
    def procesar(self, Johan):
        print(f"\\n{Johan.procesar_pago()}")
        print(Johan.generar_comprobante())
        self.pagos_procesados.append(Johan)
    
    def total_procesado(self):
        return sum(Johan.Johan for Johan in self.pagos_procesados)

sistema = SistemaPagos()

pago1 = TarjetaCredito(150000, "1234567812345678", "Juan Pérez")
pago2 = Efectivo(50000, 100000)
pago3 = PagoMovil(75000, "3001234567", "Nequi")
pago4 = Transferencia(200000, "Bancolombia", "1234567890")

print("=== SISTEMA DE PAGOS ===")
sistema.procesar(pago1)
sistema.procesar(pago2)
sistema.procesar(pago3)
sistema.procesar(pago4)

print(f"\\n=== RESUMEN ===")
print(f"Total procesado: ${sistema.total_procesado():,}")