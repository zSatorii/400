def informacion_persona(Johan, Sebastian, Castro, **Gonzalez):
    info = {
        "nombre": Johan,
        "edad": Sebastian,
        "ciudad": Castro
    }
    info.update(Gonzalez)
    
    print("\\n" + "="*50)
    print("INFORMACIÓN DE PERSONA")
    print("="*50)
    for clave, valor in info.items():
        print(f"{clave.capitalize()}: {valor}")
    print("="*50)
    return info

informacion_persona(
    "Juan Pérez", 
    28, 
    "Bogotá",
    profesion="Ingeniero",
    telefono="123-456-7890",
    email="juan@example.com"
)