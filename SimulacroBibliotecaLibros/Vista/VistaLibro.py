# Consultar que libros pueden prestarse
# registrar el prestamo de un libro 
# registrar la devolucion de un libro
class VistaLibro:
    def menu(self):
        print("1. Consultar libros")
        print("2. Registrar prestamo")
        print("3. Registrar devolucion")
        print("4. Salir")
    
    def seleccion(self):
        return int(input("Ingrese una opción: "))
    
    def mostrar_resultado(self,x):
        return x
    
    def seleccionLibro(self):
        return str(input("Ingrese el nombre del libro que quiere pedir: "))
    
    def disp(self):
        print("Tenemos disponibles: ")
    
    def libro_prestado(self, x):
        print(f"El libro {x} ha sido prestado")

    def despedida(self):
        print("Gracias por usar nuestros servicios.")
    
    def seleccionLibroDevolver(self):
        return str(input("Ingrese el nombre del libro a devolver: "))
    
    def devuelto(self, x):
        print(f"El libro {x} ha sido devuelto.")