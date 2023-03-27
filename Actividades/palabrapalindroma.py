def palindromo(palabra):
      
    #se le borran los espacios, porque se va a servir tanto para palabras con o sin espacio
    #Ejemplo: luz azul
    palabra = palabra.replace(' ','')
    
    #Hace toda la palabra minuscula
    palabra = palabra.lower()

    #Revierte la Palabra
    palabraInvertida = palabra[::-1]

    #Preguntamos
    if palabra == palabraInvertida:
        #Va a retornar un valor booleano true
        return True
    
    else:
        #Va a retornar un valor booleano false
        return False

def main():
    palabra = input('Ingrese una palabra: ')
    
    seraPalindromo = palindromo(palabra)

    if seraPalindromo:
        print ('Es palindromo')
    else:
        print ('No es palindromo')

if __name__ == '__main__':
    main()