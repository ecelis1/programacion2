nColumnas = 2
nFilas = 3


listaDatos = [[0 for c in range(nColumnas)] for f in range(nFilas)]

print(listaDatos)

for f in range(nFilas):
    listaDatos[f][0]=str(input('Ingrese el Apellido: '))
    listaDatos[f][1]=int(input('Ingrese la edad: '))


print(listaDatos)

for f in range(nFilas):
    print(listaDatos[f][0],',',listaDatos[f][1])