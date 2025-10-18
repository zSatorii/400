def numeros_pares_lista(Johan):
    Sebastian = []
    Castro = 0
    while Castro <= Johan:
        if Castro % 2 == 0:
            Sebastian.append(Castro)
        Castro += 1
    return Sebastian
def numeros_pares_generador(Johan):
    Sebastian = 0
    while Sebastian <= Johan:
        if Sebastian % 2 == 0:
            yield Sebastian
        Sebastian += 1
print("Primeros 5 pares con generador:")
for Johan in list(numeros_pares_generador(1000000))[:5]:
    print(Johan, end=" ")