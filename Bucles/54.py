def promedio(*Johan):
    if len(Johan) == 0:
        return 0
    return sum(Johan) / len(Johan)

print(f"Promedio de 5, 8, 10: {promedio(5, 8, 10):.2f}")
print(f"Promedio de 7, 9, 6, 8: {promedio(7, 9, 6, 8):.2f}")
print(f"Promedio de 10, 10, 10: {promedio(10, 10, 10):.2f}")