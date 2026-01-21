#lectura
from os import write

try:    #Siempre con try catch
    fichero=open("Quijote.txt","rt") #Si usamos r debemos crear el fichero en la misma carpeta del script/en modo a (append) situa el cursor al final

    """
    linea=fichero.readline()
    while linea!="":
        if linea[-1]=='\n':
            print(linea[:-1]) #con :-1 eliminamos el ultimo caracter que es un /n (Salto de linea)
        else:
            print(linea)
        linea=fichero.readline()#lee la cantidad de caracteres que le inidiquemos por linea/si queremos que lea linea completa lo dejamos vacio
    """
    linea = fichero.readline(4) #al poner 4 solo coge 4 caracteres
    while linea != "":
        print(linea)
        linea = fichero.readline(4)
    texto = fichero.read() #lee el fichero
    print(texto)
    texto3 = fichero.readlines() #lee el fichero pero lo devuelve en forma de lista y con cada linea como un elemento
    print(texto3) #sale vacia porque el cursor estaba al final

    fichero.close() #Para cerrar el fichero
except:
    print("Error al manipular el fichero")

#escritura
try:
    fichero = open("Quijote.txt", "wt")
    lista=["En un lugar de La Mancha\nde cuyo nombre\nno quiero acordarme..."]
    fichero.writelines(lista) #escribe las lineas de una lista

    """
    fichero.write("En un lugar de La Mancha\n")
    fichero.write("de cuyo nombre\n")
    fichero.write("no quiero acordarme...\n")
    """



    fichero.close()
except:
    print("Error al manipular el fichero")

#append / añade al final del documento
try:
    fichero = open("Quijote.txt", "at")
    fichero.write("En un lugar de La Mancha\n")
    fichero.write("de cuyo nombre\n")
    fichero.write("no quiero acordarme...\n")


    fichero.close()
except:
    print("Error al manipular el fichero")

#lectura y cursor
try:
    fichero = open("Quijote.txt", "r+")
    print(fichero.readline())
    print("Despues de leer estoy aqui",fichero.tell()) #tell dice la linea
    fichero.seek(fichero.tell()+10) #para moverse 10 posiciones desde mi posicion actual
    print("Despues de moverme estoy aqui", fichero.tell())
    fichero.write(("XXX"))
    print("Despues de escribir estoy aqui", fichero.tell())
    fichero.seek(0) #seek(0) para ir al inicio, seek(0,2) para ir al fin, seek(n) posicion n contando desde el principio
    print("Despues de hacer seek estoy aqui",fichero.tell())

    fichero.close()
except:
    print("Error al manipular el fichero")