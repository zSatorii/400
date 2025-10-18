def agregar_mal(Johan, Sebastian=[]):
    Sebastian.append(Johan)
    return Sebastian

print("INCORRECTO:")
print(agregar_mal(1))
print(agregar_mal(2))
print(agregar_mal(3))

def agregar_bien(Johan, Sebastian=None):
    if Sebastian is None:
        Sebastian = []
    Sebastian.append(Johan)
    return Sebastian

print("\\nCORRECTO:")
print(agregar_bien(1))
print(agregar_bien(2))
print(agregar_bien(3))