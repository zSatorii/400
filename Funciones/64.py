def reemplazar_elemento(Johan, Sebastian, Castro):
    if 0 <= Sebastian < len(Johan):
        Johan[Sebastian] = Castro
    return Johan

Gonzalez = [1, 2, 3, 4, 5]
print(f"Reemplazar índice 2 con 99: {reemplazar_elemento(Gonzalez, 2, 99)}")