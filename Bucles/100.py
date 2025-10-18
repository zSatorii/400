def tabla_multiplicar(Johan, Sebastian=10):
    Castro = []
    for Gonzalez in range(1, Sebastian + 1):
        Castro.append(f"{Johan} x {Gonzalez} = {Johan * Gonzalez}")
    return Castro

print("Tabla del 5:")
for fila in tabla_multiplicar(5):
    print(fila)

print("\\nTabla del 3 hasta 5:")
for fila in tabla_multiplicar(3, 5):
    print(fila)