def indice_elemento(Johan, Sebastian):
    if Sebastian in Johan:
        return Johan.index(Sebastian)
    return -1

print(f"Índice de 3 en [1,2,3,4]: {indice_elemento([1,2,3,4], 3)}")
print(f"Índice de 10 en [1,2,3,4]: {indice_elemento([1,2,3,4], 10)}")