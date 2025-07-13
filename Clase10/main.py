# -*- coding: utf-8 -*-

def agregar_producto(productos, nombre, precio):
    """Agrega un producto a la lista y devuelve la lista actualizada."""
    productos.append({"nombre": nombre, "precio": precio})
    return productos

def consultar_productos(productos):
    """Devuelve una lista con la descripción de los productos."""
    if not productos:
        return ["No hay productos en la lista."]
    return [f"{idx}. {p['nombre']} - ${p['precio']:.2f}" for idx, p in enumerate(productos, 1)]

def eliminar_producto(productos, nombre):
    """Elimina un producto por nombre y devuelve la lista actualizada y un mensaje."""
    for producto in productos:
        if producto["nombre"].lower() == nombre.lower():
            productos.remove(producto)
            return productos, "Producto eliminado correctamente."
    return productos, "Producto no encontrado."

def menu():
    productos = []
    while True:
        print("\n--- Menú de Productos ---")
        print("1. Agregar producto")
        print("2. Consultar productos")
        print("3. Eliminar producto")
        print("4. Salir del programa")
        print("---------------------------")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Ingrese el nombre del producto: ").strip()
            if not nombre:
                print("El nombre no puede estar vacío.\n")
                continue
            try:
                precio = float(input("Ingrese el precio del producto: "))
                if precio < 0:
                    print("El precio no puede ser negativo.\n")
                    continue
                productos = agregar_producto(productos, nombre, precio)
                print("Producto agregado correctamente.\n")
            except ValueError:
                print("Precio inválido. Por favor, ingrese un número válido.\n")

        elif opcion == "2":
            lista_productos = consultar_productos(productos)
            print()
            for linea in lista_productos:
                print(linea)
            print()

        elif opcion == "3":
            nombre = input("Ingrese el nombre del producto a eliminar: ").strip()
            if not nombre:
                print("El nombre no puede estar vacío.\n")
                continue
            productos, mensaje = eliminar_producto(productos, nombre)
            print(mensaje + "\n")

        elif opcion == "4":
            print("¡Hasta luego!")
            break

        else:
            print("Opción inválida. Intente de nuevo.\n")

if __name__ == "__main__":
    menu()
    