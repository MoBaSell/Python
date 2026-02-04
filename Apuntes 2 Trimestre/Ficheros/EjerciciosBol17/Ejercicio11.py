"""11. Tenemos un fichero cuyo formato es el siguiente (pero el contenido puede variar, lógicamente):
1234.5
725.3
pepe
4.37
12
ani33kk
1285.3
Realiza una función que reciba como argumento el nombre del fichero. Tu función debe de leer el
contenido y mostrarnos una salida como esta (para el anterior fichero):
Número de datos válidos: 5
Número de datos inválidos: 2
Mínimo: 4.37
Máximo: 1285.3
Media aritmética: 652.294
Tu función debería de detectar las líneas incorrectas y no tenerlas en cuenta pero informar de ellas
en la salida tal y como ves en el ejemplo anterior. Se considerará incorrecta cualquier línea que no
pueda convertirse a numérica con o sin decimales
La media aritmética debe de expresarse con tres decimales máximo
No olvides tener en cuenta las excepciones que puedan ocasionarse por el trabajo con el fichero
"""

def procesar_fichero(nombre_fichero):
    try:
        f = open(nombre_fichero, "r", encoding="utf-8")
        lineas = f.readlines()
        f.close()
    except FileNotFoundError:
        print(f"Error: el fichero '{nombre_fichero}' no existe.")
        return

    datos_validos = []
    datos_invalidos = 0

    for linea in lineas:
        linea = linea.strip()
        if not linea:
            continue
        try:
            numero = float(linea)
            datos_validos.append(numero)
        except ValueError:
            datos_invalidos += 1

    if datos_validos:
        minimo = min(datos_validos)
        maximo = max(datos_validos)
        media = sum(datos_validos) / len(datos_validos)
        print(f"Número de datos válidos: {len(datos_validos)}")
        print(f"Número de datos inválidos: {datos_invalidos}")
        print(f"Mínimo: {minimo}")
        print(f"Máximo: {maximo}")
        print(f"Media aritmética: {round(media,3)}")
    else:
        print("No hay datos válidos en el fichero.")

procesar_fichero("textos/datos.txt")
