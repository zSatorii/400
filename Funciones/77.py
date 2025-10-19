def par_impar_lista(Johan):
    Sebastian = sum(1 for Castro in Johan if Castro % 2 == 0)
    Gonzalez = len(Johan) - Sebastian
    return {"pares": Sebastian, "impares": Gonzalez}

print(f"En [1,2,3,4,5,6]: {par_impar_lista([1,2,3,4,5,6])}")
print(f"En [10,15,20,25]: {par_impar_lista([10,15,20,25])}")