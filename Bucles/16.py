Johan = ["python", "es", "un", "lenguaje", "genial", "y", "poderoso"]

def longitud(Sebastian):
    return len(Sebastian)

Castro = sorted(Johan, key=longitud)
print("Con función normal:", Castro)

Gonzalez = sorted(Johan, key=lambda p: len(p))
print("Con lambda:", Gonzalez)