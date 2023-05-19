import os

def cargarCliente():
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



