def externa():
    print("Función externa ejecutándose")
    
    def interna():
        print("Función interna ejecutándose")
    
    interna()
    print("Función externa terminando")

externa()