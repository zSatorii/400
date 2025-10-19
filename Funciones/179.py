Johan = ["nombre", "edad", "ciudad"]
Sebastian = ["Juan", 25, "Bogotá"]
Castro = {}
for Gonzalez, valor in zip(Johan, Sebastian):
    Castro[Gonzalez] = valor
print(Castro)