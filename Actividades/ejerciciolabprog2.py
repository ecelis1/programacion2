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
    if resultadoSumatoria==0:
        input('ERROR, no se puede realizar el promedio, ya que no hay datos cargados.\nDebes cargar las edades.')
    else:
        promedio = sumatoria/len(vector)
        print(f"El promedio es: ",promedio, " años de edad.")
        input('\nPROMEDIO REALIZADO EXITOSAMENTE \nPresione tecla "ENTER" para volver al MENU PRINCIPAL')
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

#SUMATORIA DE EDADES
def sumatoria(vector):
    limpiarPantalla()
    global resultadoSumatoria
    resultadoSumatoria = 0
    for i in range(len(vector)):
        resultadoSumatoria=resultadoSumatoria + vector[i]
    return resultadoSumatoria

#EDADES MAYORES AL PROMEDIO 
def edadesMayoresAlPromedio(v1,promedio):
    limpiarPantalla()
    v2 = []

    for x in range(len(v1)):
        limpiarPantalla()
        if v1[x]>promedio:
            v2.append(v1[x])
        return print('Edades mayores al promedio: ',v2)

#MAYOR EDAD EN ENTERO
def mayorEdadInt(vector):
    limpiarPantalla()
    mayor=0
    for i in range(len(vector)):
        if mayor<vector[i]:
            mayor=vector[i]
    return print('La Mayor edad es: ',mayor)

#ORDENAR EDADES
def orden_edad(vector):
    limpiarPantalla()
    vectOrdenado = []
    vectOrdenado = vector
    vectOrdenado.sort()
    print('\nEl vector ordenado es: ',vectOrdenado)
    input('\nORDENAMIENTO POR FUNCION SORT REALIZADO DE MANERA EXITOSA\nPresione tecla "ENTER" para volver al MENU PRINCIPAL')

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
                if resultadoSumatoria==0:
                    print(f'No se puede hacer la sumatoria de edades porque no hay edades cargadas.\n\n')
                    input('Presione la tecla "ENTER" para volver al MENU PRINCIPAL')
                elif resultadoSumatoria==1:
                    print(f'La sumatoria de edades es: {resultadoSumatoria} año.\n\n')
                    input('Presione la tecla "ENTER" para volver al MENU PRINCIPAL')
                elif resultadoSumatoria>1:
                    print(f'La sumatoria de edades es: {resultadoSumatoria} años.\n\n')
                    input('Presione la tecla "ENTER" para volver al MENU PRINCIPAL')
            case "4":
                promedio(sumatoria(v1),v1)
            case "5":
                edadesMayoresAlPromedio(v1,promedio)
            case "6":
                mayorEdadInt(v1)
            case "7":
                print('falta hacer')
            #mayorEdadStr()
            case "8":
                orden_edad(v1)
            case "9":
                diferenciaEdadPromedio(v1)
            case "10":
                break
            case other:
                print('\nEsa opcion no existe')
                input('Presione la tecla "ENTER" para volver al MENU PRINCIPAL')
    
       

if __name__ == '__main__':
    main()