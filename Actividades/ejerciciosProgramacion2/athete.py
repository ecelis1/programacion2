class Atleta:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

class Nadador(Atleta):
    def __init__(self, nombre, edad, estilo):
        super().__init__(nombre, edad)
        self.estilo = estilo

class Corredor(Atleta):
    def __init__(self, nombre, edad, distancia):
        super().__init__(nombre, edad)
        self.distancia = distancia

class Ciclista(Atleta):
    def __init__(self, nombre, edad, tipo_bicicleta):
        super().__init__(nombre, edad)
        self.tipo_bicicleta = tipo_bicicleta

class Futbolista(Atleta):
    def __init__(self, nombre, edad, posicion):
        super().__init__(nombre, edad)
        self.posicion = posicion

# Crear un objeto de la clase Nadador
nadador1 = Nadador("Juan", 25, "Libre")
print("Nombre del nadador:", nadador1.nombre)
print("Edad del nadador:", nadador1.edad)
print("Estilo de natación del nadador:", nadador1.estilo)

# Crear un objeto de la clase Corredor
corredor1 = Corredor("Pedro", 30, "Maratón")
print("Nombre del corredor:", corredor1.nombre)
print("Edad del corredor:", corredor1.edad)
print("Distancia de carrera del corredor:", corredor1.distancia)

# Crear un objeto de la clase Ciclista
ciclista1 = Ciclista("Ana", 28, "Montaña")
print("Nombre del ciclista:", ciclista1.nombre)
print("Edad del ciclista:", ciclista1.edad)
print("Tipo de bicicleta del ciclista:", ciclista1.tipo_bicicleta)

# Crear un objeto de la clase Futbolista
futbolista1 = Futbolista("Carlos", 22, "Delantero")
print("Nombre del futbolista:", futbolista1.nombre)
print("Edad del futbolista:", futbolista1.edad)
print("Posición del futbolista:", futbolista1.posicion)
