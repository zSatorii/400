def ultimo_elemento(Johan):
    if len(Johan) > 0:
        return Johan[-1]
    return None

print(f"Último elemento de [1,2,3]: {ultimo_elemento([1,2,3])}")
print(f"Último elemento de ['a','b','c']: {ultimo_elemento(['a','b','c'])}")