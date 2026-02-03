class Pokemon:
    def __init__(self,pokedex,nombre,peso,altura,tipo):
        self.pokedex=pokedex
        self.nombre=nombre
        self.peso=peso
        self.altura=altura
        self.tipo=tipo

    def mostrar(self):
        print(f"#{self.pokedex} - {self.nombre}")
        print(f"Peso: {self.peso} kg")
        print(f"Altura: {self.altura} m")
        print(f"Tipo: {self.tipo}")
        print("-" * 15)

lista_pokemons = []
lineas_erroneas = []

try:
    fichero=open("pokemons.txt","rt")
    lineas=fichero.readlines()

    for linea in lineas:
        # 1. Limpiamos el salto de línea (\n) y espacios sobrantes
        linea = linea.strip()

        if linea!="": # Verificamos que la línea no esté vacía

            # 2. Separamos por ", " tal como indica el enunciado
            datos=linea.split(", ")

            # 1. ¿El primer dato es un número entero?
            # 2. ¿Tiene 5 o 6 campos? (Si tiene menos o más, es errónea)
            if datos[0].isdigit() and (len(datos)==5 or len(datos)==6):
                # Si es correcta, extraemos y guardamos en la lista
                pokedex=datos[0]
                nombre=datos[1]
                peso=datos[2]
                altura=datos[3]
                # 4. Los tipos pueden ser uno o dos.
                # Tomamos todo desde la posición 4 hasta el final y lo unimos.
                tipos_unidos = ", ".join(datos[4:])

                # 5. Creamos el objeto e invocamos el método
                nuevo_pokemon = Pokemon(pokedex, nombre, peso, altura, tipos_unidos)
                lista_pokemons.append(nuevo_pokemon)

            else:
                # Si falla cualquier condición, va a la lista de errores
                lineas_erroneas.append(linea)

    fichero.close()

# --- SALIDA FINAL POR PANTALLA ---
    # Primero mostramos todos los objetos creados
    for p in lista_pokemons:
        p.mostrar()

# Luego mostramos el informe de errores si los hay
    if len(lineas_erroneas) > 0:
        print(f"\n{len(lineas_erroneas)} Líneas erroneas en el fichero:")
        for l in lineas_erroneas:
            print(l)



except:
    print("Error al manejar el fichero")