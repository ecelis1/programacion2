import os

#servicio;importe_enero,importe_febrero...importe_diciembre

#def registrarPago():

menuServicios = '1-AGUA\n2-GAS\n3-ELECTRICIDAD\n'

# crear el diccionario de servicios con los importes de enero a diciembre
servicios = {
    "electricidad": {
        "enero": 0,
        "febrero": 0,
        "marzo": 0,
        "abril": 0,
        "mayo": 0,
        "junio": 0,
        "julio": 0,
        "agosto": 0,
        "septiembre": 0,
        "octubre": 0,
        "noviembre": 0,
        "diciembre": 0,
    },
    "agua": {
        "enero": 0,
        "febrero": 0,
        "marzo": 0,
        "abril": 0,
        "mayo": 0,
        "junio": 0,
        "julio": 0,
        "agosto": 0,
        "septiembre": 0,
        "octubre": 0,
        "noviembre": 0,
        "diciembre": 0,
    },
    "gas": {
        "enero": 0,
        "febrero": 0,
        "marzo": 0,
        "abril": 0,
        "mayo": 0,
        "junio": 0,
        "julio": 0,
        "agosto": 0,
        "septiembre": 0,
        "octubre": 0,
        "noviembre": 0,
        "diciembre": 0,
    }
}

def registrarPago(servicio):
    #Registrar Pago de Servicio
    while True:
        servicio = input('Ingrese el nombre del servicio(o "fin" para cerrar el programa: ')

        if servicio=='fin':
            break

        mes = str.lower(input('Ingrese el mes que pago: '))
        
        importe = float(input(f'Ingrrese el importe para el mes de {mes}: '))     
        
        print(servicios)
        escribirloenunArchivo(servicios)

    return servicios

def sumarMes(servicios):
    #Sumar el importe de todo un mes de todos los servicios

    totalMes = 0

    mes = str.lower(input('Ingrese el mes que desea sumar: '))



    for servicio in servicios:
        totalMes+=servicios[servicio][mes]

    print(f'El total de los importes de {mes} es: {totalMes}')

def sumarServicioAnual(servicios):
    #Sumar el importe de todo un mes de todos los servicios

    totalServicioAnual = 0

    servicioX = str.lower(input('Ingrese el servicio que desea ver el gasto hasta el momento: '))



    for mes in servicios[servicioX]:
        totalServicioAnual += servicios[servicioX][mes]

    print(f'El total de los importes anual de {servicioX} es: {totalServicioAnual}')

def gastoTotalServicios(servicios):
    total = 0
    for servicio in servicios:
        for mes in servicios[servicio]:
            total += servicios[servicio][mes]

    # Mostrar el total de los importes de todos los servicios y meses
    print(f"El total de los importes de todos los servicios y meses es: {total}")

def escribirloenunArchivo(servicios):
    with open("Actividades\Laboratorio2\SimulacrosParcial\servicios.txt", "w") as archivo:
        # Escribir encabezado de tabla
        archivo.write("Servicio\tenero\tfebrero\tmarzo\tabril\tmayo\tjunio\tjulio\tagosto\tseptiembre\toctubre\tnoviembre\tdiciembre\n")
        # Iterar sobre el diccionario y escribir los datos en formato de tabla
       
        # recorremos cada servicio en el diccionario
        
        for servicio, meses in servicios.items():
            # agregamos el nombre del servicio como encabezado de la tabla
            archivo.write(servicio + ";")
            # recorremos cada mes y su importe
            importes = []
            for mes,importe in meses.items():
                # agregamos una fila a la lista con los valores del mes y el importe
                importes.append(str(importe))
                
            # escribimos la tabla en el archivo
            archivo.write(','.join(importes))
            archivo.write('\n')
    

    with open("Actividades\Laboratorio2\SimulacrosParcial\servicios.txt", "r") as archivo:
        archivo = archivo.read()
        print()

    
    


def main():
    while True:
        seleccion = int(input('QUE DESEA HACER?\n1.CARGAR UNA BOLETA\n2.RESUMEN DE GASTO DE UN SERVICIO\n3.GASTO DE UN MES DE TODOS LOS SERVICIOS\n4.GASTO ANUAL DE TODOS LOS SERVICIOS\n5.SALIR\nIngrese su eleccion: '))

        match seleccion:
            case 1:
                registrarPago(servicios)
            case 2:
                sumarServicioAnual(servicios)
            case 3:
                sumarMes(servicios)
            case 4:
                gastoTotalServicios(servicios)
            
            case 6:
                escribirloenunArchivo(servicios)
            case 5:
                break

if __name__ == '__main__':
    main()

