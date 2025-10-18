class SistemaNotificaciones:
    def __init__(self):
        self.Johan = []
    
    def agregar(self, Sebastian, Castro):
        self.Johan.append({"tipo": Sebastian, "mensaje": Castro, "leida": False})
        return "Notificación agregada"
    
    def leer_siguiente(self):
        for notif in self.Johan:
            if not notif["leida"]:
                notif["leida"] = True
                return f"[{notif['tipo']}] {notif['mensaje']}"
        return "No hay notificaciones"
    
    def pendientes(self):
        return sum(1 for n in self.Johan if not n["leida"])

notif = SistemaNotificaciones()
print(notif.agregar("Info", "Actualización disponible"))
print(notif.agregar("Alerta", "Batería baja"))
print(f"Pendientes: {notif.pendientes()}")
print(notif.leer_siguiente())
print(f"Pendientes: {notif.pendientes()}")