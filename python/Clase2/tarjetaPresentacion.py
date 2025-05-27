# ¡Hola!

# En nuestro día a día, interactuamos con muchos clientes, y uno de los pasos iniciales es recopilar y organizar su información básica. 
# Para eso, necesito que desarrolles un pequeño programa en Python que haga lo siguiente:


# Solicite al cliente su nombre, apellido, edad y correo electrónico.

print("Bienvenida a la creación de tu tarjeta de presentación digital.\n")

nombre = input("Ingrese el nombre completo: ").strip().title()
profesion = input("Ingrese su profesión u ocupación: ").strip().title()
empresa = input("Ingrese el nombre de su empresa (o deje en blanco si no aplica): ").strip().title()
correo = input("Ingrese su correo electrónico: ").strip()
telefono = input("Ingrese su número de teléfono: ").strip()

print("\n" + "="*40)
print("       TARJETA DE PRESENTACIÓN")
print("="*40)
print(f"Nombre: {nombre}")
print(f"Profesión: {profesion}")
if empresa:
    print(f"Empresa: {empresa}")
print(f"Correo: {correo}")
print(f"Teléfono: {telefono}")
print("="*40)

input("\nPresione Enter para salir...")  # Pausa para que puedas ver la tarjeta
