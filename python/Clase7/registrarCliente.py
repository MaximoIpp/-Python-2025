"""
Ejercicio Práctico - Registro de nombres de clientes y clientas

En TalentoLab necesitamos llevar un registro ordenado de los nombres de clientes y clientas que se van incorporando.

Tu tarea es escribir un programa en Python que haga lo siguiente:

- Solicite los nombres de los y las clientes uno por uno y valide que cada nombre no esté vacío.
  Si se deja el campo vacío, mostrar un mensaje de advertencia y volver a pedir el nombre.

- Guarde cada nombre válido en una lista, asegurándote de agregarlo con el método .append().

- Permití que se finalice la carga de nombres escribiendo la palabra "fin".

- Una vez finalizada la carga, ordená alfabéticamente los nombres en la lista y mostrá la lista ordenada utilizando un bucle for.
"""

# Lista para almacenar los nombres de clientes
nombres_clientes = []

print("Ingrese los nombres de los clientes. Escriba 'fin' para terminar la carga.\n")

while True:
    nombre = input("Ingrese un nombre: ").strip()
    
    # Verificar si el usuario quiere finalizar la carga
    if nombre.lower() == "fin":
        break
    
    # Validar que el nombre no esté vacío
    if nombre == "":
        print("¡Advertencia! El nombre no puede estar vacío. Intente nuevamente.")
        continue
    
    # Agregar el nombre válido a la lista
    nombres_clientes.append(nombre)

# Ordenar la lista alfabéticamente
nombres_clientes.sort()

# Mostrar la lista ordenada
print("\nLista ordenada de clientes:")
for i, nombre in enumerate(nombres_clientes, start=1):
    print(f"{i}. {nombre}")
