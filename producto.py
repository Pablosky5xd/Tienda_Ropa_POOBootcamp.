class Producto:
    def __init__(self, nombre, precio):
        self._nombre = nombre  
        self._precio = precio

    def mostrar_info(self):
        return f"{self._nombre} - Precio: {self._precio}"

class Ropa(Producto):
    def __init__(self, nombre, precio, cantidad):
        super().__init__(nombre, precio)
        self._cantidad = cantidad

    def mostrar_info(self):
        return f"{super().mostrar_info()}, Cantidad: {self._cantidad}"

class Camisa(Ropa):
    def __init__(self, nombre, precio, cantidad, talla):
        super().__init__(nombre, precio, cantidad)
        self._talla = talla

    def mostrar_info(self):
        return f"{super().mostrar_info()}, Talla: {self._talla}"

class Pantalon(Ropa):
    def __init__(self, nombre, precio, cantidad, talla):
        super().__init__(nombre, precio, cantidad)
        self._talla = talla

    def mostrar_info(self):
        return f"{super().mostrar_info()}, Talla: {self._talla}"

class Zapato(Ropa):
    def __init__(self, nombre, precio, cantidad, talla):
        super().__init__(nombre, precio, cantidad)
        self._talla = talla

    def mostrar_info(self):
        return f"{super().mostrar_info()}, Talla: {self._talla}"
