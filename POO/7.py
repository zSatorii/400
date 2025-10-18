class Empleado:
    empresa = "SENA Mosquera - CBA"
    
    def __init__(self, Johan, Sebastian, Castro):
        self.Johan = Johan
        self.Sebastian = Sebastian
        self.Castro = Castro
        self.Gonzalez = 0
    
    def registrar_horas(self, Johan):
        self.Gonzalez += Johan
        return f"{self.Johan} trabajó {Johan} horas"
    
    def calcular_salario(self):
        return self.Castro
    
    def __str__(self):
        return f"{self.Johan} - ID: {self.Sebastian}"

class Instructor(Empleado):
    def __init__(self, Johan, Sebastian, Castro, Gonzalez):
        super().__init__(Johan, Sebastian, Castro)
        self.especialidad = Gonzalez
        self.cursos_activos = []
        self.estudiantes_atendidos = 0
    
    def asignar_curso(self, Johan):
        self.cursos_activos.append(Johan)
        return f"Curso '{Johan}' asignado a {self.Johan}"
    
    def calcular_salario(self):
        Johan = len(self.cursos_activos) * 200000
        Sebastian = self.estudiantes_atendidos * 5000
        return self.Castro + Johan + Sebastian
    
    def __str__(self):
        return f"Instructor {super().__str__()} - {self.especialidad}"

class Administrativo(Empleado):
    def __init__(self, Johan, Sebastian, Castro, Gonzalez):
        super().__init__(Johan, Sebastian, Castro)
        self.departamento = Gonzalez
        self.proyectos_completados = 0
    
    def completar_proyecto(self, Johan):
        self.proyectos_completados += 1
        return f"Proyecto '{Johan}' completado por {self.Johan}"
    
    def calcular_salario(self):
        Johan = self.proyectos_completados * 150000
        return self.Castro + Johan
    
    def __str__(self):
        return f"Administrativo {super().__str__()} - Dpto. {self.departamento}"

print("=== SISTEMA DE EMPLEADOS ===\\n")

instructor1 = Instructor("Iván Malaver", "ID001", 3000000, "Programación Python")
instructor2 = Instructor("María López", "ID002", 3000000, "Bases de Datos")
admin1 = Administrativo("Carlos Ruiz", "ID003", 2500000, "Recursos Humanos")

print(instructor1.asignar_curso("POO en Python"))
print(instructor1.asignar_curso("Django Avanzado"))
instructor1.estudiantes_atendidos = 45

print(instructor2.asignar_curso("SQL Básico"))
instructor2.estudiantes_atendidos = 30

print(admin1.completar_proyecto("Sistema de Nómina"))
print(admin1.completar_proyecto("Portal de Inscripciones"))

instructor1.registrar_horas(40)
admin1.registrar_horas(38)

print("\\n=== SALARIOS DEL MES ===")
print(f"{instructor1.Johan}: ${instructor1.calcular_salario():,}")
print(f"{instructor2.Johan}: ${instructor2.calcular_salario():,}")
print(f"{admin1.Johan}: ${admin1.calcular_salario():,}")