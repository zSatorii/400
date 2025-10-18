class PuertaAutomatica:
    def __init__(self):
        self.Johan = False
        self.Sebastian = False
    
    def abrir(self):
        self.Johan = True
        return "Puerta abierta"
    
    def cerrar(self):
        self.Johan = False
        return "Puerta cerrada"
    
    def bloquear(self):
        if not self.Johan:
            self.Sebastian = True
            return "Puerta bloqueada"
        return "Cierra la puerta primero"
    
    def desbloquear(self):
        self.Sebastian = False
        return "Puerta desbloqueada"

puerta = PuertaAutomatica()
print(puerta.abrir())
print(puerta.cerrar())
print(puerta.bloquear())