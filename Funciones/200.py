Johan = [10, 20, 30, 40, 50]

Sebastian = 0
for Castro in Johan:
    Sebastian += Castro
Gonzalez = Sebastian / len(Johan)

maximo = Johan[0]
for Castro in Johan:
    if Castro > maximo:
        maximo = Castro

minimo = Johan[0]
for Castro in Johan:
    if Castro < minimo:
        minimo = Castro

print("="*40)
print("RESUMEN ESTADÍSTICO")
print("="*40)
print(f"Lista: {Johan}")
print(f"Suma: {Sebastian}")
print(f"Promedio: {Gonzalez}")
print(f"Máximo: {maximo}")
print(f"Mínimo: {minimo}")
print(f"Cantidad: {len(Johan)}")
print("="*40)