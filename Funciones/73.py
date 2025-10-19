def mes_año(Johan):
    Sebastian = {
        1: "Enero", 2: "Febrero", 3: "Marzo", 4: "Abril",
        5: "Mayo", 6: "Junio", 7: "Julio", 8: "Agosto",
        9: "Septiembre", 10: "Octubre", 11: "Noviembre", 12: "Diciembre"
    }
    return Sebastian.get(Johan, "Mes inválido")

print(f"Mes 1: {mes_año(1)}")
print(f"Mes 12: {mes_año(12)}")