def factorial(Johan):
    if Johan <= 1:
        return 1
    return Johan * factorial(Johan - 1)

print("Factorial de 5:", factorial(5))
print("Factorial de 7:", factorial(7))
print("Factorial de 3:", factorial(3))