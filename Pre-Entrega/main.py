# Lista principal donde se almacenan los productos.
# Cada producto es una sublista con tres elementos: [nombre_producto, categoria_producto, precio_producto]
db_productos = []

while True:
    print("Sistema de Gestión Básica De Productos")
    print("1. Agregar producto")
    print("2. Mostrar productos")
    print("3. Buscar producto")
    print("4. Eliminar producto")
    print("5. Salir")
    
    opcion = input("Seleccione una opción (1-5): ").strip()
    print()

    # OPCIÓN 1: AGREGAR PRODUCTO
    if opcion == '1':
        while True:
            # pedir y validar el nombre del producto
            while True:
                nombre_producto = input("Ingrese el nombre del producto: ").strip().title()
                if nombre_producto == "":
                    print("El nombre no puede estar vacío. Intente nuevamente.")
                else:
                    break  # nombre válido, salir del bucle

            # pedir y validar la categoría del producto
            while True:
                categoria_producto = input("Ingrese la categoría del producto: ").strip().title()
                if categoria_producto == "":
                    print("La categoría no puede estar vacía. Intente nuevamente.")
                else:
                    break  # categoría válida, salir del bucle

            # pedir y validar el precio del producto
            while True:
                precio_str = input("Ingrese el precio (sin centavos, solo números enteros): ").strip()
                try:
                    precio_producto = int(precio_str)
                    if precio_producto <= 0:
                        print("El precio debe ser mayor que cero. Intente nuevamente.")
                    else:
                        break  # precio válido, salir del bucle
                except ValueError:
                    print("El precio debe ser un número entero positivo. Intente nuevamente.")

            # agregar el producto validado a la lista principal
            db_productos.append([nombre_producto, categoria_producto, precio_producto])
            print(f"Producto '{nombre_producto}' agregado correctamente.\n")

            # preguntar si el usuario desea agregar otro producto
            agregar_otro = input("¿Desea agregar otro producto? (s/n): ").strip().lower()
            if agregar_otro != 's':
                # si la respuesta no es 's', salir del ciclo de agregar productos y volver al menú principal
                break

    # OPCIÓN 2: MOSTRAR PRODUCTOS
    elif opcion == '2':
        if not db_productos:
            print("No hay productos registrados.\n")
        else:
            print("Lista de productos registrados:")
            print("-" * 40)
            # recorrer la lista y mostrar cada producto con su índice para facilitar la lectura
            for i, prod in enumerate(db_productos, start=1):
                nombre_producto, categoria_producto, precio_producto = prod
                print(f"{i}. Nombre: {nombre_producto} | Categoría: {categoria_producto} | Precio: ${precio_producto}")
            print("-" * 40 + "\n")

    # OPCIÓN 3: BUSCAR PRODUCTO
    elif opcion == '3':
        if not db_productos:
            print("No hay productos para buscar.\n")
        else:
            # solicitar término de búsqueda y convertirlo a minúsculas para búsqueda insensible a mayúsculas/minúsculas
            busqueda = input("Ingrese el nombre del producto a buscar: ").strip().lower()
            if busqueda == "":
                print("La búsqueda no puede estar vacía.\n")
            else:
                # filtrar productos cuyo nombre contenga el término de búsqueda
                encontrados = [prod for prod in db_productos if busqueda in prod[0].lower()]
                if encontrados:
                    print(f"Se encontraron {len(encontrados)} producto(s) que coinciden con '{busqueda}':")
                    print("-" * 40)
                    # mostrar los productos encontrados con su índice
                    for i, prod in enumerate(encontrados, start=1):
                        nombre_producto, categoria_producto, precio_producto = prod
                        print(f"{i}. Nombre: {nombre_producto} | Categoría: {categoria_producto} | Precio: ${precio_producto}")
                    print("-" * 40 + "\n")
                else:
                    print(f"No se encontraron productos con el nombre '{busqueda}'.\n")

    # OPCIÓN 4: ELIMINAR PRODUCTO
    elif opcion == '4':
        if not db_productos:
            print("No hay productos para eliminar.\n")
        else:
            print("Lista de productos registrados:")
            print("-" * 40)
            # mostrar todos los productos con su índice para que el usuario elija cuál eliminar
            for i, prod in enumerate(db_productos, start=1):
                nombre_producto, categoria_producto, precio_producto = prod
                print(f"{i}. Nombre: {nombre_producto} | Categoría: {categoria_producto} | Precio: ${precio_producto}")
            print("-" * 40 + "\n")

            while True:
                # solicitar el número del producto a eliminar o '0' para cancelar la operación
                opcion_eliminar = input("Ingrese el número del producto que desea eliminar (o '0' para cancelar): ").strip()
                if opcion_eliminar == '0':
                    print("Operación cancelada.\n")
                    break  # salir sin eliminar

                if not opcion_eliminar.isdigit():
                    print("Debe ingresar un número válido. Intente nuevamente.")
                    continue  # pedir nuevamente si no es un número válido

                indice = int(opcion_eliminar) - 1  # ajustar índice para lista (0-based)

                if 0 <= indice < len(db_productos):
                    producto_eliminado = db_productos.pop(indice)  # eliminar producto
                    print(f"Producto '{producto_eliminado[0]}' eliminado correctamente.\n")
                    break  # salir después de eliminar
                else:
                    print("Número fuera de rango. Intente nuevamente.")

    # OPCIÓN 5: SALIR DEL PROGRAMA
    elif opcion == '5':
        print("Gracias por usar el sistema. ¡Hasta luego!")
        break  # terminar el ciclo principal y salir

    else:
        # manejo de opción inválida ingresada por el usuario
        print("Opción inválida. Por favor, seleccione una opción del 1 al 5.\n")
