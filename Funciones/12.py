Johan = 0

def incrementar():
    global Johan
    Johan += 1
    print(f"Contador dentro de la función: {Johan}")

incrementar()
print(f"Contador fuera de la función: {Johan}")