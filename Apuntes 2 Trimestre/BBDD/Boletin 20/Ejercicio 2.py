import mysql.connector
try:
    conexion=mysql.connector.connect(user='daw2',password='LaElipa',host='localhost',database='dwes5')
    cursor = conexion.cursor()
    query1 = "UPDATE pokemon set nombre = UPPER(nombre) where peso>200"
    cursor.execute(query1)

    conexion.commit()

    print("Numero de registros actualizados: ",cursor.rowcount)
    

    cursor.close()
    conexion.close()

except mysql.connector.Error as err:
    print(err)