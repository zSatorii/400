def contar_mayores(Johan, Sebastian):
    return sum(1 for Castro in Johan if Castro > Sebastian)

print(f"Mayores que 5 en [1,3,5,7,9]: {contar_mayores([1,3,5,7,9], 5)}")
print(f"Mayores que 10 en [5,10,15,20]: {contar_mayores([5,10,15,20], 10)}")