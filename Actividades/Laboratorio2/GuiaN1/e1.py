#Escribir una función que reciba una muestra de números en una lista y devuelva su media / ajustar el ancho alt+z


def media(lista):
    suma = sum(lista)
    cantElementos = len(lista)

    media = suma / cantElementos

    return media


lista = [3,4,2,1,24,7,9,20]

print (f'La media es: {media(lista)}')


