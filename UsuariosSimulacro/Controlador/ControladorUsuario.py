from Model.Usuarios import Usuario
from Vista.VistaUsuario import VistaUsuario


class ControladorUsuario:
    def __init__(self, vista=VistaUsuario(),modelo=Usuario()):
        self.vista = vista
        self.modelo = modelo

    def UsuariosHabilitados(self):
        habilitados = self.modelo.obtenerHabilitado()
        self.vista.MostrarUsuariosHabilitados(habilitados)
        

    def mostrarUsuarios(self):
        self.vista.MostrarUsuarios(self.modelo.usuarios)

    def verificarPasswordUsuario(self, dni):
            usuario = self.modelo.obtenerUsuarioPorDNI(dni)
            if usuario is not None:
                if usuario.isPassFuerte():
                    self.vista.UsuarioTieneContraseniaFuerte(usuario)
                else:
                    self.vista.UsuarioTieneContraseniaDebil(usuario)
            else:
                self.vista.MostrarMensajeError("No se encontró ningún usuario con el DNI proporcionado.")
    
    def verificarSiPassEsFuerte(self):
        for usuario in self.modelo.usuarios:
            if usuario.isPassFuerte():
                self.vista.UsuarioTieneContraseniaFuerte(usuario)
            else:
                self.vista.UsuarioTieneContraseniaDebil(usuario)

    def verificarRegistro(self):
        apellido = input(self.vista.MostrarMensaje('Ingrese el Apellido: '))
        nombre = input(self.vista.MostrarMensaje('Ingrese el nombre: '))
        dni = input(self.vista.MostrarMensaje('Ingrese el dni: '))
        mail = input(self.vista.MostrarMensaje('Ingrese el mail: '))
        password = input(self.vista.MostrarMensaje('Ingrese el password: '))
        estado = input(self.vista.MostrarMensaje('Ingrese el estado: '))
    
        if self.modelo.RegistrarUsuario(apellido,nombre,dni,mail,password,estado):
            self.vista.MostrarMensajeError(f'El Mail: {mail} Ya existe')
            

        
    