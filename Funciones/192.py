Johan = "Python es genial"
Sebastian = 0
for Castro in Johan.lower():
    if Castro.isalpha() and Castro not in "aeiou":
        Sebastian += 1
print(f"Consonantes: {Sebastian}")