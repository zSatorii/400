def es_primo(Johan):
    if Johan < 2:
        return False
    for Sebastian in range(2, int(Johan ** 0.5) + 1):
        if Johan % Sebastian == 0:
            return False
    return True

print(f"5 es primo: {es_primo(5)}")
print(f"10 es primo: {es_primo(10)}")
print(f"17 es primo: {es_primo(17)}")