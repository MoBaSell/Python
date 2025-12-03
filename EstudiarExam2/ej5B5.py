import random
from collections import Counter


def analizar_numeros_aleatorios():
    """Genera 100 números (1-50) y encuentra el mayor, menor y el más repetido."""

    # 1. Generar los 100 números aleatorios
    numeros = [random.randint(1, 50) for _ in range(100)]

    # 2. Obtener el mayor y el menor (uso directo de funciones max() y min())
    mayor = max(numeros)
    menor = min(numeros)

    # 3. Obtener el que más se repite (uso de Counter de la librería collections)
    # Counter crea un diccionario con {elemento: cuenta}
    conteo = Counter(numeros)

    # most_common(1) devuelve una lista con la tupla (elemento, cuenta) del más repetido
    (mas_repetido, veces) = conteo.most_common(1)[0]

    print("\n**Análisis de 100 Números Aleatorios (1-50)**")
    # print(f"Lista de números generados (muestra): {numeros[:10]}...") # Descomentar para ver una muestra
    print(f"El **mayor** número generado es: **{mayor}**")
    print(f"El **menor** número generado es: **{menor}**")
    print(f"El número que **más veces se repite** es el **{mas_repetido}**, repitiéndose **{veces}** veces.")


# Ejecutar el programa
analizar_numeros_aleatorios()
