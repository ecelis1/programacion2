import pprint
import os
equipos = [[0 for j in range(10)] for i in range(5)]
equipos[0][0]="P1"
equipos[0][1]="P2"
equipos[0][2]="P3"
equipos[0][3]="P4"
equipos[0][4]="P5"
equipos[0][5]="PG"
equipos[0][6]="PE"
equipos[0][7]="PP"
equipos[0][8]="GH"
equipos[0][9]="GR"



pprint.pprint(equipos)

for i in range(1,5):
    for j in range(5):
        
        if i==j:
            equipos[i][j]=0;
        else:
            resultado = int(input(f"Ingrese el resultado del partido entre el Equipo {i+1} y Equipo {j+1}: "))
            equipos[i][j] = resultado

            #Acumulo los goles hechos
            equipos[i][8] = equipos[i][8] + resultado


pprint.pprint(equipos)
input()
os.system("cls")

for i in range(5):
    golesrecibidos=0
    for j in range(5):
        
        if i==j:
            equipos[i][j]=0;
        else:
            #Comparacion de resultados, y asignacion de Partidos Ganados, Empatados y Perdidos
            if equipos[i][j]>equipos[i+1][j-1]:
                print(f"Este partido lo gano el equipo{i+1} al equipo {j+1}")
                equipos[i][5]+=1
            elif equipos[i][j]==equipos[i+1][j-1]:
                print(f"Este partido se empato, el el equipo{i+1} hizo {equipos[i][j]} goles y equipo {j+1} hizo {equipos[i+1][j-1]}")
                equipos[i][6]+=1

                #Goles Recibidos
                golesrecibidos = golesrecibidos + equipos[i+1][j-1]
                equipos[i][9]= golesrecibidos

            elif equipos[i][j]<equipos[i+1][j-1]:
                equipos[i][7]+=1

                #Goles Recibidos
                golesrecibidos = golesrecibidos + equipos[i+1][j-1]
                equipos[i][9] = golesrecibidos

            

pprint.pprint(equipos)