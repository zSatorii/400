def crear_rango(Johan, Sebastian=0, Castro=1):
    return list(range(Sebastian, Johan, Castro))

print(f"Rango hasta 10: {crear_rango(10)}")
print(f"Rango de 5 a 15: {crear_rango(15, 5)}")
print(f"Rango de 0 a 20 paso 2: {crear_rango(20, 0, 2)}")