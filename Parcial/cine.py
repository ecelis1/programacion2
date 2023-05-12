import os

def cargar(matriz):
    mostrarReservas(matriz)
    while True:
        while True:
            try:
                fila = int(input('Introduce la fila que quieres: '))
                if fila<=0 or fila>4:
                    continue
                else:
                    break
            except ValueError:
                print('No se acepta caracteres, ingrese un valor entero.')
            
        while True:
            try:
                columna = int(input('Introduce la columna que quieres: '))
                if columna<=0 or columna>5:
                    continue
                else:
                    break
            except ValueError:
                print('No se acepta caracteres, por favor ingrese un entero.')
        
        if matriz[fila-1][columna-1]=='O':
            print('La fila esta Ocupada')
            continue
        else:
            matriz[fila-1][columna-1]='O'
            print('RESERVA REALIZADA...')
            decision = str.lower(input('QUIERES SEGUIR RESERVANDO LUGARES?\n s/n?'))
            
            
            try:
                if decision == 'n':
                    input('GRACIAS!!. PRESIONE ENTER PARA VOLVER AL MENU PRINCIPAL')
                    break
                else:
                    continue
    #faltaria cerrar cuando ponga otra letra que no sera s o n

            except ValueError:
                print('Ingrese un string')
             



def mostrarReservas(matriz):
    print('Reservas de Butacas')
    for linea in range(4):
        for columna in range(5):
            print(matriz[linea][columna],end=' ')
        print(" ")

def guardarReservas(matriz):
    with open('reservasCine.txt','w')as archivo:
        archivo.write('RESERVA DE BUTACAS\n')
        for filas in matriz:
            archivo.write(' '.join(filas) + '\n')
        fecha=str(input('INGRESE LA FECHA: '))
        archivo.write(fecha)


def menuPrincipal():
    print('EL CINE DE EMANUEL CELIS\n1-CARGAR UNA RESERVA\n2-MOSTRAR RESERVAS\n3-GUARDAR RESERVAS\n4-SALIR\nIngrese su opcion(1-3): ')

def main():
    seleccion:0  

    cine = [['X' for columnas in range(5)] for filas in range(4)]

   # with open('reservasCine.txt','r') as archivo:
#        archivo.readline()
 #           contenido=archivo.readlines()
  #          contenido.pop(4)
   #         for i in range(4):
    #            for j in range(5):
     #               if contenido[i][j]==cine[i][j]:
    #            print('Valores iguales encontrados')
    #               else:
    #                   print('Valores distintos se reemplaza')
     #                   cine[i][j]=contenido[i][j]

 #Quise hacer la comparacion con un archivo ya existente, pero no me acuerdo la funcion,para poder eliminar los espacios, sino cada vez que compara, compara un espacio con el valor que tiene, y ya empieza a cargar espaciso a la matriz y quita todo los resultados correctos, solo pude tomar la primera columna, lo demas no lo pude hacer.                   

                
    mostrarReservas(cine)

    while True:
        try:
            seleccion = int(input(f'{menuPrincipal()}'))
        except ValueError:
            print('Ingrese un Entero, no se admite caracteres')

        else:
            match seleccion:
                case 1:
                    cargar(cine)
                case 2:
                    mostrarReservas(cine)
                case 3:
                    guardarReservas(cine)
                case 4:
                    print('Ha salido del programa.')
                    break




if __name__ == '__main__':
    main()
