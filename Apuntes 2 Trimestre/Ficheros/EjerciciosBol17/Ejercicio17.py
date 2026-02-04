"""17. Queremos hacer un programa en Python que revise que la sintaxis de un archivo es
correcta. El fichero debería de tener una estructura como la que sigue:
Imedio, Demetrio;Programador Categoría 2;1599.56
Borriquero, Luis Ricardo;Analista;1341.60
Lorin, Francisco;Administrativo;1095
Cortada del Rosal, Rosa;Administrador de bases de datos;2256.99
- Los elementos están separados por punto y coma.
- El primer elemento son los apellidos (una o varias palabras y sólo puede haber letras)
separados del nombre (también una o varias palabras y sólo puede haber letras) por una coma
y un espacio
- El segundo elemento el puesto de trabajo (una o varias palabras también pero en este caso
puede haber números)
- El tercer y último campo es el salario mensual (un número que puede tener decimales o no)
- Cualquier línea que no cumpla con lo listado anteriormente se considerará errónea
Tú programa debería de leer de un fichero origen y escribir en un fichero destino sólo las líneas
que sean correctas. Las que no sean correctas deberían de listarse por pantalla.
Los ficheros de origen y de destino deberían de aparecer como variables del programa para
que sea mas fácil la corrección. Así, por ejemplo:
origen = /home/josemaria/origen.txt
destino = /home/josemaria/salida.txt"""

from re import match

origen = "textos/origen17.txt"
destino = "textos/salida17.txt"

patron = r"^[A-Za-zÑñáéíóúÁÉÍÓÚ ]+, [A-Za-zÑñáéíóúÁÉÍÓÚ ]+;[A-Za-zÑñáéíóúÁÉÍÓÚ0-9 ]+;[0-9]+(\.[0-9]+)?$"

correctas = []

try:
    with open(origen, "r", encoding="utf-8") as f:
        for linea in f:
            linea = linea.strip()
            if match(patron,linea):
                correctas.append(linea)
            else:
                print(linea)
except FileNotFoundError:
    print(f"Error: el fichero '{origen}' no existe")
    exit()

with open(destino, "w", encoding="utf-8") as f:
    for linea in correctas:
        f.write(linea + "\n")
