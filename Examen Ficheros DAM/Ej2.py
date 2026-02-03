import pickle

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


# --- PARTE A: OBTENER LOS DATOS (REUTILIZANDO EL EJ 1) ---
lista_pokemons = []

try:
    fichero_txt=open("pokemons.txt","rt")

    for linea in fichero_txt:
        # 1. Limpiamos el salto de línea (\n) y espacios sobrantes
        linea = linea.strip()

        if linea!="": # Verificamos que la línea no esté vacía

            # 2. Separamos por ", " tal como indica el enunciado
            datos=linea.split(", ")

            # 1. ¿El primer dato es un número entero?
            # 2. ¿Tiene 5 o 6 campos? (Si tiene menos o más, es errónea)
            if datos[0].isdigit() and (len(datos)==5 or len(datos)==6):

                tipos = ", ".join(datos[4:])
                p = Pokemon(datos[0], datos[1], datos[2], datos[3], tipos)
                lista_pokemons.append(p)

    fichero_txt.close()

    # --- PARTE B: GUARDAR EN BINARIO ---
    # Usamos 'wb' para escritura binaria
    fichero_bin = open("pokemons.bin", "wb")
    pickle.dump(lista_pokemons, fichero_bin)
    fichero_bin.close()
    print("Fichero binario 'pokemons.dat' creado con éxito.\n")

    # --- PARTE C: LEER DEL BINARIO Y MOSTRAR ---
    # Usamos 'rb' para lectura binaria
    fichero_lectura = open("pokemons.bin", "rb")
    pokemons_recuperados = pickle.load(fichero_lectura)
    fichero_lectura.close()

    print("Datos leídos del fichero binario:")
    for poke in pokemons_recuperados:
        poke.mostrar()

except:
    print("Error al manejar el fichero")