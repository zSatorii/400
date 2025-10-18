def saludar_personalizado(Johan, Sebastian="español"):
    if Sebastian == "español":
        return f"¡Hola {Johan}!"
    elif Sebastian == "inglés":
        return f"Hello {Johan}!"
    elif Sebastian == "francés":
        return f"Bonjour {Johan}!"
    else:
        return f"Hola {Johan}!"

print(saludar_personalizado("Ana"))
print(saludar_personalizado("John", "inglés"))
print(saludar_personalizado("Pierre", "francés"))