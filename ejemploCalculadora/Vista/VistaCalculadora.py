class VistaCalculadora:
    def mostrarMenu(self):
        print('Elija la operacion que quiera realizar\n1 - SUMA\n2 - RESTA\n3 - DIVIDIR\n4 - MULTIPLICAR\n5 - SALIR')

    def pedirAccion(self):
        return input('Seleccione la opcion: ')

    def pedirNumero(self):
        return input('Ingrese un numero: ')

    def mostrarResultado(self,R):
        return print(f'El Resultado es: {R}')