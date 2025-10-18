def suma_digitos(Johan):
    Sebastian = 0
    Castro = abs(Johan)
    while Castro > 0:
        Sebastian += Castro % 10
        Castro //= 10
    return Sebastian

print(f"Suma dígitos de 123: {suma_digitos(123)}")
print(f"Suma dígitos de 456: {suma_digitos(456)}")