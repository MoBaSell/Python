"""
 Queremos implementar una clase para gestionar nuestra colección de mangas con las
siguientes características:
- Por cada manga guardaremos el nombre del mangaka (autor) el título de la colección (en
japonés, obligatorio y en español, opcional), el género prinicpal (shonen, shojo, seinen, josei,
kodomo, yuri, spokon, isekai y hentai) y el último número publicado en la colección. Crea
getters para todos ellos y setter para el título en castellano (por si originalmente no lo
sabemos y luego lo queremos añadir) y para el número por el que va la colección.
- Queremos, además, poder actualizar los números que tenemos y saber que números nos
faltan. Para ello crearemos dos métodos: uno que nos permitirá introducir los números que
vamos comprando (permitiendo una entrada variable de argumentos para cuando
compramos mas de uno a la vez) y otro que nos diga que números nos faltan para completar
la colección.
- Si cuando introducimos los números que compramos resulta que ya tenemos alguno de
ellos repetido debería de advertirnos
- También necesitaremos una funcion que nos permita eliminar un número (lo hemos perdido,
etc.). Si tratamos de eliminar un número que no tenemos debería de advertírsenos
"""
from enum import Enum

class MangaGenero(Enum):
    shonen = "Shonen"
    shojo = "Shojo"
    seinen = "Seinen"
    josei = "Josei"
    kodomo = "Kodomo"
    yuri = "Yuri"
    spokon = "Spokon"
    isekai = "Isekai"
    hentai = "Hentai"

class ColeccionManga:
    def __init__(self, autor, titulo, genero, ultimaPublicacion, *tomos, tituloCastellano=None):
        if not isinstance(genero, MangaGenero): raise ValueError("Genero no válido.")

        self.__autor = autor
        self.__titulo = titulo
        self.__genero = genero
        self.__ultimaPublicacion = ultimaPublicacion
        self.__tituloCastellano = tituloCastellano
        self.__tomos = list(set(tomos))  # evitamos duplicados iniciales
        self.__tomos.sort()

    # region Properties
    @property
    def autor(self):
        return self.__autor

    @property
    def genero(self):
        return self.__genero

    @property
    def titulo(self):
        return self.__titulo

    @property
    def tomos(self):
        return self.__tomos.copy()

    @property
    def ultimaPublicacion(self):
        return self.__ultimaPublicacion
    @ultimaPublicacion.setter
    def ultimaPublicacion(self, valor):
        if valor < 1:
            raise ValueError("La última publicación debe ser mayor que 0")
        self.__ultimaPublicacion = valor

    @property
    def tituloCastellano(self):
        return self.__tituloCastellano
    @tituloCastellano.setter
    def tituloCastellano(self, valor):
        self.__tituloCastellano = valor
    # endregion

    # region Funciones
    def agregarAColeccion(self, *numeros):
        for numero in numeros:
            if numero in self.tomos:
                print(f"El tomo {numero} ya está en la colección.")
                continue
            if numero > len(self.tomos) or numero < 0:
                print(f"El tomo {numero} no está en el rango de la colección.")
                continue
            self.tomos.append(numero)

        self.tomos.sort()

    def cuantosFaltanParaCompletar(self):
        faltantes = []
        for i in range(1, self.__ultimaPublicacion + 1):
            if i not in self.__tomos:
                faltantes.append(i)
        return faltantes

    def eliminarDeColeccion(self, numero):
        if numero not in self.__tomos:
            print(f"El tomo {numero} no está en la colección.")
        else:
            self.__tomos.remove(numero)
    # endregion

manga = ColeccionManga("Junji Ito", "Uzumaki", MangaGenero.seinen, 6, 1, 2, 4)

manga.agregarAColeccion(3, 4)

print(manga.cuantosFaltanParaCompletar())

manga.eliminarDeColeccion(2)
manga.eliminarDeColeccion(10)

print(manga.tomos)
