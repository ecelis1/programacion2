import os

d = {}

file = open ('Actividades\Laboratorio2\EjerciciosRandom\seleccionesyjugadores.txt','r')
file.readline()

for linea in file:
    seleccion,jugadores = linea.strip().split(',')
    jugadores = jugadores.split('-')

    #clave -> seleccion
    #la clave se puede repetir en el archivo?
    #no se puede repetir en el archivo, porque esta argentina, venezuela, entre otros, entonces asignamos

    d[seleccion]=jugadores

file.close()

print(d)