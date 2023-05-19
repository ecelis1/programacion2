class Carrito:
    def __init__(self,items) -> None:
       self.items = items

    def calcularTotal(self):
        total = 0

        for item in self.items:
            total = total + item.calcularImporte()
        return total
               
