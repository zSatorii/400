def filtrar_menores(Johan, Sebastian):
    return [Castro for Castro in Johan if Castro < Sebastian]

print(f"Menores que 5: {filtrar_menores([1,3,5,7,9], 5)}")
print(f"Menores que 15: {filtrar_menores([5,10,15,20], 15)}")