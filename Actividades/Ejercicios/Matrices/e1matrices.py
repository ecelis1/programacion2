#Una agencia de venta de vehículos automóviles distribuye quince modelos diferentes y tiene en su plantilla diez vendedores. Se desea un programa que escriba un informe mensual de las ventas por vendedor y modelos, así como el número de automóviles vendido por cada vendedor y el número total de cada modelo vendido por todos los vendedores. Asimismo para entregar el premio al mejor vendedor, necesita saber cual es el vendedor que más coches ha vendido.

def imprimirMatriz(matriz,i,j):
    for i in range(i):
        for j in range(j):
            print(matriz[i][j], end=' ')


#def cargarMatriz():

import pprint

vendedores = 10
modelo = 15

registroMensual = [[0 for columnas in range(15)] for filas in range(10)]


while True:
    vendedores = int(input('Ingrese el num del Vendedor (1 al 10), ingrese 0 para salir del programa.'))

    if vendedores == 0:
        break

    modelo = int(input('Ingrese el modelo de la unidad vendida (1 al 15): '))

    cantidades = int(input('Ingrese la cantidad vendida de este modelo: '))

    registroMensual[vendedores-1][modelo-1] += cantidades


    print('INFORME MENSUAL')

    for i in range(vendedores):
        totalVendido = 0
        print(f'Vendedor {vendedores+1}: ')

        for j in range(modelo):
            cantidades = registroMensual[i][j]
            totalVendido += cantidades

            if cantidades > 0:
                print(f'Modelo {modelo+1}: {cantidades}')
    
    print(f'Total de ventas del mes: {totalVendido}')

