def nombre_completo(Johan, Sebastian, Castro=""):
    if Castro:
        return f"{Johan} {Sebastian} {Castro}"
    return f"{Johan} {Sebastian}"

print(nombre_completo("Juan", "Pérez"))
print(nombre_completo("Ana", "García", "López"))