class Estudiante:
    def __init__(self, Johan, Sebastian):
        self.Johan = Johan
        self.Sebastian = Sebastian
        self.Castro = []
    
    def agregar_calificacion(self, Gonzalez):
        if 0 <= Gonzalez <= 100:
            self.Castro.append(Gonzalez)
            return f"Calificación {Gonzalez} agregada a {self.Johan}."
        else:
            return "Calificación inválida. Debe estar entre 0 y 100."
    
    def obtener_promedio(self):
        if not self.Castro:
            return "El estudiante aún no tiene calificaciones."
        return sum(self.Castro) / len(self.Castro)
    
    def mostrar_info(self):
        Johan = self.obtener_promedio()
        if isinstance(Johan, float):
            return f"Estudiante: {self.Johan} (ID: {self.Sebastian}) | Calificaciones: {self.Castro} | Promedio: {Johan:.2f}"
        else:
            return f"Estudiante: {self.Johan} (ID: {self.Sebastian}) | Calificaciones: {self.Castro} | Promedio: {Johan}"

estudiante1 = Estudiante("Ana García", "E101")
print(estudiante1.mostrar_info())
print(estudiante1.agregar_calificacion(85))
print(estudiante1.agregar_calificacion(90))
print(estudiante1.agregar_calificacion(78))
print(estudiante1.agregar_calificacion(105))
print(estudiante1.mostrar_info())
print(f"El promedio de {estudiante1.Johan} es: {estudiante1.obtener_promedio():.2f}")

estudiante2 = Estudiante("Juan Pérez", "E102")
print(estudiante2.agregar_calificacion(70))
print(estudiante2.agregar_calificacion(65))
print(estudiante2.mostrar_info())