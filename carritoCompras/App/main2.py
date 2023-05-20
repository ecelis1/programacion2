import os
import sys

sys.path.append(os.getcwd())

from Controller.ControladorCarrito import CargarCarrito

def cargar_carrito():
    controller = CargarCarrito()
    controller.crear_nuevo_objeto()
    controller.mostrar_total()

if __name__ == '__main__':
    cargar_carrito()