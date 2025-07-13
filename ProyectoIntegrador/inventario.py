import sqlite3
from colorama import init, Fore, Style

# Inicializar Colorama
init(autoreset=True)

DB_NAME = 'inventario.db'

def crear_base_y_tabla():
    """Crea la base de datos y la tabla productos si no existen."""
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS productos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                descripcion TEXT,
                cantidad INTEGER NOT NULL CHECK(cantidad >= 0),
                precio REAL NOT NULL CHECK(precio > 0),
                categoria TEXT
            )
        ''')
        conn.commit()
    except sqlite3.Error as e:
        print(Fore.RED + f"Error al crear la base de datos o tabla: {e}")
    finally:
        conn.close()

def validar_nombre(nombre):
    return bool(nombre.strip())

def validar_cantidad(cantidad):
    try:
        c = int(cantidad)
        return c >= 0
    except ValueError:
        return False

def validar_precio(precio):
    try:
        p = float(precio)
        return p > 0
    except ValueError:
        return False

def registrar_producto():
    nombre = input("Nombre del producto: ").strip()
    if not validar_nombre(nombre):
        print(Fore.RED + "Error: El nombre no puede estar vacío.")
        return

    descripcion = input("Descripción (opcional): ").strip()

    cantidad = input("Cantidad disponible: ").strip()
    if not validar_cantidad(cantidad):
        print(Fore.RED + "Error: La cantidad debe ser un número entero mayor o igual a 0.")
        return
    cantidad = int(cantidad)

    precio = input("Precio: ").strip()
    if not validar_precio(precio):
        print(Fore.RED + "Error: El precio debe ser un número positivo.")
        return
    precio = float(precio)

    categoria = input("Categoría (opcional): ").strip()

    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("BEGIN TRANSACTION")
        cursor.execute('''
            INSERT INTO productos (nombre, descripcion, cantidad, precio, categoria)
            VALUES (?, ?, ?, ?, ?)
        ''', (nombre, descripcion, cantidad, precio, categoria))
        conn.commit()
        print(Fore.GREEN + "Producto registrado exitosamente.")
    except sqlite3.Error as e:
        conn.rollback()
        print(Fore.RED + f"Error al registrar el producto: {e}")
    finally:
        conn.close()

def mostrar_productos():
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("SELECT id, nombre, descripcion, cantidad, precio, categoria FROM productos ORDER BY id")
        productos = cursor.fetchall()
        if productos:
            print(Fore.BLUE + "\n--- Productos Registrados ---")
            for p in productos:
                print(f"ID: {p[0]} | Nombre: {p[1]} | Descripción: {p[2] or '-'} | Cantidad: {p[3]} | Precio: ${p[4]:.2f} | Categoría: {p[5] or '-'}")
            print()
        else:
            print(Fore.YELLOW + "No hay productos registrados.")
    except sqlite3.Error as e:
        print(Fore.RED + f"Error al obtener productos: {e}")
    finally:
        conn.close()

def actualizar_producto():
    mostrar_productos()
    id_prod = input("Ingrese el ID del producto a actualizar: ").strip()
    if not id_prod.isdigit():
        print(Fore.RED + "ID inválido.")
        return
    id_prod = int(id_prod)

    nombre = input("Nuevo nombre del producto: ").strip()
    if not validar_nombre(nombre):
        print(Fore.RED + "Error: El nombre no puede estar vacío.")
        return

    descripcion = input("Nueva descripción (opcional): ").strip()

    cantidad = input("Nueva cantidad disponible: ").strip()
    if not validar_cantidad(cantidad):
        print(Fore.RED + "Error: La cantidad debe ser un número entero mayor o igual a 0.")
        return
    cantidad = int(cantidad)

    precio = input("Nuevo precio: ").strip()
    if not validar_precio(precio):
        print(Fore.RED + "Error: El precio debe ser un número positivo.")
        return
    precio = float(precio)

    categoria = input("Nueva categoría (opcional): ").strip()

    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("BEGIN TRANSACTION")
        cursor.execute('''
            UPDATE productos
            SET nombre = ?, descripcion = ?, cantidad = ?, precio = ?, categoria = ?
            WHERE id = ?
        ''', (nombre, descripcion, cantidad, precio, categoria, id_prod))
        if cursor.rowcount == 0:
            print(Fore.YELLOW + "No se encontró producto con ese ID.")
            conn.rollback()
        else:
            conn.commit()
            print(Fore.GREEN + "Producto actualizado correctamente.")
    except sqlite3.Error as e:
        conn.rollback()
        print(Fore.RED + f"Error al actualizar producto: {e}")
    finally:
        conn.close()

def eliminar_producto():
    mostrar_productos()
    id_prod = input("Ingrese el ID del producto a eliminar: ").strip()
    if not id_prod.isdigit():
        print(Fore.RED + "ID inválido.")
        return
    id_prod = int(id_prod)

    confirm = input(Fore.YELLOW + f"¿Confirma eliminar el producto con ID {id_prod}? (s/n): ").strip().lower()
    if confirm != 's':
        print(Fore.CYAN + "Eliminación cancelada.")
        return

    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("BEGIN TRANSACTION")
        cursor.execute("DELETE FROM productos WHERE id = ?", (id_prod,))
        if cursor.rowcount == 0:
            print(Fore.YELLOW + "No se encontró producto con ese ID.")
            conn.rollback()
        else:
            conn.commit()
            print(Fore.GREEN + "Producto eliminado correctamente.")
    except sqlite3.Error as e:
        conn.rollback()
        print(Fore.RED + f"Error al eliminar producto: {e}")
    finally:
        conn.close()

def buscar_producto():
    print("Buscar producto por:")
    print("1. ID")
    print("2. Nombre")
    print("3. Categoría")
    opcion = input("Seleccione opción: ").strip()

    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()

        if opcion == '1':
            id_buscar = input("Ingrese ID: ").strip()
            if not id_buscar.isdigit():
                print(Fore.RED + "ID inválido.")
                return
            cursor.execute("SELECT * FROM productos WHERE id = ?", (int(id_buscar),))
        elif opcion == '2':
            nombre_buscar = input("Ingrese nombre o parte del nombre: ").strip()
            cursor.execute("SELECT * FROM productos WHERE nombre LIKE ?", ('%' + nombre_buscar + '%',))
        elif opcion == '3':
            categoria_buscar = input("Ingrese categoría o parte de ella: ").strip()
            cursor.execute("SELECT * FROM productos WHERE categoria LIKE ?", ('%' + categoria_buscar + '%',))
        else:
            print(Fore.RED + "Opción inválida.")
            return

        resultados = cursor.fetchall()
        if resultados:
            print(Fore.BLUE + "\n--- Resultados de búsqueda ---")
            for p in resultados:
                print(f"ID: {p[0]} | Nombre: {p[1]} | Descripción: {p[2] or '-'} | Cantidad: {p[3]} | Precio: ${p[4]:.2f} | Categoría: {p[5] or '-'}")
            print()
        else:
            print(Fore.YELLOW + "No se encontraron productos que coincidan.")
    except sqlite3.Error as e:
        print(Fore.RED + f"Error en la búsqueda: {e}")
    finally:
        conn.close()

def reporte_cantidad_limite():
    limite = input("Ingrese la cantidad límite para el reporte: ").strip()
    if not limite.isdigit():
        print(Fore.RED + "Cantidad inválida.")
        return
    limite = int(limite)

    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM productos WHERE cantidad <= ? ORDER BY cantidad ASC", (limite,))
        productos = cursor.fetchall()
        if productos:
            print(Fore.BLUE + f"\n--- Productos con cantidad menor o igual a {limite} ---")
            for p in productos:
                print(f"ID: {p[0]} | Nombre: {p[1]} | Cantidad: {p[3]}")
            print()
        else:
            print(Fore.YELLOW + "No hay productos con cantidad menor o igual a ese límite.")
    except sqlite3.Error as e:
        print(Fore.RED + f"Error al generar reporte: {e}")
    finally:
        conn.close()

def menu():
    crear_base_y_tabla()
    while True:
        print(Fore.CYAN + "\n=== Menú Principal ===")
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
            print(Fore.CYAN + "¡Gracias por usar el sistema! Hasta luego.")
            break
        else:
            print(Fore.RED + "Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    menu()
