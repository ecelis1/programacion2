import random

def jugar(vidas):
    numeroRandom = random.randint(1,100)
    numElegido=None

    while numeroRandom != numElegido:
        numElegido = int(input('Ingresa el Numero entre 1 y 100: '))

        if numeroRandom<numElegido:
            print('Elige un numero mas pequenio')
            vidas -= 1
        elif numeroRandom>numElegido:
            print('Elige un numero mas grande')
            vidas -= 1
        
        if vidas == 0:
            print('GAME OVER - Te quedaste sin vidas')
            break

        print(f'Te quedan {vidas} vidas')
    
    if numElegido==numeroRandom:
        print('WIN - GANASTE EL JUEGO')

def main():
    while True:
        menu = """
        BIENVENIDO A ADIVINA EL NUMERO
        
        ELIGE LA DIFICULTAD DEL JUEGO
        1 - Facil
        2 - Medio
        3 - Dificil
        4 - Salir
        Ingrese una opcion: """
        
        opcion = input(menu)


        match opcion:
            case "1":
                jugar(20)
            case "2":
                jugar(10)
            case "3":
                jugar(5)
            case "4":
                print('Usted ha salido del juego')
                break
            case other:
                print('Esa opcion no existe')

if __name__ == '__main__':
    main()