#Escribir una función que reciba una muestra de números en una lista y devuelva otra lista con sus cuadrados.

def cuadrados(lista):
    cuadrados=[]

    for i in range(len(lista)):
        cuadrados.append(lista[i]** 2)
    return cuadrados


lista = [3,4,2,1,24,7,9,20]
print(f'La lista de numeros enteros es: {lista}')
print (f'Los cuadrados de los numeros son: {cuadrados(lista)}')