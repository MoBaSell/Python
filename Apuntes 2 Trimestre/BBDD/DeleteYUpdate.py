import mysql.connector
try:
    #Iniciamos la conexion
    conexion=mysql.connector.connect(user='daw2',password='LaElipa',host='localhost',database='dwes5')

    cursor=conexion.cursor()
    query1="update pokemon set nombre='Pokemon Cachas' where nombre='Mewtwo'"
    cursor.execute(query1)
    print(cursor.rowcount,"filas afectadas por el query")
    query2="select * from pokemon"
    cursor.execute(query2)
    for fila in cursor:
        print(fila)

    conexion.commit() #para confirmar los cambios

    cursor.close()
    conexion.close()

except mysql.connector.Error as err:
    print(err)