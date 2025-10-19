def contar_menores(Johan, Sebastian):
    return sum(1 for Castro in Johan if Castro < Sebastian)

print(f"Menores que 5 en [1,3,5,7,9]: {contar_menores([1,3,5,7,9], 5)}")
print(f"Menores que 15 en [5,10,15,20]: {contar_menores([5,10,15,20], 15)}")