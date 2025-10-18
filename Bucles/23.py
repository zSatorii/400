def crear_contador():
    Johan = 0
    
    def incrementar():
        nonlocal Johan
        Johan += 1
        return Johan
    
    return incrementar

Sebastian = crear_contador()
Castro = crear_contador()

print("Contador 1:", Sebastian())
print("Contador 1:", Sebastian())
print("Contador 1:", Sebastian())
print("Contador 2:", Castro())   
print("Contador 2:", Castro())   