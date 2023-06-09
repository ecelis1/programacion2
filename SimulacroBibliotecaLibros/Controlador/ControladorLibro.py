from Modelo.Libro import Libro
from Vista.VistaLibro import VistaLibro

class ControladorLibro:
    def __init__(self, modelo=Libro(), vista=VistaLibro()):
        self.modelo = modelo
        self.vista = vista
        self.libros = []
    
    def mostrar_menu(self):
        self.vista.menu()
        try:
            x = self.vista.seleccion()
        except ValueError:
            print("Opcion no valida")
        self.controlador_menu(x)
    
    def controlador_menu(self,x):
        self.abrir_archivo()
        if x == 1:
            self.mostrar_libros()
        elif x == 2:
            self.prestamo()
        elif x == 3:
            self.devolucion()
        elif x == 4:
            self.vista.despedida()
            exit()
    
    def abrir_archivo(self):
        try:
            with open("libros.txt", "r") as file:
                for line in file:
                    datos = line.strip().split(",")
                    libro = Libro(datos[0].strip('\"'), datos[1].strip('\"'), int(datos[2]), int(datos[3]))
                    self.libros.append(libro)
        except Exception:
            print("No se pudo abrir el archivo")
    
    def mostrar_libros(self):
        self.vista.disp()
        for libro in self.libros:
            if libro.cantDisponibles > 0:
                print(f"Nombre: {libro.nombre} - Cantidad disponible: {libro.cantDisponibles} \n")
    
    def prestamo(self):
        self.mostrar_libros()
        x = self.vista.seleccionLibro()
        for libro in self.libros:
            if x.lower() == libro.nombre.lower():
                if libro.cantDisponibles > 0:
                    libro.cantDisponibles -= 1
                    libro.cantPrestados += 1
                    z = libro.get_nombre()
                    self.vista.libro_prestado(z)
        else:
                print("Ese nombre no corresponde a ningún libro.")
        self.guardar_datos()
        
    
    def devolucion(self):
        x = self.vista.seleccionLibroDevolver()
        for libro in self.libros:
            if x.lower() == libro.nombre.lower():
                if libro.cantDisponibles > 0:
                    libro.cantDisponibles += 1
                    libro.cantPrestados -= 1
                    z = libro.get_nombre()
                    self.vista.devuelto(z)
        else:
            print("Ese nombre no corresponde a ningún libro.")
        self.guardar_datos()
    
    def guardar_datos(self):
        with open("libros.txt", "w") as file:
            for libro in self.libros:
                nombre = libro.nombre
                autor = libro.autor
                cantDisponibles = libro.cantDisponibles
                cantPrestados = libro.cantPrestados
                x = [f"{nombre},{autor},{str(cantDisponibles)},{str(cantPrestados)}\n"]
                file.writelines(x)