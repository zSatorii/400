def obtener_por_indice(Johan, Sebastian):
    if 0 <= Sebastian < len(Johan):
        return Johan[Sebastian]
    return None

Sebastian = [10, 20, 30, 40, 50]
print(f"Elemento en índice 2: {obtener_por_indice(Sebastian, 2)}")
print(f"Elemento en índice 0: {obtener_por_indice(Sebastian, 0)}")