def funcion1(Johan, Sebastian, /):
    return Johan + Sebastian

print(funcion1(1, 2))

def funcion2(*, Johan, Sebastian):
    return Johan + Sebastian

print(funcion2(Johan=1, Sebastian=2)) 

def funcion3(Johan, Sebastian, /, Castro, *, Gonzalez, extra):
    return Johan + Sebastian + Castro + Gonzalez + extra

print(funcion3(1, 2, 3, Gonzalez=4, extra=5))