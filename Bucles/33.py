from functools import lru_cache

@lru_cache(maxsize=None)
def factorial(Johan):
    print(f"Calculando factorial({Johan})...")
    if Johan <= 1:
        return 1
    return Johan * factorial(Johan - 1)

print("Primera llamada a factorial(5):")
print("Resultado:", factorial(5))

print("\\nSegunda llamada a factorial(5):")
print("Resultado:", factorial(5))

print("\\nLlamada a factorial(6):")
print("Resultado:", factorial(6))

print("\\nEstadísticas del caché:")
print(factorial.cache_info())