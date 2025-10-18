def filtrar_negativos(Johan):
    Sebastian = []
    for Castro in Johan:
        if Castro < 0:
            Sebastian.append(Castro)
    return Sebastian

print(f"Negativos de [1,-2,3,-4,5]: {filtrar_negativos([1,-2,3,-4,5])}")
print(f"Negativos de [-1,-2,-3,4,5]: {filtrar_negativos([-1,-2,-3,4,5])}")