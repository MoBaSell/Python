def validar_ip(ip):
    partes = ip.split(".")

    # Verificar que tenga 4 partes numéricas
    if len(partes) != 4:
        return None

    try:
        numeros = [int(p) for p in partes]
    except ValueError:
        return None  # Contiene algo que no es número

    # Verificar que todos estén en rango 0–255
    for n in numeros:
        if n < 0 or n > 255:
            return None

    return numeros


def determinar_clase(ip):
    primer_byte = ip[0]

    if 0 <= primer_byte <= 127:
        return "A", "/8"
    elif 128 <= primer_byte <= 191:
        return "B", "/16"
    elif 192 <= primer_byte <= 223:
        return "C", "/24"
    elif 224 <= primer_byte <= 255:
        return "Reservada", None
    else:
        return "No válida", None


# Programa principal
direccion = input("Introduce una dirección IP: ")

ip = validar_ip(direccion)

if ip is None:
    print("Dirección no válida")
else:
    clase, mascara = determinar_clase(ip)
    if clase == "Reservada":
        print("Dirección reservada")
    elif clase == "No válida":
        print("Dirección no válida")
    else:
        print(f"{direccion}{mascara}")
