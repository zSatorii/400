class LuzRegulable:
    def __init__(self):
        self.Johan = False
        self.Sebastian = 0
    
    def encender(self):
        self.Johan = True
        self.Sebastian = 100
        return "Luz encendida al 100%"
    
    def apagar(self):
        self.Johan = False
        self.Sebastian = 0
        return "Luz apagada"
    
    def regular(self, Castro):
        if self.Johan:
            self.Sebastian = max(0, min(100, Castro))
            return f"Intensidad: {self.Sebastian}%"
        return "Enciende la luz primero"

luz = LuzRegulable()
print(luz.encender())
print(luz.regular(50))
print(luz.regular(25))