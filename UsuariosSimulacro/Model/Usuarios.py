class Usuario:
    def __init__(self,dni,password,apellido,nombre,mail,estado=False):
        self._dni = dni
        self._password = password
        self._apellido = apellido
        self._nombre = nombre

        self._mail = mail
        self._estado = estado

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
        return self._password

    def setEstado(self, x):
        self._password = x





    def isHabilitado(self):

    def isPassFuerte(self):
        pass