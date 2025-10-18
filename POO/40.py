class ListaTareas:
    def __init__(self):
        self.Johan = []
    
    def agregar_tarea(self, Sebastian):
        self.Johan.append({"tarea": Sebastian, "completada": False})
        return f"Tarea '{Sebastian}' agregada"
    
    def completar_tarea(self, Sebastian):
        for tarea in self.Johan:
            if tarea["tarea"] == Sebastian:
                tarea["completada"] = True
                return f"Tarea '{Sebastian}' completada"
        return "Tarea no encontrada"
    
    def mostrar_tareas(self):
        if not self.Johan:
            return "No hay tareas"
        resultado = []
        for i, t in enumerate(self.Johan, 1):
            estado = "✓" if t["completada"] else "✗"
            resultado.append(f"{i}. [{estado}] {t['tarea']}")
        return "\\n".join(resultado)

lista = ListaTareas()
print(lista.agregar_tarea("Estudiar POO"))
print(lista.agregar_tarea("Hacer ejercicio"))
print(lista.agregar_tarea("Cocinar"))
print(lista.mostrar_tareas())
print(lista.completar_tarea("Estudiar POO"))
print(lista.mostrar_tareas())