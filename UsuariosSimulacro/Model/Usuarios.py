import os

rutaArchivo = 'Data/archivoUsuarios.txt'

class Usuario:
    def __init__(self,apellido = str,nombre = str,dni = str,mail = str, password = str, estado = str, usuarios = []):
        
        self._apellido = apellido
        self._nombre = nombre
        self._dni = dni
        self._mail = mail
        self._password = password
        self._estado = estado
        self.usuarios = usuarios

    def getDNI(self):
        return self._dni

    def setDNI(self, x):
        self._dni = x

    def getPassword(self):
        return self._password
    def setPassword(self,x):
        self._password=x

    def getApellido(self):
        return self._apellido

    def setApellido(self, x):
        self._apellido = x

    def getNombre(self):
        return self._nombre

    def setNombre(self, x):
        self._nombre = x

    def getMail(self):
        return self._mail

    def setMail(self, x):
        self._mail = x

    def getEstado(self):
        return self._estado

    def setEstado(self, x):
        self._estado = x


    def cargarUsuariosArchivo(self):     

        if os.path.exists(rutaArchivo):
            with open(rutaArchivo,'r') as archivoUser:
                for linea in archivoUser:
                    datos = linea.strip().split(",")
                    #usuario()
                    usuario = Usuario(datos[0],datos[1],datos[2],datos[3],datos[4],datos[5])
                    self.usuarios.append(usuario)
            print('Se cargaron los usuarios cargados en el archivo.')
        else:
            with open(rutaArchivo, 'w'):
                pass
            print("Archivo creado.")

    def obtenerHabilitado(self):
        usuariosHabilitados = []
        for usuario in self.usuarios:
            if usuario.getEstado() == 'habilitado':
                usuariosHabilitados.append(usuario)
        return usuariosHabilitados
    
    def isPassFuerte(self):
        mayusculas = 0
        minusculas = 0
        numeros = 0

        for caracter in self._password:
            if caracter.isupper():
                mayusculas += 1
            elif caracter.islower():
                minusculas += 1
            elif caracter.isdigit():
                numeros += 1

        return mayusculas > 2 and minusculas > 1 and numeros > 5
    
    def obtenerUsuarioPorDNI(self, dni):
        for usuario in self.usuarios:
            if usuario._dni == dni:
                return usuario
        return None
    
    def verificarMailExistente(self, mail):
        for usuario in self.usuarios:
            if usuario._mail == mail:
                return True
        return False
    
    def RegistrarUsuario(self,apellido,nombre,dni,mail,password,estado):
        if self.verificarMailExistente(mail):
            return True
        else:
            nuevoUser = Usuario(apellido,nombre,dni,mail,password,estado)
            if nuevoUser.isPassFuerte():
                self.usuarios.append(nuevoUser)
                with open(rutaArchivo, "a") as archivo:
                    ultimo_usuario = self.usuarios[-1]
                    archivo.write(f"\n{ultimo_usuario._apellido},{ultimo_usuario._nombre},{ultimo_usuario._dni},{ultimo_usuario._mail},{ultimo_usuario._password},{ultimo_usuario._estado}")
                
                print('Usuario Guardado, Exitosamente')
            else:
                print('La contrasenia no es fuerte')



