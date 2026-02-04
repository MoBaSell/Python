"""18. Queremos añadir al fichero del ejercicio anterior un cuarto campo que sea la edad del
trabajador. Tu programa deberá de mostrar el nombre de cada persona del fichero pero no
como aparece en él, sino poniendo antes el nombre y a continuación los apellidos) y
preguntarnos la edad que introduciremos por teclado. Un ejemplo de ejecución partiendo del
fichero anterior sería como sigue:
Demetrio Imedio. ¿Cuál es su edad? 34
Luis Ricardo Borriquero. ¿Cuál es su edad? 46
Francisco Lorín. ¿Cuál es su edad? 24
Rosa Cortada del Rosal. ¿Cuál es su edad? 58
En este caso no habrá que hacer comprobaciones previas del formato del fichero que se
supone correcto, pero si de que lo que se introduce por teclado es un número entero superior o
igual a 18 e inferior a 67 (se trata de un fichero de trabajadores y hay que ser mayor de edad y
no haber cumplido la edad de jubilación ordinaria).
El fichero, una vez añadidos los datos, debería de quedar así:
Imedio, Demetrio;Programador Categoría 2;1599.56;34
Borriquero, Luis Ricardo;Analista;1341.60;46
Lorin, Francisco;Administrativo;1095;24
Cortada del Rosal, Rosa;Administrador de bases de datos;2256.99;58
En este caso el fichero final debe de llamarse igual que el original, así que sólo habrá una
variable con el nombre del único fichero con el que puedes trabajar. Así, por ejemplo
fichero = /home/josemaria/empleados.txt"""

fichero = "textos/origen17.txt"

lineas_actualizadas = []

try:
    with open(fichero, "r", encoding="utf-8") as f:
        lineas = f.readlines()
except FileNotFoundError:
    print(f"Error: el fichero '{fichero}' no existe")
    exit()

for linea in lineas:
    linea = linea.strip()
    if not linea:
        continue
    partes = linea.split(";")
    apellidos_nombre = partes[0]  # "Apellidos, Nombre"
    apellidos, nombre = apellidos_nombre.split(", ")
    nombre_mostrar = f"{nombre} {apellidos}"

    while True:
        edad_input = input(f"{nombre_mostrar}. ¿Cuál es su edad? ").strip()
        if edad_input.isdigit():
            edad = int(edad_input)
            if 18 <= edad <= 66:
                break
        print("Edad inválida. Debe ser un número entre 18 y 66.")

    nueva_linea = linea + f";{edad}"
    lineas_actualizadas.append(nueva_linea)

# Sobrescribir fichero
with open("textos/NewSalida17.txt", "w", encoding="utf-8") as f:
    for l in lineas_actualizadas:
        f.write(l + "\n")
