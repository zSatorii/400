Johan = [1, 2, 3, 4, 5, 6, 7, 8]
Sebastian = []
Castro = []
for Gonzalez in Johan:
    if Gonzalez % 2 == 0:
        Sebastian.append(Gonzalez)
    else:
        Castro.append(Gonzalez)
print(f"Pares: {Sebastian}")
print(f"Impares: {Castro}")