class Calculadora:
    def __init__(self,A=0, B=0, operacion="0" ):
        self.numA = A
        self.numB = B
        self.operacion = operacion

    def getNumA(self):
        return self.numA

    def setNumA(self,X):
        self.numA = X

    def setNumB(self,X):
        self.numB = X

    def getNumB(self):
        return self.numB

    def setOperacion(self,operacion):
        self.operacion=operacion

    def getOperacion(self):
        return self.operacion

    def __str__(self):
        return self.numA +''+ self.numB

    def sumar(self):
        if self.operacion == "1":
            return int(self.numA)+int(self.numB)

    def restar(self):
        if self.operacion == "2":
            return int(self.numA) - int(self.numB)

    def dividir(self):
        if self.operacion == "3":
            if self.numB == "0":
                print('No se puede dividir por 0')
            else:
                return int(self.numA) / int(self.numB)

    def multiplicar(self):
        if self.operacion == "4":
            return int(self.numA) * int(self.numB)


