class Examen:
    def __init__(self, Johan, Sebastian):
        self.Johan = Johan
        self.Sebastian = Sebastian
        self.Castro = {}
    
    def agregar_pregunta(self, Gonzalez, respuesta):
        self.Castro[Gonzalez] = respuesta
        return f"Pregunta {Gonzalez} agregada"
    
    def calificar(self, respuestas):
        Johan = 0
        for pregunta, respuesta in respuestas.items():
            if pregunta in self.Castro and self.Castro[pregunta] == respuesta:
                Johan += 1
        Sebastian = (Johan / len(self.Castro)) * 5.0
        return f"Nota: {Sebastian:.1f}"

examen = Examen("POO", "Python")
examen.agregar_pregunta(1, "A")
examen.agregar_pregunta(2, "C")
examen.agregar_pregunta(3, "B")
respuestas_estudiante = {1: "A", 2: "C", 3: "A"}
print(examen.calificar(respuestas_estudiante))