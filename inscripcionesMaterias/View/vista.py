#vista
class VistaAlumno:
    def mostrarMateriasDisponibles(self, materias):
        if not materias:
            print("No hay MATERIAS DISPONIBLES")
        else:
            print("MATERIAS DISPONBILES:")
            for indice, materia in enumerate(materias):
                print(f"{indice + 1}. {materia.nombre}")

    def mostrarMensaje(self, mensaje):
        print(mensaje)

    def mostrarMenu(self):
        print("1 - Mostrar materias disponibles\n2 - Marcar materia como aprobada\n3 - Verificar inscripción en materia\n4 - Salir\nSeleccione una opción: ")

