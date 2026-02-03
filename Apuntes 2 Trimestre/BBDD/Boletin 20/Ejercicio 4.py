import mysql.connector

try:
    conexion = mysql.connector.connect(user='daw2', password='LaElipa', host='localhost', database='dwes5'    )
    cursor = conexion.cursor()

    # 1. Obtener el último ID
    cursor.execute("SELECT MAX(numero_pokedex) FROM pokemon")
    resultado = cursor.fetchone()[0]

    # Si la tabla está vacía, resultado es None, empezamos en 1
    nuevo_id = 1 if resultado is None else resultado + 1

    # 2. Pedir datos (Convertimos a los tipos correctos)
    nombre = input("Ingrese el nombre: ")
    peso = float(input("Ingrese el peso: "))
    altura = float(input("Ingrese la altura: "))

    # 3. Insertar usando parámetros (%) para evitar Inyección SQL
    query = "INSERT INTO pokemon (numero_pokedex, nombre, peso, altura) VALUES (%s, %s, %s, %s)"
    valores = (nuevo_id, nombre, peso, altura)

    cursor.execute(query, valores)
    conexion.commit()

    print(f"Registro insertado con éxito. Nuevo ID: {nuevo_id}")

    cursor.close()
    conexion.close()

except mysql.connector.Error as err:
    print(f"Error de base de datos: {err}")
except ValueError:
    print("Error: El peso y la altura deben ser números.")