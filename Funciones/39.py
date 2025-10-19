def precio_final(Johan, Sebastian):
    Castro = Johan * (Sebastian / 100)
    return Johan - Castro

print(f"Precio $100 - 15% = ${precio_final(100, 15):.2f}")
print(f"Precio $200 - 25% = ${precio_final(200, 25):.2f}")