

print("Bienvenido al sistema financiero de TalentoLab.\n")

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

# Registrar ingresos mensuales durante 6 meses
mes = 1
total_ingresos = 0.0

while mes <= 6:
    ingreso_input = input(f"Ingrese el ingreso del mes {mes}: ").strip()
    try:
        ingreso = float(ingreso_input)
        if ingreso < 0:
            print("Valor no válido. El ingreso debe ser un número positivo. Intente nuevamente.")
            continue
        total_ingresos += ingreso
        mes += 1
    except ValueError:
        print("Valor no válido. Por favor, ingrese un número.")

# Mostrar resultados
print("\n--- Resumen del cliente ---")
print(f"Apellido: {apellido}")
print(f"Nombre: {nombre}")
print(f"Correo electrónico: {correo}")
print(f"Rango etario: {rango}")
print(f"Total ingresos acumulados en 6 meses: ${total_ingresos:,.2f}")

input("\nPresione Enter para salir...")
