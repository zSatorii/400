def contar_vocales(Johan):
    Sebastian = "aeiouAEIOU"
    Castro = 0
    for Gonzalez in Johan:
        if Gonzalez in Sebastian:
            Castro += 1
    return Castro

print(f"Vocales en 'Hola': {contar_vocales('Hola')}")
print(f"Vocales en 'Python': {contar_vocales('Python')}")
print(f"Vocales en 'Murcielago': {contar_vocales('Murcielago')}")