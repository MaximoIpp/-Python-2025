"""
Tu tarea es la siguiente:

Crear una lista con los nombres de los y las clientes que vamos a procesar. Algunos nombres pueden estar en blanco, y debemos detectarlo.

Recorrer la lista y mostrar el nombre de cada cliente o clienta, junto con su posición en la lista (por ejemplo, Cliente 1, Cliente 2, etc.). 

Si encuentras a alguien cuyo nombre sea una cadena en blanco, mostrar un mensaje de alerta indicando que ese dato no es válido. 

Para los nombres válidos, convertir cada uno a formato adecuado usando .capitalize(), de modo que siempre tengan la primera letra en mayúscula y el resto en minúscula.
"""

# Lista con nombres de clientes, algunos pueden estar en blanco o contener solo espacios
clientes = ["ana", "", "JUAN", "maria", " ", "Carlos", "lucia"]

# Recorrer la lista con índice para mostrar posición y nombre
for i, nombre in enumerate(clientes, start=1):
    nombre_limpio = nombre.strip()  # Eliminar espacios en blanco antes y después
    if nombre_limpio == "":
        print(f"Cliente {i}: ¡Alerta! Nombre no válido (cadena en blanco).")
    else:
        # Formatear nombre: primera letra mayúscula, resto minúsculas
        nombre_formateado = nombre_limpio.capitalize()
        print(f"Cliente {i}: {nombre_formateado}")
