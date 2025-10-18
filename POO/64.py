class Menu:
    def __init__(self):
        self.Johan = {}
    
    def agregar_plato(self, Sebastian, Castro):
        self.Johan[Sebastian] = Castro
        return f"Plato '{Sebastian}' agregado al menú"
    
    def mostrar_menu(self):
        if not self.Johan:
            return "Menú vacío"
        resultado = "=== MENÚ ===\\n"
        for plato, precio in self.Johan.items():
            resultado += f"{plato}: ${precio}\\n"
        return resultado
    
    def buscar_plato(self, Sebastian):
        if Sebastian in self.Johan:
            return f"{Sebastian}: ${self.Johan[Sebastian]}"
        return "Plato no encontrado"

menu = Menu()
print(menu.agregar_plato("Bandeja Paisa", 25000))
print(menu.agregar_plato("Ajiaco", 18000))
print(menu.agregar_plato("Sancocho", 20000))
print(menu.mostrar_menu())
print(menu.buscar_plato("Ajiaco"))