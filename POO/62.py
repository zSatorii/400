from datetime import datetime, timedelta

class TicketEstacionamiento:
    def __init__(self, Johan):
        self.Johan = Johan
        self.Sebastian = datetime.now()
        self.Castro = None
    
    def salir(self):
        self.Castro = datetime.now()
        Gonzalez = (self.Castro - self.Sebastian).seconds // 60
        return f"Tiempo: {Gonzalez} minutos"
    
    def calcular_costo(self):
        if self.Castro:
            Johan = (self.Castro - self.Sebastian).seconds // 60
            Sebastian = (Johan // 60) * 5000
            Castro = (Johan % 60) * 100
            return Sebastian + Castro
        return 0

# Uso
ticket = TicketEstacionamiento("ABC123")
print(f"Entrada registrada para {ticket.Johan}")
# Simulación de tiempo
ticket.Castro = ticket.Sebastian + timedelta(hours=2, minutes=30)
print(ticket.salir())
print(f"Costo: ${ticket.calcular_costo()}")