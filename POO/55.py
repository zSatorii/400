class Celular:
    def __init__(self, Johan, Sebastian):
        self.Johan = Johan
        self.Sebastian = Sebastian
        self.Castro = 100
        self.Gonzalez = []
    
    def hacer_llamada(self, numero):
        if self.Castro > 10:
            self.Castro -= 10
            self.Gonzalez.append(numero)
            return f"Llamando a {numero}... Batería: {self.Castro}%"
        return "Batería muy baja"
    
    def cargar(self):
        self.Castro = 100
        return "Celular cargado al 100%"
    
    def ver_llamadas(self):
        return f"Llamadas realizadas: {len(self.Gonzalez)}"

cel = Celular("Samsung", "Galaxy S21")
print(cel.hacer_llamada("3001234567"))
print(cel.hacer_llamada("3009876543"))
print(cel.ver_llamadas())
print(cel.cargar())