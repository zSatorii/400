class Password:
    def __init__(self, Johan):
        self.Johan = Johan
    
    def verificar(self, Sebastian):
        if Sebastian == self.Johan:
            return "Contraseña correcta"
        return "Contraseña incorrecta"
    
    def cambiar(self, Castro, Sebastian):
        if Castro == self.Johan:
            self.Johan = Sebastian
            return "Contraseña cambiada exitosamente"
        return "Contraseña actual incorrecta"
    
    def es_fuerte(self):
        if len(self.Johan) >= 8 and any(c.isdigit() for c in self.Johan):
            return True
        return False

pwd = Password("miPass123")
print(pwd.verificar("123456"))
print(pwd.verificar("miPass123"))
print(f"¿Es fuerte? {pwd.es_fuerte()}")
print(pwd.cambiar("miPass123", "nuevoPass456"))
print(pwd.verificar("nuevoPass456"))