from Modelo.Calculadora import Calculadora
from Vista.VistaCalculadora import *

class CalculadorControlador:
        def __init__(self):
            self.vista = VistaCalculadora()
            self.modelo = Calculadora()

        def iniciarMenu(self):

            while True:
                self.vista.mostrarMenu()
                try:
                    op = self.vista.pedirAccion()
                    if op<=0 or op>5:
                        print("Ingrese la opcion correcta, para poder realizar la operacion.\nIngrese '5' y pulse ENTER para SALIR")
                except:
                    print('Ingrese el valor correcto')
                self.modelo.setOperacion(op)
                if op == "1":
                    A=self.vista.pedirNumero()
                    B=self.vista.pedirNumero()
                    self.modelo.setNumA(A)
                    self.modelo.setNumB(B)
                    R=self.modelo.sumar()
                    self.vista.mostrarResultado(R)
                elif op == "2":
                    A = self.vista.pedirNumero()
                    B = self.vista.pedirNumero()
                    self.modelo.setNumA(A)
                    self.modelo.setNumB(B)
                    R = self.modelo.restar()
                    self.vista.mostrarResultado(R)

                elif op == "3":
                    A = self.vista.pedirNumero()
                    B = self.vista.pedirNumero()
                    self.modelo.setNumA(A)
                    self.modelo.setNumB(B)
                    R = self.modelo.dividir()
                    self.vista.mostrarResultado(R)
                elif op == "4":
                    A = self.vista.pedirNumero()
                    B = self.vista.pedirNumero()
                    self.modelo.setNumA(A)
                    self.modelo.setNumB(B)
                    R = self.modelo.multiplicar()
                    self.vista.mostrarResultado(R)
                elif op == "5":
                    break
