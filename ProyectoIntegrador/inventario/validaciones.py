def validar_nombre(nombre):
    return bool(nombre.strip())

def validar_cantidad(cantidad):
    try:
        c = int(cantidad)
        return c >= 0
    except ValueError:
        return False

def validar_precio(precio):
    try:
        p = float(precio)
        return p > 0
    except ValueError:
        return False

def validar_id(id_str):
    return id_str.isdigit()
