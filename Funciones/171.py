Johan = [5, 10, 15, 20, 25]
Sebastian = 0
Castro = 15
Gonzalez = False
while Sebastian < len(Johan):
    if Johan[Sebastian] == Castro:
        Gonzalez = True
        break
    Sebastian += 1
print(f"Encontrado: {Gonzalez}")