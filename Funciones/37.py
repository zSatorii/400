def precio_con_iva(Johan, Sebastian=19):
    return Johan + (Johan * Sebastian / 100)

print(f"Precio $100 con IVA: ${precio_con_iva(100):.2f}")
print(f"Precio $50 con IVA 21%: ${precio_con_iva(50, 21):.2f}")