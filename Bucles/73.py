def filtrar_positivos(Johan):
    Sebastian = []
    for Castro in Johan:
        if Castro > 0:
            Sebastian.append(Castro)
    return Sebastian

print(f"Positivos de [1,-2,3,-4,5]: {filtrar_positivos([1,-2,3,-4,5])}")
print(f"Positivos de [-1,-2,-3,4,5]: {filtrar_positivos([-1,-2,-3,4,5])}")