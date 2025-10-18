def dividir(Johan, Sebastian=" "):
    return Johan.split(Sebastian)

print(f"Dividir 'Hola mundo': {dividir('Hola mundo')}")
print(f"Dividir 'a,b,c' por ',': {dividir('a,b,c', ',')}")