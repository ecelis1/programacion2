import pprint
import os


#FUNCION LIMPIAR PANTALLA
def limpiarpantalla():
    os.system('cls')

#INICIALIZO LA MATRIZ CON 0s
resultados = [[0 for j in range(5)] for i in range(5)]

#INGRESO LOS GOLES TANTOS A FAVOR COMO EN CONTRA
for i in range(5):
    for j in range(i+1, 5):
        while True:
            try:
                print(f'EQUIPO {i+1} vs EQUIPO {j+1}')
                goles_equipoa = int(input(f"Ingrese la cantidad de goles del equipo {i+1} en el partido contra el equipo {j+1}: "))
                goles_equipob = int(input(f"Ingrese la cantidad de goles del equipo {j+1} en el partido contra el equipo {i+1}: "))
                if goles_equipoa < 0 or goles_equipob < 0:
                    print("Error: el número de goles debe ser un entero positivo.")
                    continue
                break
            except ValueError:
                print("Error: debe ingresar un número entero positivo.")
        
        #ASIGNO LOS GOLES A LA MATRIZ RESULTADOS  
        resultados[i][j] = goles_equipoa
        resultados[j][i] = goles_equipob

limpiarpantalla()
#IMPRIMO TABLA RESULTADO FINAL
print("\nTABLA DE RESULTADOS\nFINAL\nP1 P2 P3 P4 P5")
for i in range(5):
    for j in range(5):
        print(resultados[i][j],end='  ')
    print()
print()

#ESTADISTICAS DE CADA EQUIPO
for i in range(5):
    triunfos = 0
    empates = 0
    derrotas = 0
    goles_marcados = 0
    goles_recibidos = 0
    for j in range(5):
        if i == j:
            continue
        if resultados[i][j] > resultados[j][i]:
            triunfos += 1
        elif resultados[i][j] == resultados[j][i]:
            empates += 1
        else:
            derrotas += 1
        goles_marcados += resultados[i][j]
        goles_recibidos += resultados[j][i]
    
    #MUESTRO POR PANTALLA LA ESTADISTICAS DE CADA EQUIPO
    print(f"""Equipo {i+1}:\nTriunfos: {triunfos}\nEmpates: {empates}\nDerrotas: {derrotas}\nGoles marcados: {goles_marcados}\nGoles recibidos: {goles_recibidos}\n""")