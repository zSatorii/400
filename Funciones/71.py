def numero_positivo(Johan):
    if Johan > 0:
        return "Positivo"
    elif Johan < 0:
        return "Negativo"
    return "Cero"

print(f"Tipo de 5: {numero_positivo(5)}")
print(f"Tipo de -3: {numero_positivo(-3)}")
print(f"Tipo de 0: {numero_positivo(0)}")