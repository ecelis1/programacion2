class AutoEstereo:
    def __init__(self,marcaEstereo,modeloEstereo) -> None:
        self.marcaEstereo = marcaEstereo
        self.modeloEstereo = modeloEstereo
    
    def __str__(self) -> str:
        return (f'La marca del stereo es: {self.marcaEstereo}, y su modelo es {self.modeloEstereo} ')