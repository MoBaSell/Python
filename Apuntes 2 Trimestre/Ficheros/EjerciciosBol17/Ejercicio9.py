"""
9. Tenemos un fichero llamado alumnos.txt con el siguiente formato:
Pedo, Aitor: 5, 7
Casitas, Armando: 4.5, 9
Lega, Francisco: 8.5, 6.5, 6.3
Ligro, Penélope: 1.1
Cada alumno aparece seguido de una serie de notas (números decimales entre 1 y 10)
Haz un programa en python que lea de ese fichero y nos de una salida en consola listando sólo los
alumnos que tienen todas las calificaciones aprobadas (notas superiores o iguales a 5) y la media
aritmética:
Aitor Pedo – 6
Francisco Lega – 7.1
Donde el número que aparece es la media aritmética de las notas de cada alumno
NOTAS:
 El contenido del fichero alumnos.txt que aparece aquí es sólo un ejemplo. Tu programa
debería de funcionar correctamente con cualquier fichero con ese formato.
 En el fichero, la separación entre el nombre y la nota es de un signo de dos puntos seguido de
un espacio. La separación entre cada dos notas es una coma y un espacio.
 Cada alumno tiene una nota como mínimo, pero el número es variable, indeterminado y
puede ser diferente por cada alumno
 Las medias se redondearán a un decimal máximo
 Suponemos que el formato del fichero es siempre correcto y no tiene errores
"""

f = open("textos/alumnos.txt", "r", encoding="utf-8")
lineas = f.readlines()
f.close()

for linea in lineas:
    linea = linea.strip()
    if not linea:
        continue

    nombre_completo, notas_str = linea.split(": ")
    apellido, nombre = nombre_completo.split(", ")

    notas = [float(n) for n in notas_str.split(", ")]

    if all(n >= 5 for n in notas):
        media = round(sum(notas) / len(notas), 1)
        print(f"{nombre} {apellido} – {media}")

    """
    aprobado = True
    for n in notas:
        if n < 5:
            aprobado = False
            break

    if aprobado:
        media = round(sum(notas) / len(notas), 1)
        print(f"{nombre} {apellido} – {media}")
    """

"""
with open("textos/alumnos.txt", "r", encoding="utf-8") as f:
    lineas = f.readlines()

for linea in lineas:
    linea = linea.strip()
    if not linea:
        continue

    nombre_completo, notas_str = linea.split(": ")
    apellido, nombre = nombre_completo.split(", ")
    
    notas = [float(n) for n in notas_str.split(", ")]

    if all(n >= 5 for n in notas):
        media = round(sum(notas) / len(notas), 1)
        print(f"{nombre} {apellido} – {media}")
"""