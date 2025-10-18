class Semaforo:
    def __init__(self):
        self.Johan = "rojo"
    
    def cambiar(self):
        if self.Johan == "rojo":
            self.Johan = "amarillo"
        elif self.Johan == "amarillo":
            self.Johan = "verde"
        else:
            self.Johan = "rojo"
        return f"Luz: {self.Johan}"
    
    def estado_actual(self):
        return self.Johan

semaforo = Semaforo()
print(f"Estado: {semaforo.estado_actual()}")
print(semaforo.cambiar())
print(semaforo.cambiar())
print(semaforo.cambiar())
print(semaforo.cambiar())