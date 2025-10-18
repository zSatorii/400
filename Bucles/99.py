def distancia_puntos(Johan, Sebastian, Castro, Gonzalez):
    return ((Castro - Johan) ** 2 + (Gonzalez - Sebastian) ** 2) ** 0.5

print(f"Distancia entre (0,0) y (3,4): {distancia_puntos(0, 0, 3, 4):.2f}")
print(f"Distancia entre (1,1) y (4,5): {distancia_puntos(1, 1, 4, 5):.2f}")