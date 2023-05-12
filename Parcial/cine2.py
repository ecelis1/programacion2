import os


if os.path('reservasCine.txt') == True:
    print('El Archivo Existe')
else:
    with open('reservasCine.txt','w') as archive:
       archive.seek(0)