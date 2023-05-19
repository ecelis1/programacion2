import os
def cargarProductos():
    productos = []

    while True:
        nombre = input("Ingrese el nombre del producto (o 'salir' para terminar): ")
        if nombre.lower() == "salir":
            break

        cantidad = input("Ingrese el cantidad del producto: ")
        producto = nombre + " " + cantidad
        productos.append(producto)

    if os.path.exists("Files\productos.txt"):
        with open("Files\productos.txt", "a+") as archivo:
            archivo.seek(0)
            productosExistentes = archivo.readlines()

            for producto_Existente in productosExistentes:
                if producto_Existente.strip() == producto:
                    opcion = input(f"El producto '{producto}' ya existe. ¿Desea eliminarlo? (s/n): ")
                    if opcion.lower() == "s":
                        productos.remove(producto)
                    break

            archivo.write('\n'.join(productos) + '\n')
    else:
        with open("Files\productos.txt", "w") as archivo:
            archivo.write('\n'.join([productos]) + '\n')

    print("Productos cargados correctamente en el archivo")
