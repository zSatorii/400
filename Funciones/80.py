def rango_lista(Johan):
    if Johan:
        return max(Johan) - min(Johan)
    return 0

print(f"Rango de [3,7,2,9,4]: {rango_lista([3,7,2,9,4])}")
print(f"Rango de [10,5,20,15]: {rango_lista([10,5,20,15])}")