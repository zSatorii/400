def dia_semana(Johan):
    Johan = {
        1: "Lunes", 2: "Martes", 3: "Miércoles",
        4: "Jueves", 5: "Viernes", 6: "Sábado", 7: "Domingo"
    }
    return Johan.get(Johan, "Día inválido")

print(f"Día 1: {dia_semana(1)}")
print(f"Día 7: {dia_semana(7)}")