import random

def generarContrasenia():
    mayus = ['A','B','C','D','F','G']
    minus = ['a','b','c','d','f','g']
    simb = ['!','#','$','%','&']
    num =  ['1','2','3','4','5','6','7','8','9','0']
    
    caracteres = minus + mayus + simb + num

    contrasenia = []

    # el for va a ser hasta 15 caracteres, va a ser una
    #contrasenia de 15 caracteres

    for i in range(15):
        caracterRandom = random.choice(caracteres)
        contrasenia.append(caracterRandom)

    #Con join la paso de lista a string
    contrasenia = "".join(contrasenia)
    #retorno el resutlado
    return contrasenia

def main():
    
    contrasenia = generarContrasenia()

    print('La nueva contrasenia es: ', contrasenia)

if __name__ == '__main__':
    main()