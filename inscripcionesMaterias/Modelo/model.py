#modelo
class Alumno:
    def __init__(self, nombre):
        self.nombre = nombre
        self.materiasAprobadas = []

    def agregarMateriaAprobada(self, materia):
        self.materiasAprobadas.append(materia)

class Materia:
    def __init__(self, nombre, correlativas=[]):
        self.nombre = nombre
        self.correlativas = correlativas

    def verificarMateriaAprobada(self, alumno):
        for materia in self.correlativas:
            if materia not in alumno.materiasAprobadas:
                return False
        return True