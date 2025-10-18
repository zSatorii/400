def eliminar_duplicados(Johan):
    return list(set(Johan))

print(f"Lista sin duplicados [1,2,2,3,3,3]: {eliminar_duplicados([1,2,2,3,3,3])}")
print(f"Lista sin duplicados [5,5,5,5]: {eliminar_duplicados([5,5,5,5])}")