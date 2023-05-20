from pyexpat import model
from Modelo.Producto import Producto

class ItemCarrito:
    def __init__(self,producto,cantidad):
         self.producto = producto
         self.cantidad = cantidad

    def get_producto(self):
        return self._producto

    def get_cantidad(self):
        return self._cantidad

    def set_producto(self,producto):
        self._producto=producto

    def set_cantidad(self, cantidad):
        self._cantidad = cantidad

    def calcularImporte(self):
        return int(self.cantidad) * int(self.producto.get_precio())