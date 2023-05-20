import os
import sys

sys.path.append(os.getcwd())

from Modelo.Producto import Producto
from Modelo.Carrito import Carrito
from Modelo.ItemCarrito import ItemCarrito

def main():
    while True:
        selection = int(input('MENU PRINCIPAL\n1 - Cargar Cliente\n2 - Cargar Productos\n3 - SALIR'))
        if selection == 1:
                #CARGAR CLIENTES
                clientes = []       
                while True:
                    nombre = input("Ingrese el nombre del cliente (o 'salir' para terminar): ")
                    if nombre.lower() == "salir":
                        break

                    apellido = input("Ingrese el apellido del cliente: ")
                    cliente = nombre + " " + apellido
                    clientes.append(cliente)

                if os.path.exists("Files\clientes.txt"):
                    with open("Files\clientes.txt", "a+") as archivo:
                        archivo.seek(0)
                        clientes_existentes = archivo.readlines()

                        for cliente_existente in clientes_existentes:
                            if cliente_existente.strip() == cliente:
                                opcion = input(f"El cliente '{cliente}' ya existe. ¿Desea eliminarlo antes de cargarlo? (s/n): ")
                                if opcion.lower() == "s":
                                    clientes.remove(cliente)
                                break

                        archivo.write('\n'.join(clientes) + '\n')
                else:
                    with open("Files\clientes.txt", "w") as archivo:
                        archivo.write('\n'.join(clientes) + '\n')

                print("Clientes cargados correctamente en el archivo")
        elif selection == 2:
                productos = []
                while True:
                    codigo = input("Ingrese el codigo del producto (o 'salir' para terminar): ")
                    if codigo.lower() == "salir":
                        break
                    nombre = input("Ingrese el nombre del producto: ")
                   
                    
                    precio = input("Ingrese el precio del producto: ")
                    producto = codigo + ";" + nombre + ";" + precio
                    productos.append(producto)

                if os.path.exists("Files\productos.txt"):
                    with open("Files\productos.txt", "a+") as archivo:
                        archivo.seek(0)
                        productosExistentes = archivo.readlines()

                        print(productosExistentes)

                        for producto_Existente in productosExistentes:
                            print (producto_Existente)
                            if producto_Existente.strip() == producto:
                                opcion = input(f"El producto '{producto}' ya existe. ¿Desea eliminarlo? (s/n): ")
                                if opcion.lower() == "s":
                                    productos.remove(producto)
                                break

                        archivo.write('\n'.join(productos) + '\n')
                else:
                    with open("Files\productos.txt", "w") as archivo:
                        archivo.write('\n'.join(productos) + '\n')

                print("Productos cargados correctamente en el archivo")
        elif selection == 3:
            print('Usted salio del programa')
            break

if __name__ == '__main__':
    main()