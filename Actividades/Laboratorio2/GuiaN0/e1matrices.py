#Una agencia de venta de vehículos automóviles distribuye quince modelos diferentes y tiene en su plantilla diez vendedores. Se desea un programa que escriba un informe mensual de las ventas por vendedor y modelos, así como el número de automóviles vendido por cada vendedor y el número total de cada modelo vendido por todos los vendedores. Asimismo para entregar el premio al mejor vendedor, necesita saber cual es el vendedor que más coches ha vendido.
def matriz_vacia(matriz):
    for fila in matriz:
        for elemento in fila:
            if elemento != 0:
                return False
    return True

def menu():
    menu = 'MENU PRINCIPAL:\n1 - Cargar Datos\n2 - Informe Mensual\n3 - Premio al Mejor Vendedor\n4 - Salir\nIngrese su seleccion: '
    return menu

def imprimirMatriz(matriz,i,j):
    for i in range(i):
        for j in range(j):
            print(matriz[i][j], end=' ')


def cargarMatriz(registroMensual,vendedores,modelo):
    while True:
        vendedores = int(input('Ingrese el num del Vendedor (1 al 10), ingrese 0 para salir del programa.'))

        if vendedores == 0:
            break
        
        while True:
            try:
                modelo = int(input('Ingrese el modelo de la unidad vendida (1 al 15): '))
                
                while True:
                    if modelo<1 or modelo>15:
                        modelo = int(input('POR FAVOR, ingrese el modelo correcto de la unidad vendida (1 al 15): '))
                    else:
                        break
                break


            except (ValueError):
                print('Debes ingresar un valor del 1 al 15, solo se admiten enteros.')


        cantidades = int(input('Ingrese la cantidad vendida de este modelo: '))

        registroMensual[vendedores-1][modelo-1] += cantidades

def informeMensual(matriz):
    print('INFORME MENSUAL')

    for vendedor in range(10):
        totalVendido = 0
        print(f'Vendedor {vendedor+1}: ')

        for modelos in range(14):
            cantidades = registroMensual[vendedor][modelos]
            totalVendido += cantidades

            if cantidades > 0:
                print(f'Modelo {modelos+1}: {cantidades}')
                
        
        print(f'Total de ventas del mes por el vendedor{vendedor+1}: {totalVendido}')
        matriz[vendedor][15]=totalVendido


def elQueMasVendio(matriz):
    
    if matriz_vacia(matriz)==True:
        print('La matriz no posee datos, debes ingresar datos para saber quien es el vendedor que mas vendio')   
    else:
        print('PREMIO AL VENDEDOR QUE MAS VENDIO')
        columna = [vendedores[15] for vendedores in matriz]
        
        #Obtengo el valor maximo de esa lista
        valorMaximo = max(columna)
        
        #Tomo a quien le pertenece el valor de ese dato
        vendedor_Index = columna.index(valorMaximo)

        print(f'El vendedor con mayor ventas es: {vendedor_Index+1} con una cantidad de {valorMaximo} ventas.')

import pprint

vendedores = 10
modelo = 15

registroMensual = [[0 for columnas in range(16)] for filas in range(10)]


while True:
    try:
        seleccion = int(input(f'{menu()}'))
    except(ValueError):
        print('Ingrese un valor correcto, debe ser un entero.')

    match seleccion:
        case 1:
            cargarMatriz(registroMensual,vendedores,modelo)
        case 2:
            informeMensual(registroMensual)
        case 3:
            elQueMasVendio(registroMensual)
        case 4:
            print('Usted salio del programa.')
            break
        case default:
            print('Ingrese una opcion correcta')
    







