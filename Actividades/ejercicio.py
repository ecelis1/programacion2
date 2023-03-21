cantEmpleados=int(input('Ingrese la cantidad de Empleados que se encuentra en la planta: '))


registro = [[0 for j in range (6)] for i in range (cantEmpleados)]

#Declaro Variables
supervisor=0
gerente=0
planta=0
may40=0

#Operacion
for i in range (cantEmpleados):
    registro[i][0]=input(f'Ingrese el numero de legajo del empleado {i+1}: ')
    registro[i][1]=input(f'Ingrese el apellido del empleado {i+1}: ')
    registro[i][2]=input(f'Ingrese el nombre del empleado {i+1}: ')
    registro[i][3]=input(f'Ingrese la edad del empleado {i+1}: ')
    
    #Contador mayores a 40 anios
    if int(registro[i][3])>40:
        may40=+1

    registro[i][4]=input(f'Ingrese el sueldo del empleado {i+1}: ')
    registro[i][5]=str.upper(input(f'''Ingrese el puesto del empleado {i+1}
    G - Gerente 
    S - Supervisor 
    P - Planta
    
    Su seleccion: '''))

    #Cant. Segun su puesto    
    #Contador de Supervisores
    if  registro[i][5]=="S":
        supervisor=+1
    
    #Contador de Gerentes
    elif  registro[i][5]=="G":
        gerente=+1
    
    #Contador de empleado de planta
    elif  registro[i][5]=="P":
        planta=+1
    
   
print()
#Salida
print(f"""Cantidad de Empleados por puesto
Gerentes: {gerente}
Supervisores: {supervisor}
Planta: {planta}""")

print()
#Salida Mayores de 40
if may40>0:
    print(f"Cantidad de empleados mayores a 40 anios: {may40}")
    for i in range(cantEmpleados):
        if int(registro[i][3])>40:
            print(f"""El empleado {registro[i][1]},{registro[i][2]} de Legajo: {registro[i][0]}, es mayor a 40 anios""")
else:
    print("No hay empleados que sean mayor a 40 anios")

#Operacion y Salida de empleados que cobran mas de 200k
print("Apellido y Nro Legajo Empleados que cobran mas de 200k")

for i in range(cantEmpleados):
    if float(registro[i][4])>200000:
        print(f"Apellido: {registro[i][1]}, Legajo: {registro[i][0]}")
