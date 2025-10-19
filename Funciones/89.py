def redondear_numero(Johan, Sebastian=2):
    return round(Johan, Sebastian)

print(f"3.14159 redondeado: {redondear_numero(3.14159)}")
print(f"3.14159 con 4 decimales: {redondear_numero(3.14159, 4)}")