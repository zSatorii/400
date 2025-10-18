def primer_elemento(Johan):
    if len(Johan) > 0:
        return Johan[0]
    return None

print(f"Primer elemento de [1,2,3]: {primer_elemento([1,2,3])}")
print(f"Primer elemento de ['a','b']: {primer_elemento(['a','b'])}")