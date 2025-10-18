class BibliotecaSimple:
    def __init__(self):
        self.Johan = []
    
    def agregar_libro(self, Sebastian):
        self.Johan.append({"titulo": Sebastian, "prestado": False})
        return f"'{Sebastian}' agregado"
    
    def prestar(self, Sebastian):
        for libro in self.Johan:
            if libro["titulo"] == Sebastian and not libro["prestado"]:
                libro["prestado"] = True
                return f"'{Sebastian}' prestado"
        return "Libro no disponible"
    
    def devolver(self, Sebastian):
        for libro in self.Johan:
            if libro["titulo"] == Sebastian and libro["prestado"]:
                libro["prestado"] = False
                return f"'{Sebastian}' devuelto"
        return "Libro no encontrado"

biblio = BibliotecaSimple()
print(biblio.agregar_libro("Python Básico"))
print(biblio.prestar("Python Básico"))
print(biblio.devolver("Python Básico"))