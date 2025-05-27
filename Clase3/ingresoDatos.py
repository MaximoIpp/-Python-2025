#Solicite al cliente o clienta su nombre, apellido, edad y correo electrónico.

#Compruebe que el nombre, el apellido y el correo no estén en blanco, y que la edad sea mayor a 18 años.

#Muestre los datos por la terminal, en el orden que se ingresaron. Si alguno de los datos ingresados no cumple los requisitos, sólo mostrar el texto “ERROR!”.


# Pedir todos los datos primero
nombre = input("Ingrese nombre: ").strip()
apellido = input("Ingrese apellido: ").strip()
edad_input = input("Ingrese edad: ").strip()
correo = input("Ingrese correo electrónico: ").strip()

# Validar nombre
if nombre == "" or nombre.isdigit():
    print("ERROR! El nombre no puede estar vacío ni ser un número.")
else:
    print(f"Nombre: {nombre}")

# Validar apellido
if apellido == "" or apellido.isdigit():
    print("ERROR! El apellido no puede estar vacío ni ser un número.")
else:
    print(f"Apellido: {apellido}")

# Validar edad
try:
    edad = int(edad_input)
    if edad <= 18:
        print("ERROR! La edad debe ser mayor a 18.")
    else:
        print(f"Edad: {edad}")
except ValueError:
    print("ERROR! La edad debe ser un número válido.")

# Validar correo electrónico
if "@" not in correo or correo.startswith("@") or correo.endswith("@"):
    print("ERROR! El correo electrónico no es válido.")
else:
    pos_arroba = correo.index("@")
    if "." not in correo[pos_arroba:]:
        print("ERROR! El correo electrónico no es válido.")
    else:
        print(f"Correo: {correo}")

input("\nPresione Enter para salir...")

