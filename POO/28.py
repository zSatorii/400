class Contador:
    def __init__(self, Johan=0):
        self.Johan = Johan
    
    def incrementar(self):
        self.Johan += 1
        return self.Johan
    
    def decrementar(self):
        self.Johan -= 1
        return self.Johan
    
    def reiniciar(self):
        self.Johan = 0
        return "Contador reiniciado"
    
    def valor_actual(self):
        return self.Johan

contador = Contador()
print(f"Valor: {contador.valor_actual()}")
print(f"Incrementar: {contador.incrementar()}")
print(f"Incrementar: {contador.incrementar()}")
print(f"Incrementar: {contador.incrementar()}")
print(f"Decrementar: {contador.decrementar()}")
print(f"Valor: {contador.valor_actual()}")
print(contador.reiniciar())