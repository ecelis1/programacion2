import csv

def parsear_pib(url):
    try:
        f = open(url)
    except Exception as e:
        print(e)
    else:
        cant=0
        contenido = f.readlines()
        for line in contenido:
            # Obtenemos los años de la primera linea del fichero.
            años = line.split('\t')[1:]
            # Creamos el diccionario principal para guardar los pibs de todos los países.
            dict_pibs = {}
            # Bucle iterativo para recorrer las líneas del fichero.
            for pais in contenido:
                datos_pais = pais.split('\t')
                # Obtenemos el código del país de los dos últimos caracteres del primer campo de la linea.
                codigo_pais = datos_pais.pop(0)[-2:]
                print (codigo_pais)
                input()
                # Construimos un diccionario con los años y el pib del pais.
                dict_pais = {}
                # Bucle iterativo para recorrer los pibs del país.
                for i in range(len(datos_pais)):
                    dict_pais[años[i].strip()] = datos_pais[i].strip()

                    print (dict_pais)
                # Añadimos el diccionario con los pib del país al diccionario principal
                dict_pibs[codigo_pais] = dict_pais
            
            return dict_pibs

def pib(pibs, pais="ES"):
    
    print("Año\tPIB")
    for i, j in pibs[pais].items():
        print(i, '\t', j)

pais = input('Introduce el código de un país: ')
print('Producto Interior Bruto per cápita de', pais)
pib(parsear_pib("sdg_08_10.tsv"),pais)