import os

# Define el nombre del archivo y su contenido
nombre_archivo = "ejemplo.txt"
contenido_archivo = "Datos Estudiantes Programacion 2:\n"

# Obtiene la ruta completa del escritorio
escritorio = os.path.expanduser("C://Users/ema_c/OneDrive/Escritorio/Programacion/programacion2/Actividades/CreandoArchivoEnPython")

# Combina el nombre del archivo y la ruta del escritorio para crear la ruta completa del archivo
ruta_archivo = os.path.join(escritorio, nombre_archivo)

# Crea y abre el archivo en modo de escritura
with open(ruta_archivo, "w") as archivo:
    # Escribe el contenido del archivo
    archivo.write(contenido_archivo)
    while True:
        
        
        nombre = input("Ingrese nombre del estudiante: ")
        

        if nombre=="SALIR" or nombre=="Salir" or nombre=="salir":
            break
        else:
            print("NOMBRE AGREGADO EXITOSAMENTE")
            nombre = nombre+"\n"
            archivo.write(nombre)
        

# Imprime un mensaje para indicar que el archivo ha sido creado
print(f"El archivo {nombre_archivo} ha sido creado en el escritorio.")
