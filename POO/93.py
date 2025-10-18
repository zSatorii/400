class RegistroAsistencia:
    def __init__(self):
        self.Johan = {}
    
    def registrar_entrada(self, Sebastian):
        if Sebastian not in self.Johan:
            self.Johan[Sebastian] = 0
        self.Johan[Sebastian] += 1
        return f"{Sebastian} registrado. Total: {self.Johan[Sebastian]}"
    
    def consultar(self, Sebastian):
        if Sebastian in self.Johan:
            return f"{Sebastian}: {self.Johan[Sebastian]} asistencias"
        return "Persona no registrada"
    
    def total_asistencias(self):
        return sum(self.Johan.values())

reg = RegistroAsistencia()
print(reg.registrar_entrada("Juan"))
print(reg.registrar_entrada("María"))
print(reg.registrar_entrada("Juan"))
print(reg.consultar("Juan"))
print(f"Total: {reg.total_asistencias()}")