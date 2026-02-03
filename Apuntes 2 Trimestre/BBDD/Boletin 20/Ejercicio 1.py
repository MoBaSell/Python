import mysql.connector
try:
    conexion=mysql.connector.connect(user='daw2',password='LaElipa',host='localhost',database='dwes5')
    cursor = conexion.cursor()
    query1 = "select nombre from pokemon where altura>1.5"
    cursor.execute(query1)

    for fila in cursor:
        print(fila)


    cursor.close()
    conexion.close()

except mysql.connector.Error as err:
    print(err)