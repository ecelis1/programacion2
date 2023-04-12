import pprint
import os

def limpiarpantalla():
    os.system('cls')

# inicializar matriz de resultados con ceros
resultados = [[0 for j in range(5)] for i in range(5)]

# pedir al usuario los resultados de cada partido
for i in range(5):
    for j in range(i+1, 5):
        while True:
            try:
                print(f'EQUIPO {i+1} vs EQUIPO {j+1}')
                goles_i = int(input(f"Ingrese la cantidad de goles del equipo {i+1} en el partido contra el equipo {j+1}: "))
                goles_j = int(input(f"Ingrese la cantidad de goles del equipo {j+1} en el partido contra el equipo {i+1}: "))
                if goles_i < 0 or goles_j < 0:
                    print("Error: el número de goles debe ser un entero positivo.")
                    continue
                break
            except ValueError:
                print("Error: debe ingresar un número entero positivo.")
        
              
        resultados[i][j] = goles_i
        resultados[j][i] = goles_j
        print()
        print("""TABLA DE RESULTADOS\nP1 P2 P3 P4 P5""")
        for f in range(5):
            for c in range(5):
                print(resultados[f][c],end='  ')
            print()
        print()

limpiarpantalla()
print("""TABLA DE RESULTADOS\nFINAL\nP1 P2 P3 P4 P5""")
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
    
    # imprimir estadísticas del equipo
    print(f"""Equipo {i+1}:
    Triunfos: {triunfos}
    Empates: {empates}
    Derrotas: {derrotas}
    Goles marcados: {goles_marcados}
    Goles recibidos: {goles_recibidos}\n""")