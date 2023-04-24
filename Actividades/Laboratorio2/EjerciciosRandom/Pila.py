import os

def limpiarPantalla():
    os.system('cls')

def pilaVacia(pila,tope):
    if tope==0:
        band=True
    else:
        band=False
    
    return band

def pilaLlena(pila,tope,max):
    if tope==max:
        band=True
    else:
        band=False
    
    return band

def poner(pila,tope,max,dato):
    band = pilaLlena(pila,tope,max)
    if band==True:
        print('Desbordamiento - Pila Llena')
    else:
        while True:
            try:
                dato = int(input("Ingrese un número entero: "))
                break
            except ValueError:
                print("Error: El valor ingresado no es un número entero.")
            except:
                print("Ocurrió un error inesperado.")
            if dato == "":
                print("Error: No se puede ingresar un valor vacío.")
                
        pila.append(dato)
        tope+=1

    return tope

def quitar(pila,tope,max):
    band = pilaVacia(pila,tope)
    if band==True:
        print('Subdesbordamiento - PILA VACIA')
    else:
        tope-=1
        pila[tope]=0

    
    return tope

def mostrarElementos(pila):
    if len(pila)==0:
        print('No hay elementos en la pila')
    else:
        print('Elementos Actuales de la pila')
    
        for i in range(len(pila),0,-1):
            print(f'Posicion {i}: {pila[i-1]}')
3
menu="""
1 = Saber si la pila esta vacia
2 = Saber si la pila esta llena
3 = Colocar un elemento a la pila
4 = Quitar un elemento a la pila
5 = Mostrar los elementos actuales de la pila
6 = Salir

INGRESE SU SELECCION: """       



def main():
    #Declaracion de variables
    pila,max,tope,seleccion,dato = int,int,int,int,int
    band = bool 
    
    #Inicializaciones
    band = False 
    max = 4
    dato = 0
    tope = 0
    pila = [max]*0

    while True:
        while True:

            try:
                seleccion = int(input(menu))
                break
            except ValueError:
                input ('Ingrese un valor entero, por favor - PRESIONA TECLA ENTER PARA CONTINUAR')

            
        match seleccion:
            case 1: 
                band = pilaVacia(pila,tope)
                if band == True:
                    print('La pila esta vacia')
                    input('PRESIONA TECLA ENTER PARA CONTINUAR')
                    limpiarPantalla()
                else:
                    print('La pila no esta vacia')
                    input('PRESIONA TECLA ENTER PARA CONTINUAR')
                    limpiarPantalla()
                
                

            case 2:
                band = pilaLlena(pila,tope,max);

                if band == True:
                    print ('La Pila esta LLENA')
                    input('PRESIONA TECLA ENTER PARA CONTINUAR')
                    limpiarPantalla()
                else:
                    print('La pila NO ESTA LLENA')
                    input('PRESIONA TECLA ENTER PARA CONTINUAR')
                    limpiarPantalla()
            case 3:
                tope = poner(pila,tope,max,dato)
                limpiarPantalla()
                input('ELEMENTO AGREGADO CON EXITO\n\nPRESIONA TECLA ENTER PARA CONTINUAR')
                limpiarPantalla
            
            case 4:

                tope = quitar(pila,tope,max)
                limpiarPantalla()
                input('ELEMENTO ELIMINADO CON EXITO\n\nPRESIONA TECLA ENTER PARA CONTINUAR')
                limpiarPantalla()
            
            case 5:
                mostrarElementos(pila)
                input('PRESIONA TECLA ENTER PARA VOLVER AL MENU')
                limpiarPantalla()
            
            case 6:
                print('Hasta Luego')
                break
            
            case other:
                print ('Ingrese una opcion correcta') 

if __name__ == '__main__':
    main()