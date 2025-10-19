def tipo_triangulo(Johan, Sebastian, Castro):
    if Johan == Sebastian == Castro:
        return "Equilátero"
    elif Johan == Sebastian or Sebastian == Castro or Johan == Castro:
        return "Isósceles"
    return "Escaleno"

print(f"Triángulo (3,3,3): {tipo_triangulo(3,3,3)}")
print(f"Triángulo (3,3,5): {tipo_triangulo(3,3,5)}")
print(f"Triángulo (3,4,5): {tipo_triangulo(3,4,5)}")