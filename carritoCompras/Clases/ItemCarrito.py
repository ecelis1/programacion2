import Clases.Producto
class ItemCarrito:
    def __init__(self,producto,cantidad):
         self.producto = producto
         self.cantidad = cantidad

    def calcularImporte(self):
         if (isinstance(self.producto,Clases.Producto.Producto)):
            return self.cantidad * self.producto.get_precio()