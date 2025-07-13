def validar_nombre(nombre):
    return bool(nombre.strip())

def validar_apellido(apellido):
    return bool(apellido.strip())

def validar_correo(correo):
    return "@" in correo and correo.strip() != ""

def registrar_cliente():
    print("=== Registro de Cliente ===")
    try:
        nombre = input("Ingrese el nombre: ").strip()
        if not validar_nombre(nombre):
            raise ValueError("El nombre no puede estar vacío.")

        apellido = input("Ingrese el apellido: ").strip()
        if not validar_apellido(apellido):
            raise ValueError("El apellido no puede estar vacío.")

        correo = input("Ingrese el correo electrónico: ").strip()
        if not validar_correo(correo):
            raise ValueError("El correo electrónico no es válido.")

        # Intentar abrir el archivo para escritura en modo append
        try:
            with open("clientes.txt", "a", encoding="utf-8") as archivo:
                archivo.write(f"{nombre},{apellido},{correo}\n")
        except IOError:
            print("\nError: No se pudo guardar el cliente.")
            print("Verifique los permisos del archivo.")
            return

        print("\nCliente registrado exitosamente.")

    except ValueError as ve:
        print(f"\nError de validación: {ve}")

if __name__ == "__main__":
    registrar_cliente()
