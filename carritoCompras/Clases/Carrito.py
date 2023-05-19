class Carrito:
    def __init__(self,items) -> None:
       self.items = items

    def get_cliente(self):
        return self._cliente

    def get_items(self):
        return self._items

    def set_cliente(self, cliente):
        self._cliente = cliente

    def set_items(self, items):
        self._items = items

    def calcularTotal(self):
        total = 0

        for item in self.items:
            total = total + item.calcularImporte()
        return total
               
