from Model.Usuarios import Usuario
from Vista.VistaUsuario import VistaUsuario

class ControladorUsuario:
    def __init__(self,vista = VistaUsuario(),modelo = Usuario(),aLista=[]):
        self.vista = vista
        self.modelo = modelo
        self.ListaUsuario = aLista

    def registrarUsuarioArchivo:
        with open("Data/archivoUsuarios.txt",r) as archivoUser:
            for line in archivoUser.redline():
                linea = line.split(';')
                #usuario()
                usuario = Usuario(linea[0],linea[1],linea[2],linea[3],linea[4],linea[5])

            ListaUsuario.append(usuario)


    def buscarUsuario(self,dni):
        for item in listaUsuario[]:
            if item.getDNI()==dni:
                return item