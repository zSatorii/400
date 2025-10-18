def contar_elemento(Johan, Sebastian):
    Castro = 0
    for Gonzalez in Johan:
        if Gonzalez == Sebastian:
            Castro += 1
    return Castro

print(f"Veces que aparece 5 en [1,5,3,5,5]: {contar_elemento([1,5,3,5,5], 5)}")
print(f"Veces que aparece 2 en [2,2,2,3]: {contar_elemento([2,2,2,3], 2)}")