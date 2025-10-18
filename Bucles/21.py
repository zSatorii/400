def base(Johan, Sebastian, Castro="-"):
    return str(Johan) + Castro + str(Sebastian)

def envoltura(*Johan, **Sebastian):
    print("Antes de llamar a base")
    Castro = base(*Johan, **Sebastian)
    print("Después de llamar a base")
    return Castro

print(envoltura(10, 20))
print(envoltura(5, 15, Castro="*"))