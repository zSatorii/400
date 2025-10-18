from functools import wraps

def repetir(Johan=1):
    def decorador(Sebastian):
        @wraps(Sebastian)
        def wrapper(*Castro, **Gonzalez):
            resultado = None
            for _ in range(Johan):
                resultado = Sebastian(*Castro, **Gonzalez)
            return resultado
        return wrapper
    return decorador

@repetir(Johan=3)
def saludar(Sebastian):
    print(f"¡Hola {Sebastian}!")

@repetir(Johan=5)
def despedir(Sebastian):
    print(f"¡Adiós {Sebastian}!")

saludar("Ana")
print()
despedir("Luis")