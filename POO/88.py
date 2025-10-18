class Encuesta:
    def __init__(self, Johan):
        self.Johan = Johan
        self.Sebastian = 0
        self.Castro = 0
        self.Gonzalez = 0
    
    def responder_si(self):
        self.Sebastian += 1
        return "Respuesta registrada: Sí"
    
    def responder_no(self):
        self.Castro += 1
        return "Respuesta registrada: No"
    
    def responder_nose(self):
        self.Gonzalez += 1
        return "Respuesta registrada: No sé"
    
    def resultados(self):
        total = self.Sebastian + self.Castro + self.Gonzalez
        if total == 0:
            return "Sin respuestas"
        return f"Sí: {self.Sebastian} | No: {self.Castro} | No sé: {self.Gonzalez}"

enc = Encuesta("¿Te gusta Python?")
print(enc.responder_si())
print(enc.responder_si())
print(enc.responder_no())
print(enc.resultados())