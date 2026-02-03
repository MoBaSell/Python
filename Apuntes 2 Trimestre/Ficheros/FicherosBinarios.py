import pickle

class Persona:
    def __init__(self,nomrbe):
        self.__nombre=nomrbe
    @property
    def nombre(self):
        return self.__nombre

persona1 = Persona("Jose María")
persona2 = Persona("Mohamed")

try:
    fichero = open("binario.bin", "wb")
    #pickle.dump(persona1,fichero) #buelca el contenido en el fichero
    #pickle.dump(persona2,fichero)
    lista=[]
    lista.append(persona1)
    lista.append(persona2)
    pickle.dump(lista,fichero)

    fichero.close()

    fichero = open("binario.bin", "rb")
    l = pickle.load(fichero) #carga el contenido del fichero
    for elemento in l:
        print(elemento.nombre)

    fichero.close()
except:
    print("Error al manipular el fichero")