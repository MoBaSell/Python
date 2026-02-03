import mysql.connector


class Pokemon:
    def __init__(self, pokedex, nombre, peso, altura, tipo):
        self.pokedex = pokedex
        self.nombre = nombre
        self.peso = peso
        self.altura = altura
        self.tipo = tipo


lista_pokemons = []

# 1. Obtener la lista de objetos
try:
    fichero = open("pokemons.txt", "rt", encoding="utf-8")

    for linea in fichero:
        linea = linea.strip()  # CORRECCIÓN: Usa strip() para limpiar, NO split()
        if linea != "":
            datos = linea.split(", ")
            if datos[0].isdigit() and (len(datos) == 6 or len(datos) == 5):
                tipos = ", ".join(datos[4:])
                lista_pokemons.append(Pokemon(datos[0], datos[1], datos[2], datos[3], tipos))
    fichero.close()
except Exception as e:
    print(f"Error al manipular el fichero: {e}")

# 2. Conexión a la base de datos y grabación
try:
    conexion = mysql.connector.connect(user='root', password='root', host='localhost', port=3307, database='pokemondb')
    cursor = conexion.cursor()

    for p in lista_pokemons:
        # A. Comprobar si el código ya existe
        # Nota: He usado 'numero_pokedex' porque es el nombre que se veía en tu consola
        cursor.execute(f"SELECT numero_pokedex FROM pokemon WHERE numero_pokedex = {p.pokedex}")

        if cursor.fetchone():
            print(f"ADVERTENCIA: El Pokémon #{p.pokedex} ({p.nombre}) ya existe en la BD. Saltando...")
        else:
            # B. Solo insertamos si NO existe (Usamos un else en vez de continue)
            # IMPORTANTE: Los textos como el nombre deben ir entre comillas '{p.nombre}'
            insert = f"INSERT INTO pokemon (numero_pokedex, nombre, peso, altura) VALUES ({p.pokedex}, '{p.nombre}', {p.peso}, {p.altura})"
            cursor.execute(insert)

            # C. Gestionar los tipos
            lista_tipos = p.tipo.split(", ")
            for t_nombre in lista_tipos:
                # El nombre del tipo también necesita comillas '{t_nombre}'
                cursor.execute(f"SELECT id_tipo FROM tipo WHERE nombre = '{t_nombre}'")
                resultado = cursor.fetchone()

                if resultado:
                    id_t = resultado[0]
                    sql_pt = f"INSERT INTO pokemon_tipo (numero_pokedex, id_tipo) VALUES ({p.pokedex}, {id_t})"
                    cursor.execute(sql_pt)

            print(f"Pokémon {p.nombre} insertado correctamente.")

    # Guardamos los cambios y cerramos FUERA del bucle for
    conexion.commit()
    cursor.close()
    conexion.close()
    print("\n>>> Volcado a base de datos finalizado con éxito.")

except mysql.connector.Error as err:
    print(f"Error en la base de datos: {err}")