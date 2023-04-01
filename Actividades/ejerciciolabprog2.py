import os
#limpiar pantalla
def limpiarPantalla():
    os.system ("cls") 
    
#Mostrar Menu
def mostrarMenu():
    global opcion
    opcion=str(input("""MENU PRINCIPAL

    1 - CARGAR EDADES
    2 - MOSTRAR LAS EDADES CARGADAS
    3 - CALCULAR SUMATORIA DE EDADES
    4 - CALCULAR PROMEDIO DE LAS EDADES CARGADAS
    5 - MOSTRAR EDADES MAYORES AL PROMEDIO
    6 - MOSTRAR EDAD MAYOR EN NUMERO
    7 - MOSTRAR EDAD MAYOR EN LETRAS
    8 - ORDENAR LAS EDADES
    9 - MOSTRAR DIFERENCIA ENTRE CADA EDAD Y LOS PROMEDIOS
    10 - SALIR
    
    INGRESE SU ELECCION (1-9): """))
    return(opcion)

#Cargar Vector

def cargarVector():
    limpiarPantalla()
    l=int(input('Ingrese la cantidad de edades que desea ingresar: '))
    v=[]*l
    for i in range(l):
        edad=int(input(f'Ingrese la edad {i+1}: '))
        while edad<=0:
            print('\nERROR - Por favor ingrese una edad correcta, mayor a 0\n')
            input('Presione tecla "ENTER" para continuar')
            edad=int(input(f'Ingrese la edad {i+1}: '))
        v.append(edad)
    
    input('\nEDADES CARGADAS EXITOSAMENTE \nPresione tecla "ENTER" para volver al MENU PRINCIPAL')
    limpiarPantalla()
    return v

#mostrar vector
def mostrarVector(v):
    limpiarPantalla()
    if len(v)==0:
        input('\nEl vector no posee edades cargadas\n\nPresione tecla "ENTER" para volver al MENU PRINCIPAL y poder cargar edades')
        limpiarPantalla()
    else:
        input(f'\nLas edades son:\n\n{v}\n\nPresione tecla "ENTER" para volver al MENU PRINCIPAL')
#Devuelve el promedio
def promedio(sumatoria,vector):
    limpiarPantalla()
    if sumatoria==0:
        input('ERROR, no se puede realizar el promedio, ya que no hay datos cargados.\nDebes cargar las edades.')
    else:
        promedio = sumatoria/len(vector)
        return promedio

#Diferencia de edad promedio
def diferenciaEdadPromedio(vector):
    limpiarPantalla()
    promedio = promedio(vector)
    diferencia = 0
    print('''Diferencia entre edades y promedio
    
    Edad,Promedio,Diferencia''')
    for i in range(len(vector)):
        diferencia = vector[i]-promedio
        print(vector[i],promedio,diferencia)

def sumatoria(vector):
    limpiarPantalla()
    resultado = 0
    for i in range(len(vector)):
        resultado=resultado + vector[i]
        
    if resultado==0:
        print(f'No se puede hacer la sumatoria de edades porque no hay edades cargadas.\n\n')
        input('Presione la tecla "ENTER" para volver al MENU PRINCIPAL')
    elif resultado>0:
        print(f'La sumatoria de edades es: {resultado}.\n\n')
        input('Presione la tecla "ENTER" para volver al MENU PRINCIPAL')
    return resultado
    
def edadesMayoresAlPromedio(v1,promedio):
    limpiarPantalla()
    v2 = []

    for x in range(len(v1)):
        limpiarPantalla()
        if v1[x]>promedio:
            v2.append(v1[x])
        return print('Edades mayores al promedio: ',v2)
    
def mayorEdadInt(vector):
    limpiarPantalla()
    mayor=0
    for i in range(len(vector)):
        if mayor<vector[i]:
            mayor=vector[i]
    return print('La Mayor edad es: ',mayor)

def orden_edad(vector):
    limpiarPantalla()
    vectOrdenado = []
    vectOrdenado = vector
    vectOrdenado.sort()
    print('El vector ordenado es: ',vectOrdenado)


def main():
   v1 = []
   while True:
    varOp = mostrarMenu()
    
    match opcion:
            case "1":
                v1= cargarVector()
                continue
            case "2":
                mostrarVector(v1)
            case "3":
                sumatoria(v1)
            case "4":
                promedio(sumatoria(v1),v1)
            case "5":
                edadesMayoresAlPromedio(v1,promedio)
            case "6":
                mayorEdadInt()
            case "7":
                print('falta hacer')
            #mayorEdadStr()
            case "8":
                orden_edad()
            case "9":
                diferenciaEdadPromedio()
            case "10":
                break
            case other:
                print('\nEsa opcion no existe')
                input('Presione la tecla "ENTER" para volver al MENU PRINCIPAL')
    
       

if __name__ == '__main__':
    main()