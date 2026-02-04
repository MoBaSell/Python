"""7. Te ha contratado la policía nacional para que hagas un programa que permita ver si un ciudadano
tiene ficha por delitos previos y mostrar los resultados. El archivo de la policía se llama
delincuentes.txt y tiene este formato:
- Diego Norrea, 35
Robo con violencia
- Demetrio Imedio, 53
Acoso laboral
Evasión de impuestos
Corrupción
- Inés Perado, 48
Hurto
Extorsión
Como ves, los nombres de los delincuentes siempre empiezan por un guión y un espacio en blanco y
terminan con una coma y su edad. A continuación aparecen los delitos cometidos uno por línea
Tu programa debería de pedir por teclado el nombre de un sospechoso y decir si tiene o no
antecedentes. Por ejemplo, en el caso de alguien sin antecedentes:
Introduce el nombre del ciudadano: Ricardo Borriquero
Sin antecedentes penales
En el caso de tener antecedentes debería de listarlos de la siguiente forma:
Introduce el nombre del ciudadano: Ines Perado
Edad: 48 años
Antecedentes penales:
Hurto
Extorsión
NOTA: Piensa que no sabes cuantos antecedentes puede tener el individuo pero que si está en el
fichero debe de tener al menos uno"""

class Delincuente:
    def __init__(self, nombre, edad, delitos):
        self.nombre = nombre
        self.edad = edad
        self.delitos = delitos

    def mostrar(self):
        print(f"Edad: {self.edad} años")
        print("Antecedentes penales:")
        for delito in self.delitos:
            print(delito)

def cargar_delincuentes_sin_with():
    f = open("textos/delincuentes.txt", "r", encoding="utf-8")
    lineas = f.readlines()
    f.close()

    delincuentes = []
    i = 0
    while i < len(lineas):
        linea = lineas[i].strip()
        if linea.startswith("- "):
            # Extraer nombre y edad
            parte = linea[2:].split(",")
            nombre = parte[0].strip()
            edad = int(parte[1].strip())
            delitos = []
            i += 1
            while i < len(lineas) and not lineas[i].startswith("- "):
                delitos.append(lineas[i].strip())
                i += 1
            delincuentes.append(Delincuente(nombre, edad, delitos))
        else:
            i += 1
    return delincuentes

def cargar_delincuentes_con_with():
    delincuentes = []
    with open("textos/delincuentes.txt", "r", encoding="utf-8") as f:
        lineas = f.readlines()

    i = 0
    while i < len(lineas):
        linea = lineas[i].strip()
        if linea.startswith("- "):
            parte = linea[2:].split(",")
            nombre = parte[0].strip()
            edad = int(parte[1].strip())
            delitos = []
            i += 1
            while i < len(lineas) and not lineas[i].startswith("- "):
                delitos.append(lineas[i].strip())
                i += 1
            delincuentes.append(Delincuente(nombre, edad, delitos))
        else:
            i += 1
    return delincuentes

def buscar_sospechoso(delincuentes):
    nombre_buscar = input("Introduce el nombre del ciudadano: ").strip()
    encontrado = False
    for d in delincuentes:
        if d.nombre.lower() == nombre_buscar.lower():
            d.mostrar()
            encontrado = True
            break
    if not encontrado:
        print("Sin antecedentes penales")


delincuentes = cargar_delincuentes_sin_with()
buscar_sospechoso(delincuentes)

# delincuentes = cargar_delincuentes_con_with()
# buscar_sospechoso(delincuentes)