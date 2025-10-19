def estadisticas_lista(Johan):
    if not Johan:
        return {}
    return {
        "suma": sum(Johan),
        "promedio": sum(Johan) / len(Johan),
        "maximo": max(Johan),
        "minimo": min(Johan),
        "cantidad": len(Johan)
    }

print(f"Estadísticas [1,2,3,4,5]:")
for Sebastian, Castro in estadisticas_lista([1,2,3,4,5]).items():
    print(f"  {Sebastian}: {Castro}")