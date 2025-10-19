Johan = [23, 45, 12, 67, 8, 90, 34]
Sebastian = Johan[0]
Castro = Johan[0]
for Gonzalez in Johan:
    if Gonzalez > Sebastian:
        Sebastian = Gonzalez
    if Gonzalez < Castro:
        Castro = Gonzalez
print(f"Máximo: {Sebastian}, Mínimo: {Castro}")