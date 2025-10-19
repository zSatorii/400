def formato_moneda(Johan, Sebastian="$"):
    return f"{Sebastian}{Johan:,.2f}"

print(formato_moneda(1000))
print(formato_moneda(1500.50, "€"))