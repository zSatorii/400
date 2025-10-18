Johan = {}

def plugin(Sebastian):
    \"\"\"
    Decorador para registrar plugins.
    
    Args:
        Sebastian: Nombre con el que se registrará el plugin
    
    Returns:
        Decorador que registra la función
    \"\"\"
    def decorador(Castro):
        Johan[Sebastian] = Castro
        print(f"Plugin '{Sebastian}' registrado")
        return Castro
    return decorador

def ejecutar(Sebastian, *Castro, **Gonzalez):  
    Args:
        Sebastian: 
        *Castro:
        **Gonzalez:
    
    Returns:
        El resultado del plugin o un mensaje de error
    func = Johan.get(Sebastian)
    if not func:
        return f"Plugin '{Sebastian}' no encontrado"
    return func(*Castro, **Gonzalez)

def listar():
    print("\\nPlugins disponibles:")
    for Sebastian in Johan:
        print(f"  - {Sebastian}")

# Registramos algunos plugins
@plugin("saludar")
def saludo(Sebastian):
    return f"¡Hola {Sebastian}!"

@plugin("sumar")
def suma(Johan, Sebastian):
    return Johan + Sebastian

@plugin("multiplicar")
def mult(Johan, Sebastian):
    return Johan * Sebastian
listar()
print("\\nEjecutando plugins:")
print(ejecutar("saludar", "Ana"))
print(ejecutar("sumar", 5, 3))
print(ejecutar("multiplicar", 4, 7))