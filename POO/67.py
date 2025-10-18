class Inventario:
    def __init__(self):
        self.Johan = {}
    
    def agregar_item(self, Sebastian, Castro):
        if Sebastian in self.Johan:
            self.Johan[Sebastian] += Castro
        else:
            self.Johan[Sebastian] = Castro
        return f"{Sebastian}: {self.Johan[Sebastian]} unidades"
    
    def quitar_item(self, Sebastian, Castro):
        if Sebastian in self.Johan:
            if self.Johan[Sebastian] >= Castro:
                self.Johan[Sebastian] -= Castro
                return f"Quedan {self.Johan[Sebastian]} unidades de {Sebastian}"
            return "Stock insuficiente"
        return "Item no encontrado"
    
    def consultar(self, Sebastian):
        if Sebastian in self.Johan:
            return f"{Sebastian}: {self.Johan[Sebastian]} unidades"
        return "Item no encontrado"

# Uso
inv = Inventario()
print(inv.agregar_item("Manzanas", 50))
print(inv.agregar_item("Naranjas", 30))
print(inv.quitar_item("Manzanas", 10))
print(inv.consultar("Manzanas"))