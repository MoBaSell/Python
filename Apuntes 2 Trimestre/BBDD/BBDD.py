import mysql.connector
try:
    #Iniciamos la conexion
    conexion=mysql.connector.connect(user='daw2',password='LaElipa',host='localhost',database='dwes5')

    cursor=conexion.cursor()
    query1="select * from pokemon"
    cursor.execute(query1)
    #metodo 1
    #for fila in cursor:
    #    print(fila)
    #    print(fila[1]) #para la segunda posicion de la tupla

    #metodo 2
    lista=cursor.fetchall()
    print(lista) #te devuelve todos los datos a la vez a diferencia del otro linea a linea
    print("El numero de resultados es ",len(lista)," pokemons") #Para ver la cantidad devuelta
    #metodo 3
    #query2="select nombre, numero_pokedex from pokemon"
    #cursor.execute(query2)
    #for (pokemon,id) in cursor:
    #    print(id,"-",pokemon)

    #Cerramos la conexion
    cursor.close()
    conexion.close()
except mysql.connector.Error as err:
    print(err)
