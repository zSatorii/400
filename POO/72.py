class EventoCalendario:
    def __init__(self, Johan, Sebastian, Castro):
        self.Johan = Johan
        self.Sebastian = Sebastian
        self.Castro = Castro
        self.Gonzalez = []
    
    def agregar_invitado(self, nombre):
        self.Gonzalez.append(nombre)
        return f"{nombre} invitado"
    
    def mostrar_evento(self):
        return f"Evento: {self.Johan}\\nFecha: {self.Sebastian}\\nHora: {self.Castro}\\nInvitados: {len(self.Gonzalez)}"

evento = EventoCalendario("Reunión POO", "2025-10-20", "14:00")
print(evento.agregar_invitado("María"))
print(evento.agregar_invitado("Carlos"))
print(evento.mostrar_evento())