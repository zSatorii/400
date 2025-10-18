def calcular_impuesto(Johan, Sebastian=19):
    Castro = Johan * (Sebastian / 100)
    return Johan + Castro

print(f"Precio $100 con IVA 19%: ${calcular_impuesto(100):.2f}")
print(f"Precio $50 con IVA 10%: ${calcular_impuesto(50, 10):.2f}")
print(f"Precio $200 con IVA 21%: ${calcular_impuesto(200, 21):.2f}")