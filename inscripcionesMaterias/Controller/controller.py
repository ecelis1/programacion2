#Controler
from Modelo.model import Alumno, Materia
from View.vista import VistaAlumno


class AlumnoController:
    def __init__(self, alumno):
        self.alumno = alumno
        self.materias = []
        self.view = VistaAlumno()

    def agregarMateria(self, nombre, correlativas):
        materia = Materia(nombre, correlativas)
        self.materias.append(materia)
        self.view.mostrarMensaje("Materia AGREGADA")

    def mostrarMateriasDisponibles(self):
        self.view.mostrarMateriasDisponibles(self.materias)

    def verificarInscripcion(self, indiceMateria):
        if indiceMateria < 1 or indiceMateria > len(self.materias):
            self.view.mostrarMensaje("Índice de materia INCORRECTO")
            return

        materia = self.materias[indiceMateria - 1]

        if materia.verificarMateriaAprobada(self.alumno):
            self.view.mostrarMensaje("Puede inscribirse en la materia")
        else:
            self.view.mostrarMensaje("No puede inscribirse en la materia")

    def marcarMateriaComoAprobada(self, indiceMateria):

        if indiceMateria < 1 or indiceMateria > len(self.materias):
            self.view.mostrarMensaje("Índice de materia INCORRECTO")
            return

        materia = self.materias[indiceMateria - 1]

        #comprobacion si la materia tiene una correlativa y si está aprobada
        if materia.correlativas:
            for correlativa in materia.correlativas:
                if correlativa not in self.alumno.materiasAprobadas:
                    self.view.mostrarMensaje(
                        "No puede marcar la materia como APROBADA, porque la materia correlativa NO ESTÁ APROBADA")
                    return

        self.alumno.agregarMateriaAprobada(materia)
        self.view.mostrarMensaje("Materia marcada como APROBADA")
