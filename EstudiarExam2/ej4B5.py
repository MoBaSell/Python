def contar_palabras_vocales():
    """Cuenta palabras con 4 o más vocales diferentes (A, E, I, O, U)."""
    cadena = input("Introduce una cadena de texto (frase): ")

    # Se convierte toda la cadena a minúsculas para simplificar la comprobación
    cadena_lower = cadena.lower()

    # Se separan las palabras usando split() para manejar múltiples espacios
    palabras = cadena_lower.split()

    palabras_con_cuatro_vocales = 0

    for palabra in palabras:
        # Se usa un conjunto (set) para almacenar solo las vocales únicas encontradas
        vocales_encontradas = set()
        for letra in palabra:
            if letra in 'aeiou':
                vocales_encontradas.add(letra)

        # Comprobar si el número de vocales diferentes es 4 o más
        if len(vocales_encontradas) >= 4:
            palabras_con_cuatro_vocales += 1

    print(
        f"\nLa frase introducida tiene **{palabras_con_cuatro_vocales}** palabra(s) con cuatro o más vocales diferentes.")


# Ejemplo de prueba: "Crisis constitucional por culpa del murcielago guineoecuatorial" -> 3 (constitucional, murcielago, guineoecuatorial)
# Ejecutar el programa
contar_palabras_vocales()