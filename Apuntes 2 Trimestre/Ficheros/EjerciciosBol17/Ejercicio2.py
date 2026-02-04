"""Tenemos un fichero llamado estadisticas.txt. El formato del fichero es el siguiente (pero el
contenido puede variar, lógicamente):
Hombre
1.73
Mujer
1.68
Mujer
1.83
Realiza un programa que lea el contenido de ese fichero y muestre el número de hombres, el
número de mujeres y la altura media (con dos decimales) de todos sin hacer distinción de
sexo.
Por ejemplo, para el fichero del ejemplo anterior, la salida del programa sería esta:
Hombres: 1.
Mujeres: 2.
Estatura media: 1.75
El formato del fichero se supone correcto y comprobado y nunca va dar problemas
"""

def estadisticas():
    hombres = 0
    mujeres = 0
    alturas = []

    with open("textos/estadisticas.txt", "rt") as f:
        lineas = f.readlines()

    for i in range(0, len(lineas), 2):
        sexo = lineas[i].strip()
        altura = float(lineas[i + 1].strip())

        if sexo == "Hombre":
            hombres += 1
        else:
            mujeres += 1

        alturas.append(altura)

    media = sum(alturas) / len(alturas)

    print(f"Hombres: {hombres}.")
    print(f"Mujeres: {mujeres}.")
    print(f"Estatura media: {media:.2f}")

estadisticas()