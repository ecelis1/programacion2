
from Controlador.ControladorUsuario import ControladorUsuario

def main():
    controller = ControladorUsuario()
    controller.modelo.cargarUsuariosArchivo()

    while True:
        seleccion = input(controller.vista.MostrarMenu())

        if seleccion == "1":
            controller.UsuariosHabilitados()
        elif seleccion == "2":
            controller.verificarSiPassEsFuerte()
        elif seleccion == "3":
            dni = input('Ingrese el DNI del USUARIO: ')
            controller.verificarPasswordUsuario(dni)
        elif seleccion == "4":
            controller.verificarRegistro()
        elif seleccion == "5":
            break
        else:
            print("Opción INCORRECTA. Por favor, seleccione nuevamente.")
    
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
