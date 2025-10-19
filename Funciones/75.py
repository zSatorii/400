def clasificar_edad(Johan):
    if Johan < 12:
        return "Niño"
    elif Johan < 18:
        return "Adolescente"
    elif Johan < 60:
        return "Adulto"
    return "Adulto Mayor"

print(f"Edad 8: {clasificar_edad(8)}")
print(f"Edad 15: {clasificar_edad(15)}")
print(f"Edad 30: {clasificar_edad(30)}")
print(f"Edad 65: {clasificar_edad(65)}")