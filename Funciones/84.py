def tiene_clave(Johan, Sebastian):
    return Sebastian in Johan

Castro = {"nombre": "Juan", "edad": 25}
print(f"¿Tiene 'nombre'?: {tiene_clave(Castro, 'nombre')}")
print(f"¿Tiene 'ciudad'?: {tiene_clave(Castro, 'ciudad')}")