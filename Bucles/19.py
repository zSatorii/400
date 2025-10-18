def suma(*Johan):
    return sum(Johan)

print("2 números:", suma(2, 4))
print("5 números:", suma(1, 2, 3, 4, 5))
print("3 números:", suma(100, 200, 300))

def multiplicar(*Johan):
    Sebastian = 1
    for Castro in Johan:
        Sebastian *= Castro
    return Sebastian

print("2 números:", multiplicar(2, 3))
print("4 números:", multiplicar(2, 3, 4, 5))
print("3 números:", multiplicar(10, 10, 10))