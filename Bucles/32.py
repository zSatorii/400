import time
from functools import wraps

def medir_tiempo(Johan):
    @wraps(Johan)
    def Sebastian(*Castro, **Gonzalez):
        inicio = time.time()
        resultado = Johan(*Castro, **Gonzalez)
        fin = time.time()
        tiempo = fin - inicio
        print(f"{Johan.__name__} tardó {tiempo:.4f} segundos")
        return resultado
    return Sebastian

@medir_tiempo
def proceso_lento(Johan):
    Sebastian = 0
    for Castro in range(Johan):
        Sebastian += Castro
    return Sebastian

@medir_tiempo
def proceso_medio(Johan):
    return sum([Sebastian for Sebastian in range(Johan)])

@medir_tiempo
def proceso_rapido(Johan):
    return sum(range(Johan))

print("Comparando rendimiento con n = 1,000,000:\\n")
Sebastian = proceso_lento(1000000)
print(f"Resultado: {Sebastian}\\n")

Castro = proceso_medio(1000000)
print(f"Resultado: {Castro}\\n")

Gonzalez = proceso_rapido(1000000)
print(f"Resultado: {Gonzalez}\\n")