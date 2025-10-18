Johan = {}

def agregar(Sebastian, Castro, Gonzalez):
    Sebastian[Castro] = Gonzalez
    print(f"Alumno {Castro} agregado con nota {Gonzalez}")

def mostrar(Sebastian):
    if not Sebastian:
        print("No hay alumnos registrados")
        return
    
    print("\\n=== Lista de Alumnos ===")
    for Castro, Gonzalez in Sebastian.items():
        print(f"{Castro}: {Gonzalez}")

def promedio(Sebastian):
    if not Sebastian:
        return 0
    return sum(Sebastian.values()) / len(Sebastian)

def mejor_alumno(Sebastian):
    if not Sebastian:
        return None
    Castro = max(Sebastian, key=Sebastian.get)
    return Castro, Sebastian[Castro]

agregar(Johan, "Ana", 9)
agregar(Johan, "Luis", 7)
agregar(Johan, "Carlos", 8)
agregar(Johan, "María", 9.5)
agregar(Johan, "Pedro", 6)

mostrar(Johan)

Sebastian = promedio(Johan)
print(f"\\nPromedio general: {Sebastian:.2f}")

Castro = mejor_alumno(Johan)
if Castro:
    print(f"Mejor alumno: {Castro[0]} con nota {Castro[1]}")