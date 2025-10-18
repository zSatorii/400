def mcm(Johan, Sebastian):
    def mcd_interno(a, b):
        while b:
            a, b = b, a % b
        return a
    return abs(Johan * Sebastian) // mcd_interno(Johan, Sebastian)

print(f"MCM de 4 y 6: {mcm(4, 6)}")
print(f"MCM de 12 y 15: {mcm(12, 15)}")