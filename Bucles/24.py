def log(Johan):
    def Sebastian(*Castro, **Gonzalez):
        print(f"Llamando a {Johan.__name__}...")
        resultado = Johan(*Castro, **Gonzalez)
        print(f"{Johan.__name__} terminó")
        return resultado
    return Sebastian

@log
def sumar(Johan, Sebastian):
    return Johan + Sebastian

@log
def multiplicar(Johan, Sebastian):
    return Johan * Sebastian

print("Resultado:", sumar(3, 4))
print()
print("Resultado:", multiplicar(5, 6))