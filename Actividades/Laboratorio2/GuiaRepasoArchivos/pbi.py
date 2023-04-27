import csv

# Nombre del archivo TSV con la información del PIB per cápita
nombre_archivo = "sdg_08_10.tsv"

# Preguntar al usuario por el código de país
codigo_pais = str.upper(input("Ingresa el código de país de la UE para obtener el PIB per cápita: "))



# Abrir el archivo TSV en modo lectura
with open(nombre_archivo, 'rt') as archivo:
    # Crear un objeto de lector TSV
    lector_tsv = csv.reader(archivo, delimiter='\t')

    # Bandera para indicar si se encontró el código del país
    encontrado = False

    # Iterar sobre las filas del archivo
    for fila in lector_tsv:
        # Obtener los datos de la fila
        codigo_pais_completo = fila[0]
        
        print(codigo_pais_completo.split(',')[2])
        input()
        # Extraer el código de país de la primera columna
        codigo_pais_extraido = codigo_pais_completo.split(',')[2]
        
        
        # Verificar si el código de país extraído coincide con el código proporcionado por el usuario
        if codigo_pais_extraido == codigo_pais:
            # Imprimir toda la fila
            print('\t'.join(fila))
            encontrado = True

    #si no lo encontro
    if not encontrado:
        print("No se encontró información para el código de país proporcionado.")



  