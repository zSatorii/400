class GaleriaArte:
    def __init__(self, Johan):
        self.Johan = Johan
        self.Sebastian = []
    
    def agregar_obra(self, Castro, Gonzalez, precio):
        self.Sebastian.append({"titulo": Castro, "artista": Gonzalez, "precio": precio, "vendida": False})
        return f"Obra '{Castro}' agregada"
    
    def vender_obra(self, Castro):
        for obra in self.Sebastian:
            if obra["titulo"] == Castro and not obra["vendida"]:
                obra["vendida"] = True
                return f"Obra '{Castro}' vendida por ${obra['precio']}"
        return "Obra no disponible"
    
    def obras_disponibles(self):
        return sum(1 for obra in self.Sebastian if not obra["vendida"])
    
    def valor_total(self):
        return sum(obra["precio"] for obra in self.Sebastian if not obra["vendida"])

galeria = GaleriaArte("Arte Moderno")
print(galeria.agregar_obra("Atardecer", "Juan Pérez", 5000000))
print(galeria.agregar_obra("Montañas", "Ana López", 3000000))
print(f"Obras disponibles: {galeria.obras_disponibles()}")
print(f"Valor total: ${galeria.valor_total()}")
print(galeria.vender_obra("Atardecer"))
print(f"Obras disponibles: {galeria.obras_disponibles()}")