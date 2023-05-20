class VistaProducto:
    def mostrar_producto(self,listaP):
        for item in listaP:
            print (item)
    
    def solicitar_seleccion_producto(self):
        return input('Ingrese el codigo del producto que desea: ')