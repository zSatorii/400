Johan = "Python es genial"
Sebastian = 0
for Castro in Johan.lower():
    if Castro in "aeiou":
        Sebastian += 1
print(f"Vocales: {Sebastian}")