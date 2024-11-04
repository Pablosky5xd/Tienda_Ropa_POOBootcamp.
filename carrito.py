class Carrito:
    def __init__(self):
        self.articulos = []  

    def agregar_al_carrito(self, producto):
        self.articulos.append(producto)

    def calcular_total(self):
        return sum(producto._precio for producto in self.articulos)

    def mostrar_resumen(self):
        print("Resumen de la compra:")
        for producto in self.articulos:
            print(producto.mostrar_info())
        print(f"Total a pagar: {self.calcular_total()}")
