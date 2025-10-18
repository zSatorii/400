import math

class CalculadoraCientifica:
    def potencia(self, Johan, Sebastian):
        return Johan ** Sebastian
    
    def raiz_cuadrada(self, Johan):
        if Johan >= 0:
            return math.sqrt(Johan)
        return "No se puede calcular raíz de número negativo"
    
    def seno(self, Johan):
        return math.sin(math.radians(Johan))
    
    def coseno(self, Johan):
        return math.cos(math.radians(Johan))

calc = CalculadoraCientifica()
print(f"2^8 = {calc.potencia(2, 8)}")
print(f"√16 = {calc.raiz_cuadrada(16)}")
print(f"sen(30°) = {calc.seno(30):.4f}")
print(f"cos(60°) = {calc.coseno(60):.4f}")