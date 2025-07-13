import sqlite3

def crear_base_y_tabla():
    """Crea la base de datos y la tabla productos si no existen."""
    try:
        conn = sqlite3.connect('productos.db')
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
        print(f"Error al crear la base de datos o la tabla: {e}")
    finally:
        conn.close()

def registrar_producto():
    """Solicita datos, valida y guarda un producto en la base de datos."""
    nombre = input("Ingrese el nombre del producto: ").strip()
    if not nombre:
        print("Error: El nombre no puede estar vacío.")
        return

    try:
        precio = float(input("Ingrese el precio del producto: "))
        if precio <= 0:
            print("Error: El precio debe ser un número mayor que cero.")
            return
    except ValueError:
        print("Error: Precio inválido. Debe ingresar un número.")
        return

    try:
        conn = sqlite3.connect('productos.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO productos (nombre, precio) VALUES (?, ?)", (nombre, precio))
        conn.commit()
        print("Producto registrado exitosamente.")
    except sqlite3.Error as e:
        print(f"Error al registrar el producto: {e}")
    finally:
        conn.close()

def mostrar_productos():
    """Consulta y muestra todos los productos almacenados."""
    try:
        conn = sqlite3.connect('productos.db')
        cursor = conn.cursor()
        cursor.execute("SELECT id, nombre, precio FROM productos")
        productos = cursor.fetchall()
        if productos:
            print("\n--- Productos registrados ---")
            for prod in productos:
                print(f"ID: {prod[0]} | Nombre: {prod[1]} | Precio: ${prod[2]:.2f}")
            print()
        else:
            print("No hay productos registrados.")
    except sqlite3.Error as e:
        print(f"Error al obtener los productos: {e}")
    finally:
        conn.close()

def menu():
    """Controla el menú interactivo del programa."""
    crear_base_y_tabla()
    while True:
        print("----- Menú de Productos -----")
        print("1. Registrar producto")
        print("2. Mostrar productos")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_producto()
        elif opcion == "2":
            mostrar_productos()
        elif opcion == "3":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Intente de nuevo.\n")

if __name__ == "__main__":
    menu()
