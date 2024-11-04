from tienda import Tienda
from carrito import Carrito
from producto import Camisa, Pantalon, Zapato

def main():
    tienda = Tienda()
    tienda.agregar_producto(Camisa("Camisa de Hombre", 50000, 50, "M"))
    tienda.agregar_producto(Pantalon("Pantalón de Hombre", 120000, 30, "L"))
    tienda.agregar_producto(Zapato("Zapato de Hombre", 200000, 25, "42"))
    
    carrito = Carrito()
    
    while True:
        print("\n--- Menú ---")
        print("1. Mostrar productos")
        print("2. Agregar producto al carrito")
        print("3. Ver resumen de compra")
        print("4. Salir")
        
        opcion = input("Selecciona una opción: ")
        
        if opcion == "1":
            tienda.mostrar_productos()
        
        elif opcion == "2":
            tienda.mostrar_productos()
            seleccion = int(input("Selecciona el número del producto a agregar al carrito: ")) - 1
            
            if 0 <= seleccion < len(tienda.productos):
                carrito.agregar_al_carrito(tienda.productos[seleccion])
                print(f"{tienda.productos[seleccion]._nombre} agregado al carrito.")
            else:
                print("Selección inválida.")
        
        elif opcion == "3":
            carrito.mostrar_resumen()
        
        elif opcion == "4":
            print("Gracias por tu compra. ¡Hasta luego!")
            break
        
        else:
            print("Opción no válida, por favor selecciona nuevamente.")

if __name__ == "__main__":
    main()
