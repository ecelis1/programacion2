from View.VistaProducto import VistaProducto
from Modelo.Producto import Producto

class ControladorProducto():
    def __init__(self,vista = VistaProducto(), productos = []) -> None:
        self.vista = vista
        self.producto = productos

    def mostrar_informacion(self):
        if len(self.productos)==0:
            self.productos = self.inicializarProdcutos()
        self.vista.mostrar_productos(self.productos)

    def inicializarProductos(self):
        producto1 = Producto('cepillo',100,1)
        producto2 = Producto('cepillo 2',150,2)

        self.productos = [producto1,producto2]

        return self.productos
    
    def getProductoForCodigo(self,codigo):
        for producto in self.productos:
            if producto.get_codigo() == int(codigo):
                return producto
    
    def seleccionarProducto(self):
        codigo = self.vista.solicitar_seleccion_producto()
        return self.getProductoForCodigo(codigo)