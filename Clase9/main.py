# Programa de gestión de productos

productos = []

def mostrar_menu():
    print("\n--- Menú de Productos ---")
    print("1. Agregar producto")
    print("2. Consultar productos")
    print("3. Eliminar producto")
    print("4. Salir del programa")
    print("---------------------------")

def agregar_producto():
    nombre = input("Ingrese el nombre del producto: ")
    try:
        precio = float(input("Ingrese el precio del producto: "))
        productos.append({"nombre": nombre, "precio": precio})
        print("Producto agregado con éxito!")
    except ValueError:
        print("Error: El precio debe ser un número.")

def consultar_productos():
    if not productos:
        print("No hay productos registrados.")
        return
    print("\nLista de productos:")
    for idx, producto in enumerate(productos, start=1):
        print(f"{idx}. {producto['nombre']} - ${producto['precio']:.2f}")

def eliminar_producto():
    consultar_productos()
    if not productos:
        return
    nombre = input("Ingrese el nombre del producto a eliminar: ")
    encontrado = False
    for producto in productos[:]:
        if producto["nombre"].lower() == nombre.lower():
            productos.remove(producto)
            encontrado = True
            print("Producto eliminado con éxito!")
            break
    if not encontrado:
        print("No se encontró el producto.")

def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            agregar_producto()
        elif opcion == "2":
            consultar_productos()
        elif opcion == "3":
            eliminar_producto()
        elif opcion == "4":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()
