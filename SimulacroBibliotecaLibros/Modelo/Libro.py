class Libro:
    def __init__(self, nombre="", autor="", cantDisponibles=0, cantPrestados=0):
        self.nombre = nombre
        self.autor = autor
        self.cantDisponibles = cantDisponibles
        self.cantPrestados = cantPrestados
    
    def __str__(self):
        return f"{self.nombre}, - Autor: {self.autor} - Cantidad disponibles: {self.cantDisponibles} - Cantidad prestados: {self.cantPrestados}"
    
    def get_nombre(self):
        return self.nombre
    def set_nombre(self, nombre):  
        self.nombre = nombre
    def get_autor(self):
        return self.autor
    def set_autor(self, autor):
        self.autor = autor
    def get_cantDisp(self):
        return self.cantDisponibles
    def set_cantDisp(self, cantDisp):
        self.cantDisponibles += cantDisp
    def get_cantPrest(self):
        return self.cantPrestados
    def set_cantPrest(self, cantPrest):
        self.cantPrestados += cantPrest
    