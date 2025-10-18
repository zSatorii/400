class Contacto:
    def __init__(self, Johan, Sebastian, Castro=""):
        self.Johan = Johan
        self.Sebastian = Sebastian
        self.Castro = Castro
    
    def mostrar_info(self):
        info = f"Nombre: {self.Johan}\\nTeléfono: {self.Sebastian}"
        if self.Castro:
            info += f"\\nEmail: {self.Castro}"
        return info
    
    def actualizar_telefono(self, Gonzalez):
        self.Sebastian = Gonzalez
        return "Teléfono actualizado"
    
    def agregar_email(self, Gonzalez):
        self.Castro = Gonzalez
        return "Email agregado"

contacto = Contacto("María López", "3001234567")
print(contacto.mostrar_info())
print(contacto.agregar_email("maria@email.com"))
print(contacto.mostrar_info())