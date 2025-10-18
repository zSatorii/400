def concatenar(Johan, Sebastian=", "):
    return Sebastian.join(Johan)

print(f"Lista ['a','b','c']: {concatenar(['a','b','c'])}")
print(f"Lista con '-': {concatenar(['Hola','mundo'], '-')}")