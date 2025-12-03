valida = False
while not valida:
    fraccion = input("Escribe tu fracción: ")
    numeros = fraccion.split("/")

    # Validaciones
    if fraccion.count("/") != 1:
        print("Formato incorrecto! Debe tener exactamente una barra '/'")
    elif fraccion[0] == "/" or fraccion[-1] == "/":
        print("Formato incorrecto! La barra no puede estar al inicio ni al final")
    elif "." in numeros[0] or "." in numeros[1]:
        print("Formato incorrecto! No se permiten decimales")
    elif not numeros[0].isdigit() or not numeros[1].isdigit():
        print("Formato incorrecto! Solo se permiten números enteros")
    elif int(numeros[1]) == 0:
        print("Formato incorrecto! El denominador no puede ser 0")
    else:
        valida = True

# Calcular la fracción
solucion = int(numeros[0]) / int(numeros[1])
print("Solución:", round(solucion, 3))
