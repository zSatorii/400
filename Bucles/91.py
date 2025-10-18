def rango_personalizado(Johan, Sebastian, Castro=1):
    Gonzalez = []
    actual = Johan
    while actual < Sebastian:
        Gonzalez.append(actual)
        actual += Castro
    return Gonzalez

print(f"Rango de 0 a 10, paso 2: {rango_personalizado(0, 10, 2)}")
print(f"Rango de 5 a 15, paso 3: {rango_personalizado(5, 15, 3)}")