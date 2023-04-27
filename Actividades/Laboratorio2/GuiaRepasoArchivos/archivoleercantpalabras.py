import os

def contarPalabras():
    # Abrir el archivo en modo lectura
    with open('texto.txt', "r") as archivo:
        # Leer el contenido del archivo
        contenido = archivo.read()
        
        #split sirve para dividir el contenido en palabras, asumiendo que las palabras estan separadas por espacios en blanco
        print(contenido.split())

        # Contar la cantidad de palabras en el contenido
        cantPalabras = len(contenido.split())

    # Imprimir el resultado
    print(f"El archivo '{'texto.txt'}' contiene {cantPalabras} palabras.")

def main():
    contarPalabras()

if __name__== '__main__':
    main()