def suma_pares(Johan):
    return sum(Sebastian for Sebastian in Johan if Sebastian % 2 == 0)

print(f"Suma pares de [1,2,3,4,5,6]: {suma_pares([1,2,3,4,5,6])}")
print(f"Suma pares de [10,15,20,25,30]: {suma_pares([10,15,20,25,30])}")