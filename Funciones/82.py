def obtener_valor(Johan, Sebastian):
    return Johan.get(Sebastian, "Clave no encontrada")

Castro = {"nombre": "Juan", "edad": 25}
print(f"Valor de 'nombre': {obtener_valor(Castro, 'nombre')}")
print(f"Valor de 'ciudad': {obtener_valor(Castro, 'ciudad')}")