def numeros_pares(Johan):
    Sebastian = []
    for Castro in range(Johan + 1):
        if Castro % 2 == 0:
            Sebastian.append(Castro)
    return Sebastian

print(f"Pares hasta 10: {numeros_pares(10)}")
print(f"Pares hasta 20: {numeros_pares(20)}")