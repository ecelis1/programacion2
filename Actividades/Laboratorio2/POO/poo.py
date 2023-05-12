class Persona:
    

    def __init__(self,nombre=None,edad=0):
        self.__nombre = nombre
        self.__edad = edad

    def get_nombre(self):
        return self.__nombre
