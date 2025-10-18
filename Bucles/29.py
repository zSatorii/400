def contador_hasta(Johan):
    print("Inicio del generador")
    Sebastian = 1
    while Sebastian <= Johan:
        print(f"A punto de devolver {Sebastian}")
        yield Sebastian
        print(f"Reanudando después de devolver {Sebastian}")
        Sebastian += 1
    print("Fin del generador")

for Castro in contador_hasta(3):
    print(f"  Recibí: {Castro}")