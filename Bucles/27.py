from functools import lru_cache
def fibonacci_lento(Johan):
    if Johan < 2:
        return Johan
    return fibonacci_lento(Johan-1) + fibonacci_lento(Johan-2)
@lru_cache(maxsize=None)
def fibonacci_rapido(Johan):
    if Johan < 2:
        return Johan
    return fibonacci_rapido(Johan-1) + fibonacci_rapido(Johan-2)

print("Con caché:", fibonacci_rapido(10))
print("Con caché:", fibonacci_rapido(50))
print("\\nEstadísticas del caché:")
print(fibonacci_rapido.cache_info())