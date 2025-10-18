def mostrar_datos(**Johan):
    print("Información recibida:")
    for Sebastian, Castro in Johan.items():
        print(f"  {Sebastian}: {Castro}")

mostrar_datos(nombre="Ana", edad=20, ciudad="Bogotá")
print()
mostrar_datos(producto="Laptop", precio=1500000, marca="Dell", año=2023)