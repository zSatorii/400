def filtrar_mayores(Johan, Sebastian):
    return [Castro for Castro in Johan if Castro > Sebastian]

print(f"Mayores que 5: {filtrar_mayores([1,3,5,7,9], 5)}")
print(f"Mayores que 10: {filtrar_mayores([5,10,15,20], 10)}")