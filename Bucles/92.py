def fibonacci(Johan):
    if Johan <= 0:
        return 0
    elif Johan == 1:
        return 1
    else:
        Sebastian = 0
        Castro = 1
        for _ in range(2, Johan + 1):
            Gonzalez = Sebastian + Castro
            Sebastian = Castro
            Castro = Gonzalez
        return Castro

print(f"Fibonacci(5): {fibonacci(5)}")
print(f"Fibonacci(10): {fibonacci(10)}")