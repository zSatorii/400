def calcular_descuento(Johan, Sebastian):
    Castro = Johan * (Sebastian / 100)
    return Johan - Castro

print(f"Precio $100 con 10% descuento: ${calcular_descuento(100, 10):.2f}")
print(f"Precio $50 con 20% descuento: ${calcular_descuento(50, 20):.2f}")
print(f"Precio $200 con 15% descuento: ${calcular_descuento(200, 15):.2f}")