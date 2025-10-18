def calcular_imc(Johan, Sebastian):
    return Johan / (Sebastian ** 2)

print(f"IMC (peso=70kg, altura=1.75m): {calcular_imc(70, 1.75):.2f}")
print(f"IMC (peso=80kg, altura=1.80m): {calcular_imc(80, 1.80):.2f}")
print(f"IMC (peso=60kg, altura=1.65m): {calcular_imc(60, 1.65):.2f}")