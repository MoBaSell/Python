"""12. Queremos hacer un programa en python que sirva para evaluar los resultados de un test. El
fichero manejará dos ficheros: uno llamado soluciones.txt y otro llamado respuestas.txt
El fichero llamado soluciones.txt tiene esta estructura:
A, C, C, D, B, A, D, A, B, A
Como ves, son los resultados de un examen de 10 preguntas tipo test. Las opciones válidas son A,
B, C o D y ninguna otra y deben de aparecer como aquí arriba: en mayúsculas y separadas por un
espacio y una coma. Si el fichero de soluciones no es correcto de dará un mensaje en consola y no
se hará nada mas.
El fichero llamado respuestas.txt tendrá la siguiente estructura:
Claudia Pasón: A, C, C, D, A, A, C, A, B, A
Germán Tequilla C, B, C, A, B, D, C, A B
Alfonso Litario: A, B, C, D, B, A, D, A, B, A
Como ves, hay una linea por cada examinado. Despues del nombre hay dos puntos y un espacio y
por último las respuestas al test también separadas por coma y espacio. Si alguna línea no es
correcta no se tendrá en cuenta a la hora de procesar el fichero y se ignorará, pero si se verán las
demás. En el anterior ejemplo la línea 2, por ejemplo, es errónea
Tu programa debería de mostrar las notas de las líneas correctas de esta forma:
Claudia Pasón: 7.6
Alfonso Litario: 8.8
Para obtener la nota de cada examinado se suma 1 por cada respuesta correcta y se resta 0,2 por
cada respuesta incorrecta. La nota se expresará con dos decimales máximo
"""
#Soluciones
with open("textos/soluciones.txt", "rt") as f:
    sol_linea = f.readline().strip()

soluciones = [r.strip() for r in sol_linea.split(",")]
if len(soluciones) != 10 or not all(r in "ABCD" for r in soluciones):
    print("Error: el fichero soluciones.txt no tiene el formato correcto.")
    exit()

#Respuestas
with open("textos/respuestas.txt", "r", encoding="utf-8") as f:
    lineas = f.readlines()

for linea in lineas:
    linea = linea.strip()
    if not linea:
        continue
    if ": " not in linea:
        continue  # Línea incorrecta

    nombre, resp_str = linea.split(": ", 1)
    respuestas = [r.strip() for r in resp_str.split(",")]
    if len(respuestas) != 10 or not all(r in "ABCD" for r in respuestas):
        continue  # Línea incorrecta

    nota = 0
    #Esto es lo mismo que lo de abajo
    """for sol, resp in zip(soluciones, respuestas):
        if resp == sol:
            nota += 1
        else:
            nota -= 0.2"""

    for i in range(len(soluciones)):
        if respuestas[i] == soluciones[i]:
            nota += 1
        else:
            nota -= 0.2

    print(f"{nombre}: {round(nota,2)}")
