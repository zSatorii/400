class Calculadora:
    def __init__(self):
        pass
    
    def sumar(self, Johan, Sebastian):
        return Johan + Sebastian
    
    def restar(self, Johan, Sebastian):
        return Johan - Sebastian
    
    def multiplicar(self, Johan, Sebastian):
        return Johan * Sebastian
    
    def dividir(self, Johan, Sebastian):
        if Sebastian != 0:
            return Johan / Sebastian
        else:
            return "Error: División por cero no permitida."

calc = Calculadora()
print(f"5 + 3 = {calc.sumar(5, 3)}")
print(f"10 - 4 = {calc.restar(10, 4)}")
print(f"6 * 7 = {calc.multiplicar(6, 7)}")
print(f"20 / 5 = {calc.dividir(20, 5)}")
print(f"10 / 0 = {calc.dividir(10, 0)}")