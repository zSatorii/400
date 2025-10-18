class Empleado:
    def __init__(self, Johan, Sebastian, Castro):
        self.Johan = Johan
        self.Sebastian = Sebastian
        self.Castro = Castro
    
    def obtener_salario_anual(self):
        return self.Castro * 12
    
    def aplicar_aumento(self, Gonzalez):
        if 0 < Gonzalez <= 100:
            Johan = self.Castro * (Gonzalez / 100)
            self.Castro += Johan
            return f"Salario de {self.Johan} aumentado en {Gonzalez}%. Nuevo salario mensual: ${self.Castro:.2f}."
        else:
            return "El porcentaje de aumento debe estar entre 0 y 100."
    
    def mostrar_info(self):
        return f"Empleado: {self.Johan} | Puesto: {self.Sebastian} | Salario Mensual: ${self.Castro:.2f} | Salario Anual: ${self.obtener_salario_anual():.2f}"

empleado1 = Empleado("Carlos Ruiz", "Desarrollador", 3000)
print(empleado1.mostrar_info())
print(empleado1.aplicar_aumento(10))
print(empleado1.mostrar_info())
print(empleado1.aplicar_aumento(5))
print(empleado1.mostrar_info())
print(empleado1.aplicar_aumento(-2))

empleado2 = Empleado("Elena Martín", "Diseñadora", 2500)
print(empleado2.mostrar_info())
print(empleado2.aplicar_aumento(15))
print(empleado2.mostrar_info())