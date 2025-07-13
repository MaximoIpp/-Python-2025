from colorama import init, Fore, Style
import db
import validaciones as val
import utils

init(autoreset=True)

def registrar_producto():
    print(Fore.CYAN + "\n--- Registrar Producto ---" + Style.RESET_ALL)
    nombre = input("Nombre del producto: ").strip()
    if not val.validar_nombre(nombre):
        utils.print_error("Error: El nombre no puede estar vacío.")
        input("Presione Enter para continuar...")
        return

    descripcion = input("Descripción (opcional): ").strip()

    cantidad = input("Cantidad disponible: ").strip()
    if not val.validar_cantidad(cantidad):
        utils.print_error("Error: La cantidad debe ser un número entero mayor o igual a 0.")
        input("Presione Enter para continuar...")
        return
    cantidad = int(cantidad)

    precio = input("Precio: ").strip()
    if not val.validar_precio(precio):
        utils.print_error("Error: El precio debe ser un número positivo.")
        input("Presione Enter para continuar...")
        return
    precio = float(precio)

    categoria = input("Categoría (opcional): ").strip()

    try:
        db.insertar_producto(nombre, descripcion, cantidad, precio, categoria)
        utils.print_success("Producto registrado exitosamente.")
    except Exception as e:
        utils.print_error(f"Error al registrar el producto: {e}")
    input("Presione Enter para continuar...")

def mostrar_productos():
    productos = db.obtener_productos()
    print(Fore.CYAN + "\n--- Productos Registrados ---" + Style.RESET_ALL)
    if productos:
        for p in productos:
            print(f"ID: {p[0]} | Nombre: {p[1]} | Descripción: {p[2] or '-'} | "
                  f"Cantidad: {p[3]} | Precio: ${p[4]:.2f} | Categoría: {p[5] or '-'}")
    else:
        utils.print_warning("No hay productos registrados.")
    input("\nPresione Enter para continuar...")

def actualizar_producto():
    mostrar_productos()
    print(Fore.CYAN + "\n--- Actualizar Producto ---" + Style.RESET_ALL)
    id_prod = input("Ingrese el ID del producto a actualizar: ").strip()
    if not val.validar_id(id_prod):
        utils.print_error("ID inválido.")
        input("Presione Enter para continuar...")
        return
    id_prod = int(id_prod)

    nombre = input("Nuevo nombre del producto: ").strip()
    if not val.validar_nombre(nombre):
        utils.print_error("Error: El nombre no puede estar vacío.")
        input("Presione Enter para continuar...")
        return

    descripcion = input("Nueva descripción (opcional): ").strip()

    cantidad = input("Nueva cantidad disponible: ").strip()
    if not val.validar_cantidad(cantidad):
        utils.print_error("Error: La cantidad debe ser un número entero mayor o igual a 0.")
        input("Presione Enter para continuar...")
        return
    cantidad = int(cantidad)

    precio = input("Nuevo precio: ").strip()
    if not val.validar_precio(precio):
        utils.print_error("Error: El precio debe ser un número positivo.")
        input("Presione Enter para continuar...")
        return
    precio = float(precio)

    categoria = input("Nueva categoría (opcional): ").strip()

    try:
        rows = db.actualizar_producto(id_prod, nombre, descripcion, cantidad, precio, categoria)
        if rows == 0:
            utils.print_warning("No se encontró producto con ese ID.")
        else:
            utils.print_success("Producto actualizado correctamente.")
    except Exception as e:
        utils.print_error(f"Error al actualizar producto: {e}")
    input("Presione Enter para continuar...")

def eliminar_producto():
    mostrar_productos()
    print(Fore.CYAN + "\n--- Eliminar Producto ---" + Style.RESET_ALL)
    id_prod = input("Ingrese el ID del producto a eliminar: ").strip()
    if not val.validar_id(id_prod):
        utils.print_error("ID inválido.")
        input("Presione Enter para continuar...")
        return
    id_prod = int(id_prod)

    confirm = input(Fore.YELLOW + f"¿Confirma eliminar el producto con ID {id_prod}? (s/n): ").strip().lower()
    if confirm != 's':
        utils.print_info("Eliminación cancelada.")
        input("Presione Enter para continuar...")
        return

    try:
        rows = db.eliminar_producto(id_prod)
        if rows == 0:
            utils.print_warning("No se encontró producto con ese ID.")
        else:
            utils.print_success("Producto eliminado correctamente.")
    except Exception as e:
        utils.print_error(f"Error al eliminar producto: {e}")
    input("Presione Enter para continuar...")

def buscar_producto():
    print(Fore.CYAN + "\n--- Buscar Producto ---" + Style.RESET_ALL)
    print("Buscar producto por:")
    print("1. ID")
    print("2. Nombre")
    print("3. Categoría")
    opcion = input("Seleccione opción: ").strip()

    try:
        if opcion == '1':
            id_buscar = input("Ingrese ID: ").strip()
            if not val.validar_id(id_buscar):
                utils.print_error("ID inválido.")
                input("Presione Enter para continuar...")
                return
            resultado = db.buscar_producto_por_id(int(id_buscar))
            resultados = [resultado] if resultado else []
        elif opcion == '2':
            nombre_buscar = input("Ingrese nombre o parte del nombre: ").strip()
            resultados = db.buscar_producto_por_nombre(nombre_buscar)
        elif opcion == '3':
            categoria_buscar = input("Ingrese categoría o parte de ella: ").strip()
            resultados = db.buscar_producto_por_categoria(categoria_buscar)
        else:
            utils.print_error("Opción inválida.")
            input("Presione Enter para continuar...")
            return

        if resultados:
            utils.print_info("\n--- Resultados de búsqueda ---")
            for p in resultados:
                print(f"ID: {p[0]} | Nombre: {p[1]} | Descripción: {p[2] or '-'} | Cantidad: {p[3]} | Precio: ${p[4]:.2f} | Categoría: {p[5] or '-'}")
        else:
            utils.print_warning("No se encontraron productos que coincidan.")
    except Exception as e:
        utils.print_error(f"Error en la búsqueda: {e}")
    input("Presione Enter para continuar...")

def reporte_cantidad_limite():
    print(Fore.CYAN + "\n--- Reporte por cantidad límite ---" + Style.RESET_ALL)
    limite = input("Ingrese la cantidad límite para el reporte: ").strip()
    if not val.validar_cantidad(limite):
        utils.print_error("Cantidad inválida.")
        input("Presione Enter para continuar...")
        return
    limite = int(limite)

    try:
        productos = db.productos_cantidad_limite(limite)
        if productos:
            utils.print_info(f"\n--- Productos con cantidad menor o igual a {limite} ---")
            for p in productos:
                print(f"ID: {p[0]} | Nombre: {p[1]} | Cantidad: {p[3]}")
        else:
            utils.print_warning("No hay productos con cantidad menor o igual a ese límite.")
    except Exception as e:
        utils.print_error(f"Error al generar reporte: {e}")
    input("Presione Enter para continuar...")

def menu():
    db.crear_base_y_tabla()
    while True:
        print(Fore.MAGENTA + "\n=== Menú Principal ===" + Style.RESET_ALL)
        print("1. Registrar producto")
        print("2. Mostrar productos")
        print("3. Actualizar producto")
        print("4. Eliminar producto")
        print("5. Buscar producto")
        print("6. Reporte por cantidad límite")
        print("7. Salir")
        opcion = input("Seleccione una opción: ").strip()

        if opcion == '1':
            registrar_producto()
        elif opcion == '2':
            mostrar_productos()
        elif opcion == '3':
            actualizar_producto()
        elif opcion == '4':
            eliminar_producto()
        elif opcion == '5':
            buscar_producto()
        elif opcion == '6':
            reporte_cantidad_limite()
        elif opcion == '7':
            utils.print_info("¡Gracias por usar el sistema! Hasta luego.")
            break
        else:
            utils.print_error("Opción inválida. Intente nuevamente.")
            input("Presione Enter para continuar...")

if __name__ == "__main__":
    menu()
