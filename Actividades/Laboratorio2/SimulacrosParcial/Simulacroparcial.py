import os
def compararPatente(patente):
        try:
            # Intentar abrir el archivo en modo lectura
            with open('FicheroPeaje.txt', 'r') as archivo_txt:
                # Aquí puedes realizar la comparación con los datos del archivo
                # y continuar con la ejecución del programa
                print("Archivo existente. Realizando comparación...")

                for linea in archivo_txt:
                    datos = linea.strip().split(',')  # Separar los datos de la línea por coma
                    if datos[0] == patente:
                        print(f"La patente {patente} se encuentra en el archivo.")
                        return True
                    else:
                        return False
                # Resto del código para comparar datos del archivo
        except FileNotFoundError:
            # Si el archivo no existe, crearlo y continuar con la ejecución del programa
            print(f"El archivo '{'FicheroPeaje.txt'}' no existe. Creando archivo...")
            with open('FicheroPeaje.txt', 'w') as archivo:
                # Escribir datos iniciales en el archivo si es necesario
                pass  # Puedes dejarlo vacío si no necesitas escribir datos iniciales
            print("Archivo creado. Continuando con la ejecución del programa...")
            # Resto del código para continuar con la ejecución del programa

    
            
                


def registrarPaso():
  
    precio=0
    menuCateg='1- Motos\n2- Autos\n3- Autos y Acoplados\n4- Gran Porte (Colectivos, Omnibus,etc.)\nIngrese su Seleccion: '
    registroAuto = []

    while True: 
        patente=input('Ingrese la patente del vehiculo: ')
        
        if compararPatente(patente):
            print('La Patente ya Existe. por favor ingrese otra.')
            continue

        registroAuto.append(patente)


        fecha=input('Ingrese la fecha: ')
        registroAuto.append(fecha)
        hora=input('Ingrese la hora: ')
        registroAuto.append(hora)
        categ=int(input(f'Ingrese a que categoria pertenece\n{menuCateg}: '))
        match categ:
            case 1:
                cantAuto=1
                precio=100
                
                print(f'Ha seleccionado Motocicletas, el importe a pagar es de ${precio}')
                registroAuto.append(str(categ))
                registroAuto.append(str(precio))
            case 2:
                cantAuto=1
                precio=150
            
                print(f'Ha seleccionado Automoviles, el importe a pagar es de ${precio}')
                registroAuto.append(str(categ))
                registroAuto.append(str(precio))
            case 3:
                cantAuto=1
                precio=300
                
                print(f'Ha seleccionado Camionetas, el importe a pagar es de ${precio}')
                registroAuto.append(str(categ))
                registroAuto.append(str(precio))
            case 4:
                cantAuto=1
                precio=500
                
                print(f'Ha seleccionado Gran Porte, el importe a pagar es de ${precio}')
                registroAuto.append(str(categ))
                registroAuto.append(str(precio))
    
        with open('FicheroPeaje.txt', 'a') as file:
            file.write(','.join(registroAuto)+'\n')
            

        print('SE HA REGISTRADO EL VEHICULO\n')

        return()

def registrarCierre():
    cantAuto = 0
    acum = 0
    # Lee el archivo de texto y busca la patente en los datos
    with open('FicheroPeaje.txt', 'r') as archivo_txt:
        for linea in archivo_txt:
            datos = linea.strip().split(',')  # Separar los datos de la línea por coma
            if datos[4]:
                acum+=int(datos[4])
            
            cantAuto+=1

    print(f"Se cerro el registro del peaje, no se pueden registrar mas vehiculos\nEl total de vehiculos que pasaron fueron: {cantAuto}\nLo que se recaudo fue: {acum}")

def menu():
    
    menu='1- Registrar Pases de Vehiculos\n2- Cerrar y Mostrar Registro\n3- Salir\nIngrese su seleccion: '
    return menu

def main():
    
    while True:
        seleccion=int(input(menu()))
        match seleccion:
            case 1:
                registrarPaso()
            case 2:
                registrarCierre()
                
            case 3:
                print('Usted salio del Programa')
                break

if __name__ == '__main__':
    main()