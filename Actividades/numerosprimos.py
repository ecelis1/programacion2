def es_primo(numero):
    contador = 0

    #El rango va de 1 a numero mas uno, ya que si no tiene +1 
    # va a ir hasta uno menos
    for i in range (1,numero+1):

        #
        if i==1 or i==numero:
            continue
        
        #Verifica que la division con los numeros hasta
        #el numero ingresado sea igual a 0
        if numero%i==0:
            contador+=1
    
    if contador == 0:
        return True
    else:
        return False

def main():
    numero = int(input('Ingrese un numero: '))
    
    if es_primo(numero):
        print('Es Primo')
    else:
        print('No es primo')

if __name__ == '__main__':
    main()