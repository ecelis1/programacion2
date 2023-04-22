import os

def registrarPaso(cantAuto):
    cantAuto=0
    acum=0
    precio=0
    menuCateg='1- Motos\n2- Autos\n3- Autos y Acoplados\n4- Gran Porte (Colectivos, Omnibus,etc.)\nIngrese su Seleccion: '
    registroAuto=[]
    patente=input('Ingrese la patente del vehiculo: ')
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
            acum=precio
            print(f'Ha seleccionado Motocicletas, el importe a pagar es de ${precio}')
            registroAuto.append(str(categ))
            registroAuto.append(str(precio))
        case 2:
            cantAuto=1
            precio=150
            acum=precio
            print(f'Ha seleccionado Automoviles, el importe a pagar es de ${precio}')
            registroAuto.append(categ)
            registroAuto.append(precio)
        case 3:
            cantAuto=1
            precio=300
            acum=precio
            print(f'Ha seleccionado Camionetas, el importe a pagar es de ${precio}')
            registroAuto.append(categ)
            registroAuto.append(str(precio))
        case 4:
            cantAuto=1
            precio=500
            acum=precio
            print(f'Ha seleccionado Gran Porte, el importe a pagar es de ${precio}')
            registroAuto.append(categ)
            registroAuto.append(precio)
   
    with open('FicheroPeaje.txt', 'a') as file:
        file.write(','.join(registroAuto))

    print('SE HA REGISTRADO EL VEHICULO\n')

    return(acum,cantAuto)

def registrarCierre(acum,cantAuto):
    archivo=open("FicheroPeaje.txt","r")
    
    print(f"Se cerro el registro del peaje, no se pueden registrar mas vehiculos\nEstos fueron los vehiculos que pasaron\n{archivo.readlines()}\nEl total de vehiculos que pasaron fueron: {cantAuto}\nLo que se recaudo fue: {acum}")
    archivo.close()

def menu():
    
    menu='1- Registrar Pases de Vehiculos\n2- Cerrar y Mostrar Registro\n3- Salir\nIngrese su seleccion: '
    return menu

def main():
    acum=0
    cantAuto=0
    recaudado=0
    cantVehiculos=0
    while True:
        seleccion=int(input(menu()))
        match seleccion:
            case 1:
                registrarPaso(cantAuto)
            case 2:
                registrarCierre(recaudado,cantVehiculos)
                
            case 3:
                print('Usted salio del Programa')
                break

if __name__ == '__main__':
    main()