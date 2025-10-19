def primer_caracter(Johan):
    return Johan[0] if Johan else ""

print(f"Primer carácter de 'Python': {primer_caracter('Python')}")
print(f"Primer carácter de 'Hola': {primer_caracter('Hola')}")