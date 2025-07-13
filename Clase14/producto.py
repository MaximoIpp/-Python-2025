import sqlite3
from colorama import init, Fore, Style

# Inicializar Colorama
init(autoreset=True)

DB_NAME = 'productos.db'

def crear_base_y_tabla():
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS productos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                precio REAL NOT NULL CHECK(precio > 0)
            )
        ''')
        conn.commit()
    except sqlite3.Error as e:
        print(Fore.RED + f"Error al crear la base de datos o tabla: {e}")
    finally:
        conn.close()

def validar_nombre(nombre):
    return bool(nombre.strip())

def validar_precio(precio):
    try:
        p = float(precio)
        return p > 0
    except ValueError:
        return False

def registrar_producto():
    nombre = input("Ingrese el nombre del producto: ").strip()
    if not validar_nombre(nombre):
        print(Fore.RED + "Error: El nombre no puede estar vacío.")
        return

    precio = input("Ingrese el precio del producto: ").strip()
    if not validar_precio(precio):
        print(Fore.RED + "Error: El precio debe ser un número positivo.")
        return

    precio = float(precio)

    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("BEGIN TRANSACTION")
        cursor.execute("INSERT INTO productos (nombre, precio) VALUES (?, ?)", (nombre, precio))
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
        cursor.execute("SELECT id, nombre, precio FROM productos ORDER BY id")
        productos = cursor.fetchall()
        if productos:
            print(Fore.BLUE + "\n--- Productos registrados ---")
            for prod in productos:
                print(f"ID: {prod[0]} | Nombre: {prod[1]} | Precio: ${prod[2]:.2f}")
            print()
        else:
            print(Fore.YELLOW + "No hay productos registrados.")
    except sqlite3.Error as e:
        print(Fore.RED + f"Error al obtener los productos: {e}")
    finally:
        conn.close()

def eliminar_producto():
    mostrar_productos()
    id_eliminar = input("Ingrese el ID del producto a eliminar: ").strip()
    if not id_eliminar.isdigit():
        print(Fore.RED + "ID inválido.")
        return

    confirmacion = input(Fore.YELLOW + f"¿Está seguro que desea eliminar el producto con ID {id_eliminar}? (s/n): ").strip().lower()
    if confirmacion != 's':
        print(Fore.CYAN + "Eliminación cancelada.")
        return

    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("BEGIN TRANSACTION")
        cursor.execute("DELETE FROM productos WHERE id = ?", (int(id_eliminar),))
        if cursor.rowcount == 0:
            print(Fore.YELLOW + "No se encontró un producto con ese ID.")
            conn.rollback()
        else:
            conn.commit()
            print(Fore.GREEN + "Producto eliminado correctamente.")
    except sqlite3.Error as e:
        conn.rollback()
        print(Fore.RED + f"Error al eliminar el producto: {e}")
    finally:
        conn.close()

def menu():
    crear_base_y_tabla()
    while True:
        print(Fore.CYAN + "\n----- Menú de Productos -----")
        print("1. Registrar producto")
        print("2. Mostrar productos")
        print("3. Eliminar producto")
        print("4. Salir")
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            registrar_producto()
        elif opcion == "2":
            mostrar_productos()
        elif opcion == "3":
            eliminar_producto()
        elif opcion == "4":
            print(Fore.CYAN + "¡Hasta luego!")
            break
        else:
            print(Fore.RED + "Opción inválida. Intente de nuevo.")

if __name__ == "__main__":
    menu()
