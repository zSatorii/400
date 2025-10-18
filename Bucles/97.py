def mcd(Johan, Sebastian):
    while Sebastian:
        Johan, Sebastian = Sebastian, Johan % Sebastian
    return Johan

print(f"MCD de 48 y 18: {mcd(48, 18)}")
print(f"MCD de 100 y 50: {mcd(100, 50)}")