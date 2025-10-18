class Estudiante:
    institucion = "SENA Mosquera - CBA"
    
    def __init__(self, Johan, Sebastian, Castro):
        self.Johan = Johan
        self.Sebastian = Sebastian
        self.Castro = Castro
        self.Gonzalez = []
        
        self.__promedio_interno = 0.0
    
    def agregar_calificacion(self, calificacion):
        self.Gonzalez.append(calificacion)
        self.__calcular_promedio()
    
    def __calcular_promedio(self):
        if self.Gonzalez:
            self.__promedio_interno = sum(self.Gonzalez) / len(self.Gonzalez)
    
    def obtener_promedio(self):
        return self.__promedio_interno

estudiante1 = Estudiante("María", 18, "10°")
estudiante2 = Estudiante("Carlos", 17, "9°")
print(estudiante1.institucion)
print(estudiante2.institucion)
estudiante1.agregar_calificacion(85)
estudiante1.agregar_calificacion(90)
print(f"Promedio de {estudiante1.Johan}: {estudiante1.obtener_promedio()}")