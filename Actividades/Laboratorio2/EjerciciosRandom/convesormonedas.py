def convertir(valor_dolar,pais):
    cantidadMoneda=float(input(f'Ingrese cantidad de {pais}: '))

    dolares = cantidadMoneda / valor_dolar
    dolares = round(dolares,2)
          
    print(f'Tienes ${dolares}USD')

def main():
    while True:
        menu = """
        1 - Soles Peruanos a Dolares
        2 - Pesos Mexicanos a Dolares
        3 - Pesos Colombianos a Dolares
        4 - Salir
        Ingrese una opcion: """
        
        opcion = input(menu)


        match opcion:
            case "1":
                convertir(3.61,'Soles Peruanos')
            case "2":
                convertir(20.01,'Pesos Mexicanos')
            case "3":
                convertir(3471.27,'Pesos Colombianos')
            case "4":
                print('Usted ha salido del convertidor')
                break
            case other:
                print('Esa opcion no existe')

if __name__ == '__main__':
    main()