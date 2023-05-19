class Producto:
    def __init__(self,nombre="",precio=0):
        self.__nombre = nombre
        self.__precio = precio
    
    def get_nombre(self):
        return self.__nombre

    def get_precio(self):
        return self.__precio
    
    def __str__(self) -> str:
        return self.__nombre
    
    