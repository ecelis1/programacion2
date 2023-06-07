from AutoEstereo import AutoEstereo

class Auto:
    def __init__(self,modelo,marca,precio=0) -> None:
        self.modelo = modelo
        self.marca = marca
        self.precio = precio
        self.autostereo = None

    def __str__(self) -> str:
        return (f'La marca del auto es: {self.marca} , modelo {self.modelo}')
    
    def get_auto(self):
        if self.autostereo == None:
            print('El auto no tiene Stereo')
        else:
            print(self.autostereo)
            

        return(f'La marca del auto es: {self.marca} ,modelo {self.modelo}, precio: {self.precio}')
        
       
    
    def add_AutoEstereo(self,autostereo):
        if isinstance(autostereo, AutoEstereo):
            self.autostereo = autostereo
            AutoEstereo.__str__
        
            

    
