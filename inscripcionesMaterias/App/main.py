#Main
from Controller.controller import AlumnoController
from Modelo.model import Alumno

def main():
    nombreAlumno = input("Ingrese el nombre del alumno: ")
    alumno = Alumno(nombreAlumno)
    controller = AlumnoController(alumno)

    controller.agregarMateria("Programación I", [])
    controller.agregarMateria("Programación II", [controller.materias[0]])
    controller.agregarMateria("Programación III", [controller.materias[1]])

    while True:


        seleccion = input(controller.view.mostrarMenu())

        if seleccion == "1":
            controller.mostrarMateriasDisponibles()
        elif seleccion == "2":
            indiceMateria = int(input("Ingrese el índice de la materia a marcar como aprobada: "))
            controller.marcarMateriaComoAprobada(indiceMateria)
        elif seleccion == "3":
            indiceMateria = int(input("Ingrese el índice de la materia para verificar inscripción: "))
            controller.verificarInscripcion(indiceMateria)
        elif seleccion == "4":
            break
        else:
            print("Opción INCORRECTA. Por favor, seleccione nuevamente.")

if __name__ == "__main__":
    main()

