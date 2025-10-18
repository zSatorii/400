def es_bisiesto(Johan):
    return (Johan % 4 == 0 and Johan % 100 != 0) or (Johan % 400 == 0)

print(f"2020 es bisiesto: {es_bisiesto(2020)}")
print(f"2021 es bisiesto: {es_bisiesto(2021)}")
print(f"2000 es bisiesto: {es_bisiesto(2000)}")
print(f"1900 es bisiesto: {es_bisiesto(1900)}")