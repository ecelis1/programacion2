import os

from Modelo.Carrito import Carrito
from Modelo.ItemCarrito import ItemCarrito
from Controller.ControladorProducto import ControladorProducto
from View.VistaProducto import VistaCarrito

class CargarCarrito:
    def __init__(self,vista = VistaCarrito(), controladorP = ControladorProducto(),modelo = '') -> None:
        self.vista = vista
        self.controladorP = controladorP
        self.modelo = modelo

    def cargar_items_carrito(self):
        self.controladorP.mostrar_informacion()
        item = ItemCarrito(self.controladorP.seleccionarProducto(),self.vista.generar)
        item2 = ItemCarrito(self.controladorP.seleccionarProducto(),self.vista.generar)
        items = [item,item2]
        return items

    def crear_nuevo_objeto(self):
        items = self.cargar_items_carrito()
        self.modelo = Carrito(items)
        
    def mostrar_total(self):
        self.vista.mostrar_total(self.modelo.calcularTotal())