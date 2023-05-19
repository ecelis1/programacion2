import os
import sys

sys.path.append(os.getcwd())

from Clases.Producto import Producto
from Clases.Carrito import Carrito
from Clases.ItemCarrito import ItemCarrito
from Functions.cargarCliente import cargarCliente
from Functions.cargarProductos import cargarProductos

def main():
    while True:
        selection = int(input('MENU PRINCIPAL\n1 - Cargar Cliente\n2 - Cargar Productos\n3 - SALIR'))
        if selection == 1:
                cargarCliente()
        elif selection == 2:
                cargarProductos()
        elif selection == 3:
            print('Usted salio del programa')
            break

if __name__ == '__main__':
    main()