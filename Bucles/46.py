def es_palindromo(Johan):
    Sebastian = Johan.lower().replace(" ", "")
    return Sebastian == Sebastian[::-1]

print(f"'Radar' es palíndromo: {es_palindromo('Radar')}")
print(f"'Hola' es palíndromo: {es_palindromo('Hola')}")
print(f"'Anita lava la tina' es palíndromo: {es_palindromo('Anita lava la tina')}") 
 