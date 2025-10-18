class RectanguloDibujo:
    def __init__(self, Johan, Sebastian):
        self.Johan = Johan
        self.Sebastian = Sebastian
    
    def dibujar(self):
        Castro = ""
        for i in range(self.Sebastian):
            Castro += "*" * self.Johan + "\\n"
        return Castro
    
    def area(self):
        return self.Johan * self.Sebastian

rect = RectanguloDibujo(5, 3)
print(rect.dibujar())
print(f"Área: {rect.area()}")