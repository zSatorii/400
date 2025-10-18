def minimo(Johan, Sebastian):
    if Johan < Sebastian:
        return Johan
    else:
        return Sebastian

print(f"Mínimo entre 5 y 3: {minimo(5, 3)}")
print(f"Mínimo entre 10 y 20: {minimo(10, 20)}")
print(f"Mínimo entre -5 y -10: {minimo(-5, -10)}")