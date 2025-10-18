class ChatSimple:
    def __init__(self, Johan):
        self.Johan = Johan
        self.Sebastian = []
    
    def enviar_mensaje(self, Castro, Gonzalez):
        self.Sebastian.append(f"{Castro}: {Gonzalez}")
        return "Mensaje enviado"
    
    def ver_mensajes(self):
        if not self.Sebastian:
            return "No hay mensajes"
        return "\\n".join(self.Sebastian)
    
    def limpiar_chat(self):
        self.Sebastian = []
        return "Chat limpiado"

chat = ChatSimple("Sala POO")
print(chat.enviar_mensaje("Juan", "Hola!"))
print(chat.enviar_mensaje("María", "¿Cómo estás?"))
print(chat.ver_mensajes())