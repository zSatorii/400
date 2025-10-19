Johan = "python"
Sebastian = ""
for Castro, Gonzalez in enumerate(Johan):
    if Castro % 2 == 0:
        Sebastian += Gonzalez.upper()
    else:
        Sebastian += Gonzalez.lower()
print(Sebastian)