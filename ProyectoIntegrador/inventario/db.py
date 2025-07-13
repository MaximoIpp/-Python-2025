import sqlite3
from contextlib import contextmanager

DB_NAME = 'inventario.db'

@contextmanager
def get_connection():
    conn = sqlite3.connect(DB_NAME)
    try:
        yield conn
        conn.commit()
    except sqlite3.Error as e:
        conn.rollback()
        raise e
    finally:
        conn.close()

def crear_base_y_tabla():
    with get_connection() as conn:
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

def insertar_producto(nombre, descripcion, cantidad, precio, categoria):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO productos (nombre, descripcion, cantidad, precio, categoria)
            VALUES (?, ?, ?, ?, ?)
        ''', (nombre, descripcion, cantidad, precio, categoria))

def obtener_productos():
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM productos ORDER BY id")
        return cursor.fetchall()

def actualizar_producto(id_prod, nombre, descripcion, cantidad, precio, categoria):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('''
            UPDATE productos
            SET nombre = ?, descripcion = ?, cantidad = ?, precio = ?, categoria = ?
            WHERE id = ?
        ''', (nombre, descripcion, cantidad, precio, categoria, id_prod))
        return cursor.rowcount

def eliminar_producto(id_prod):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM productos WHERE id = ?", (id_prod,))
        return cursor.rowcount

def buscar_producto_por_id(id_prod):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM productos WHERE id = ?", (id_prod,))
        return cursor.fetchone()

def buscar_producto_por_nombre(nombre):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM productos WHERE nombre LIKE ?", ('%' + nombre + '%',))
        return cursor.fetchall()

def buscar_producto_por_categoria(categoria):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM productos WHERE categoria LIKE ?", ('%' + categoria + '%',))
        return cursor.fetchall()

def productos_cantidad_limite(limite):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM productos WHERE cantidad <= ? ORDER BY cantidad ASC", (limite,))
        return cursor.fetchall()
