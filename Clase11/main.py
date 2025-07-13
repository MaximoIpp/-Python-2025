# -*- coding: utf-8 -*-
from colorama import init, Fore, Style
from datetime import datetime

# Inicializa Colorama para que funcione en Windows también
init(autoreset=True)

def agregar_producto(productos, nombre, precio):
    """Agrega un producto con fecha y hora actual a la lista y devuelve la lista actualizada."""
    fecha_compra = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    productos.append({"nombre": nombre, "precio": precio, "fecha": fecha_compra})
    return productos

def consultar_productos(productos):
    """Devuelve una lista con la descripción de los productos con colores y fecha."""
    if not productos:
        return [Fore.YELLOW + "No hay productos en la lista." + Style.RESET_ALL]
    lista = []
    for idx, p in enumerate(productos, 1):
        linea = (
            f"{Fore.CYAN}{idx}. {Fore.GREEN}{p['nombre']}{Style.RESET_ALL} - "
            f"{Fore.MAGENTA}${p['precio']:.2f}{Style.RESET_ALL} - "
            f"{Fore.BLUE}Fecha: {p['fecha']}{Style.RESET_ALL}"
        )
        lista.append(linea)
    return lista

def eliminar_producto(productos, nombre):
    """Elimina un producto por nombre y devuelve la lista actualizada y un mensaje coloreado."""
    for producto in productos:
        if producto["nombre"].lower() == nombre.lower():
            productos.remove(producto)
            return productos, Fore.GREEN + "Producto eliminado correctamente." + Style.RESET_ALL
    return productos, Fore.RED + "Producto no encontrado." + Style.RESET_ALL

def menu():
    productos = []
    while True:
        print(Fore.YELLOW + "\n--- Menú de Productos ---" + Style.RESET_ALL)
        print(Fore.CYAN + "1. Agregar producto")
        print("2. Consultar productos")
        print("3. Eliminar producto")
        print("4. Salir del programa" + Style.RESET_ALL)
        print(Fore.YELLOW + "---------------------------" + Style.RESET_ALL)
        opcion = input(Fore.WHITE + "Seleccione una opción: " + Style.RESET_ALL)

        if opcion == "1":
            nombre = input(Fore.WHITE + "Ingrese el nombre del producto: " + Style.RESET_ALL).strip()
            if not nombre:
                print(Fore.RED + "El nombre no puede estar vacío.\n" + Style.RESET_ALL)
                continue
            try:
                precio = float(input(Fore.WHITE + "Ingrese el precio del producto: " + Style.RESET_ALL))
                if precio < 0:
                    print(Fore.RED + "El precio no puede ser negativo.\n" + Style.RESET_ALL)
                    continue
                productos = agregar_producto(productos, nombre, precio)
                print(Fore.GREEN + "Producto agregado correctamente.\n" + Style.RESET_ALL)
            except ValueError:
                print(Fore.RED + "Precio inválido. Por favor, ingrese un número válido.\n" + Style.RESET_ALL)

        elif opcion == "2":
            lista_productos = consultar_productos(productos)
            print()
            for linea in lista_productos:
                print(linea)
            print()

        elif opcion == "3":
            nombre = input(Fore.WHITE + "Ingrese el nombre del producto a eliminar: " + Style.RESET_ALL).strip()
            if not nombre:
                print(Fore.RED + "El nombre no puede estar vacío.\n" + Style.RESET_ALL)
                continue
            productos, mensaje = eliminar_producto(productos, nombre)
            print(mensaje + "\n")

        elif opcion == "4":
            print(Fore.YELLOW + "¡Hasta luego!" + Style.RESET_ALL)
            break

        else:
            print(Fore.RED + "Opción inválida. Intente de nuevo.\n" + Style.RESET_ALL)

if __name__ == "__main__":
    menu()
