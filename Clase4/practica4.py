#Formatee correctamente los textos ingresados en “apellido” y “nombre”, convirtiendo la primera letra de cada palabra a mayúsculas y el resto en minúsculas.

#Asegurarse que el correo electrónico no tenga espacios y contenga solo una “@”.

#Que clasifique por rango etario basándose en su edad (“Niño/a” para los menores de 15 años, “Adolescente” de 15 a 18 y “Adulto/a” para los mayores de 18 años.)

print("Bienvenido al sistema de registro de clientes de TalentoLab.\n")

# Solicitar y validar apellido
while True:
    apellido = input("Ingrese apellido: ").strip().title()
    if apellido:
        break
    else:
        print("El apellido no puede estar vacío. Intente nuevamente.")

# Solicitar y validar nombre
while True:
    nombre = input("Ingrese nombre: ").strip().title()
    if nombre:
        break
    else:
        print("El nombre no puede estar vacío. Intente nuevamente.")

# Validar correo electrónico
while True:
    correo = input("Ingrese correo electrónico: ").strip()
    if correo.count("@") == 1 and " " not in correo:
        pos_arroba = correo.index("@")
        if "." in correo[pos_arroba:]:
            break
        else:
            print("El correo debe contener un '.' después del '@'. Intente nuevamente.")
    else:
        print("Correo inválido. Debe contener un solo '@' y no tener espacios. Intente nuevamente.")

# Validar edad y obtener rango etario
while True:
    try:
        edad = int(input("Ingrese edad: "))
        if edad < 0:
            print("La edad no puede ser negativa. Intente nuevamente.")
            continue
        break
    except ValueError:
        print("Por favor, ingrese un número entero válido para la edad.")

# Determinar rango etario
if edad < 15:
    rango = "Niño/a"
elif 15 <= edad <= 18:
    rango = "Adolescente"
else:
    rango = "Adulto/a"

# Mostrar resultados
print("\n--- Datos del cliente ---")
print(f"Apellido: {apellido}")
print(f"Nombre: {nombre}")
print(f"Correo electrónico: {correo}")
print(f"Rango etario: {rango}")

input("\nPresione Enter para salir...")  # Pausa para evitar cierre inmediato
