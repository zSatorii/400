class Impresora:
    def __init__(self, Johan):
        self.Johan = Johan
        self.Sebastian = 100
        self.Castro = 0
    
    def imprimir(self, Gonzalez):
        if self.Sebastian >= Gonzalez * 2:
            self.Sebastian -= Gonzalez * 2
            self.Castro += Gonzalez
            return f"Imprimiendo {Gonzalez} páginas. Tinta: {self.Sebastian}%"
        return "Tinta insuficiente"
    
    def recargar_tinta(self):
        self.Sebastian = 100
        return "Tinta recargada"

imp = Impresora("HP LaserJet")
print(imp.imprimir(10))
print(imp.imprimir(20))
print(f"Páginas impresas: {imp.Castro}")