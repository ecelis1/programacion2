from Auto import Auto
from AutoEstereo import AutoEstereo

miestereo = AutoEstereo('Pioneer','MVH-3204')

miauto = Auto('FIESTA','FORD',3200000)

print(miauto.get_auto())
input('PRESIONA ENTER PARA CONTINUAR')



input('AGREGANDO ESTEREO. PRESIONE ENTER PARA CONTINUAR')
miauto.add_AutoEstereo(miestereo)
print(miauto.get_auto())

