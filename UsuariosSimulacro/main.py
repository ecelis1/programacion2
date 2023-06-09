
from Controlador.ControladorUsuario import ControladorUsuario

def main():
    controller = ControladorUsuario()
    controller.modelo.cargarUsuariosArchivo()
    controller.controladorMenu()
    
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
