class VistaUsuario:
    def MostrarMenu(self):
        print("1 - Mostrar Usuarios Habilitados\n2 - Comprobar si las contrasenias que tienen los usuarios son fuertes\n3 - Buscar usuario por DNI, y comprobar su contrasenia\n4 - Registrar Nuevos Usuarios\n5 - Salir\nSeleccione una opción: ")
    
    def MostrarMensaje(self,mensaje):
        print(mensaje)

    def UsuarioTieneContraseniaFuerte(self,usuario):
        print(f"El usuario {usuario._nombre} {usuario._apellido} tiene una contraseña fuerte.")
    
    def UsuarioTieneContraseniaDebil(self,usuario):
        print(f"El usuario {usuario._nombre} {usuario._apellido} tiene una contraseña débil.")

    def MostrarMensajeError(self,mensaje):
        print(f'Error: {mensaje}')

    def MostrarUsuariosHabilitados(self,usuarios):

        if usuarios:
            print('USUARIOS HABILITADOS')
            for usuario in usuarios:
                print(f'Usuario: {usuario._nombre}, {usuario._apellido}\nMail: {usuario._mail}\nEstado: {usuario._estado}')
        else:
            print('No hay usuarios habilitados')
    
    def MostrarUsuarios(self,usuarios):
        if usuarios:
            print('MOSTRANDO TODOS LOS USUARIOS')
            for usuario in usuarios:
                print(f'Usuario: {usuario._nombre}, {usuario._apellido}\nMail: {usuario._mail}\nEstado: {usuario._estado}')
        else:
            print('No hay usuarios')