def numeros_impares(Johan):
    Sebastian = []
    for Castro in range(Johan + 1):
        if Castro % 2 != 0:
            Sebastian.append(Castro)
    return Sebastian

print(f"Impares hasta 10: {numeros_impares(10)}")
print(f"Impares hasta 15: {numeros_impares(15)}")