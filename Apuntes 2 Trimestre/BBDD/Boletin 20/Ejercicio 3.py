import mysql.connector

try:
    conexion = mysql.connector.connect(user='daw2', password='LaElipa', host='localhost', database='dwes5')
    cursor = conexion.cursor()

    cursor.execute("SELECT MAX(numero_pokedex) FROM pokemon")
    ultimo_id = cursor.fetchone()[0]

    if ultimo_id == None:
        nuevo_id=1
    else:
        nuevo_id=ultimo_id+1


    nombre = input("Ingrese el nombre: ")
    peso = input("Ingrese el peso: ")
    altura = input("Ingrese la altura: ")


    query1 = f"insert into pokemon (numero_pokedex,nombre, peso, altura) values ('{nuevo_id}','{nombre}','{peso}','{altura}')"
    cursor.execute(query1)

    conexion.commit()

    print(f"Registro insertado con éxito. Nuevo ID: {nuevo_id}")
    print(f"Filas afectadas: {cursor.rowcount}")

    cursor.close()
    conexion.close()

except mysql.connector.Error as err:
    print(err)