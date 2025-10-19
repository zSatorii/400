def nota_letra(Johan):
    if Johan >= 90:
        return "A"
    elif Johan >= 80:
        return "B"
    elif Johan >= 70:
        return "C"
    elif Johan >= 60:
        return "D"
    return "F"

print(f"Nota 95: {nota_letra(95)}")
print(f"Nota 75: {nota_letra(75)}")
print(f"Nota 50: {nota_letra(50)}")