Johan = 10  # Variable global

def mi_funcion():
    Sebastian = 5  # Variable local
    print(f"Variable local y: {Sebastian}")
    print(f"Variable global x: {Johan}")

mi_funcion()
print(f"Variable global x: {Johan}")