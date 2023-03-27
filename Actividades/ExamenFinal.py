import pprint
#DeclaroVariables
resultado=""
#DatosPreguntas
pregunta1 ="""Pregunta 1 
1.
2.
3.
4.
5.
Elije la opcion Correcta: """
pregunta2 ="""Pregunta 2 
1.
2.
3.
4.
5.
Elije la opcion Correcta: """
pregunta3 ="""Pregunta 3 
1.
2.
3.
4.
5.
Elije la opcion Correcta: """
pregunta4 ="""Pregunta 4 
1.
2.
3.
4.
5.
Elije la opcion Correcta: """
pregunta5 ="""Pregunta 5 
1.
2.
3.
4.
5.
Elije la opcion Correcta: """
#Datos de las respuestas correctas
datosRespuestas = [1,2,3,4,5]

#Entrada
#Cargar Legajos
cantLegajosAlumnos = 0

cantLegajosAlumnos = int(input('Ingrese la cantidad de Legajos que desea Ingresar: '))

#CreoMatriz

datosExamenFinal = [["0" for c in range(8)] for f in range(cantLegajosAlumnos)]

#datosExamenFinal[0][0]="Legajo"
#datosExamenFinal[0][1]="P1"
#datosExamenFinal[0][2]="P2"
#datosExamenFinal[0][3]="P3"
#datosExamenFinal[0][4]="P4"
#datosExamenFinal[0][5]="P5"
#datosExamenFinal[0][6]="Nota"
#datosExamenFinal[0][7]="Cond"

for f in range(1,cantLegajosAlumnos):
    print('Alumno ',f+1)
    notaFinal=0
    for c in range(8):
        if c==0:
            datosExamenFinal[f][c]=input('Ingrese su numero de legajo: ')
        if c==1:
            opcion=int(input((print(pregunta1))))
            datosExamenFinal[f][c] = opcion
            if datosExamenFinal[f][c] == datosRespuestas[0]:
                print(f"La Respuesta de la pregunta {c}, es Correcta")
                notaFinal+=20
            else:
                print(f"La Respuesta de la pregunta {c}, es Incorrecta")
        if c==2:
            opcion=int(input((print(pregunta2))))
            datosExamenFinal[f][c] = opcion
            if datosExamenFinal[f][c] == datosRespuestas[1]:
                print(f"La Respuesta de la pregunta {c}, es Correcta")
                notaFinal+=20
            else:
                print(f"La Respuesta de la pregunta {c}, es Incorrecta")
        if c==3:
            opcion=int(input((print(pregunta3))))
            datosExamenFinal[f][c] = opcion
            if datosExamenFinal[f][c] == datosRespuestas[2]:
                print(f"La Respuesta de la pregunta {c}, es Correcta")
                notaFinal+=20
            else:
                print(f"La Respuesta de la pregunta {c}, es Incorrecta")

        if c==4:
            opcion=int(input((print(pregunta4))))
            datosExamenFinal[f][c] = opcion
            if datosExamenFinal[f][c] == datosRespuestas[3]:
                print(f"La Respuesta de la pregunta {c}, es Correcta")
                notaFinal+=20
            else:
                print(f"La Respuesta de la pregunta {c}, es Incorrecta")

        if c==5:
            opcion = int(input((print(pregunta5))))
            datosExamenFinal[f][c] = opcion
            if datosExamenFinal[f][c] == datosRespuestas[4]:
                print(f"La Respuesta de la pregunta {c}, es Correcta")
                notaFinal+=20
            else:
                print(f"La Respuesta de la pregunta {c}, es Incorrecta")
        
        if c==6:
            datosExamenFinal[f][c]=(notaFinal)
                
            if datosExamenFinal[f][c]>=60:
                resultado='APROBADO'
            else:
                resultado='DESAPROBADO'
            datosExamenFinal[f][c]=str(notaFinal)+"%"
        if c==7:
            datosExamenFinal[f][c]=resultado

pprint.pprint(datosExamenFinal)
