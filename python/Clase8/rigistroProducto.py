def registrar_productos():
    productos = {}
    while True:
        producto = input("Ingrese el nombre del producto (o 'fin' para terminar): ")
        if producto.lower() == 'fin':
            break
        try:
            precio = float(input(f"Ingrese el precio de {producto}: "))
        except ValueError:
            print("Precio inválido, por favor ingrese un número.")
            continue
        productos[producto] = precio
        print("\nContenido actual del diccionario de productos:")
        for p, pr in productos.items():
            print(f"- {p}: ${pr:.2f}")
        print()  # Línea en blanco para mejor lectura

    return productos

# Ejecución del programa
if __name__ == "__main__":
    registrar_productos()
    input("\nPresioná Enter para salir...")  # Pausa para evitar que la ventana se cierre

