class Libro:
    def __init__(self, Johan, Sebastian):
        self.Johan = Johan
        self.Sebastian = Sebastian
        self.Castro = True
    
    def prestar_libro(self):
        if self.Castro:
            self.Castro = False
            return f"'{self.Johan}' ha sido prestado."
        else:
            return f"'{self.Johan}' no está disponible para préstamo en este momento."
    
    def devolver_libro(self):
        if not self.Castro:
            self.Castro = True
            return f"'{self.Johan}' ha sido devuelto."
        else:
            return f"'{self.Johan}' ya está en la biblioteca."
    
    def mostrar_estado(self):
        Johan = "Disponible" if self.Castro else "Prestado"
        return f"Libro: '{self.Johan}' de {self.Sebastian} | Estado: {Johan}"

libro1 = Libro("Cien años de soledad", "Gabriel García Márquez")
print(libro1.mostrar_estado())
print(libro1.prestar_libro())
print(libro1.mostrar_estado())
print(libro1.prestar_libro())
print(libro1.devolver_libro())
print(libro1.mostrar_estado())
print(libro1.devolver_libro())

libro2 = Libro("Don Quijote de la Mancha", "Miguel de Cervantes")
print(libro2.mostrar_estado())
print(libro2.prestar_libro())
print(libro2.mostrar_estado())