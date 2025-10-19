def suma_impares(Johan):
    return sum(Sebastian for Sebastian in Johan if Sebastian % 2 != 0)

print(f"Suma impares de [1,2,3,4,5,6]: {suma_impares([1,2,3,4,5,6])}")
print(f"Suma impares de [10,15,20,25,30]: {suma_impares([10,15,20,25,30])}")