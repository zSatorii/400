class RouterWiFi:
    def __init__(self, Johan):
        self.Johan = Johan
        self.Sebastian = True
        self.Castro = []
    
    def conectar_dispositivo(self, Gonzalez):
        self.Castro.append(Gonzalez)
        return f"{Gonzalez} conectado"
    
    def desconectar_dispositivo(self, Gonzalez):
        if Gonzalez in self.Castro:
            self.Castro.remove(Gonzalez)
            return f"{Gonzalez} desconectado"
        return "Dispositivo no encontrado"
    
    def dispositivos_conectados(self):
        return len(self.Castro)

router = RouterWiFi("MiWiFi_2024")
print(router.conectar_dispositivo("Laptop"))
print(router.conectar_dispositivo("Celular"))
print(f"Dispositivos: {router.dispositivos_conectados()}")