class Nota:
    def __init__(self, Johan, Sebastian):
        self.Johan = Johan
        self.Sebastian = Sebastian
    
    def editar(self, Johan):
        self.Sebastian = Johan
        return "Nota editada"
    
    def mostrar(self):
        return f"Título: {self.Johan}\\nContenido: {self.Sebastian}"

# Uso
nota = Nota("Lista de compras", "Leche, pan, huevos")
print(nota.mostrar())
print(nota.editar("Leche, pan, huevos, queso, jamón"))
print(nota.mostrar())