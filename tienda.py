from producto import Producto

class Tienda:
    def __init__(self):
        self.productos = [] 

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def mostrar_productos(self):
        for index, producto in enumerate(self.productos):
            print(f"{index + 1}. {producto.mostrar_info()}")
