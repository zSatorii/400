class CorreoElectronico:
    def __init__(self, Johan):
        self.Johan = Johan
        self.Sebastian = []
        self.Castro = []
    
    def recibir(self, Gonzalez, remitente):
        self.Sebastian.append({"asunto": Gonzalez, "de": remitente, "leido": False})
        return f"Nuevo correo de {remitente}"
    
    def leer(self, indice):
        if 0 <= indice < len(self.Sebastian):
            self.Sebastian[indice]["leido"] = True
            return f"Leyendo: {self.Sebastian[indice]['asunto']}"
        return "Correo no existe"
    
    def no_leidos(self):
        return sum(1 for correo in self.Sebastian if not correo["leido"])

email = CorreoElectronico("usuario@mail.com")
print(email.recibir("Reunión", "jefe@empresa.com"))
print(email.recibir("Oferta", "promo@tienda.com"))
print(f"No leídos: {email.no_leidos()}")
print(email.leer(0))
print(f"No leídos: {email.no_leidos()}")