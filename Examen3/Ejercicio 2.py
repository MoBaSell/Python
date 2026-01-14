class Libros:
    def __init__(self,ISBN,paginas,titulo,autor,clase):
        self.ISBN=ISBN
        self.paginas=paginas
        self.titulo=titulo
        self.autor=autor
        self.prestado=False
        self.clase=clase
        
class Libro(Libros):
    def __init__(self,ISBN,paginas,titulo,autor,clase,tipo,ejemplares):
        super().__init__(ISBN,paginas,titulo,autor,clase)
        self.tipo=tipo
        self.ejemplares=ejemplares

class Comic(Libros):
    def __init__(self,ISBN,paginas,titulo,autor,clase,color):
        super().__init__(ISBN,paginas,titulo,autor,clase)
        self.color=color


class Biblioteca:
    def __init__(self):
        self.stock={}

    def agregarLibro(self,ISBN,paginas,titulo,autor,clase,color=None,tipo=None,ejemplares=None):
        if clase == "Comic":
            if ISBN in self.stock:
                print(f"No puedo añadir el libro {titulo} El código introducido ({ISBN} se corresponde con un libro diferente ({self.stock[ISBN].autor} - {self.stock[ISBN].titulo})")
            else:
                libro = Comic(ISBN,paginas,titulo,autor,clase,color)
                self.stock[ISBN]=libro
                print("Añadiendo a la biblioteca:")
                print(f"{autor} - {titulo}")
        elif clase == "Libro":
            if ISBN in self.stock:
                self.stock[ISBN].ejemplares+=1
                print("Añadiendo ejemplar a la biblioteca")
                print(f"{autor} - {titulo}")
                print(f"Ahora hay {self.stock[ISBN].ejemplares} ejemplares disponibles")
            else:
                libro = Libro(ISBN, paginas, titulo, autor, clase, tipo,ejemplares)
                self.stock[ISBN] = libro
                print("Añadiendo ejemplar a la biblioteca")
                print(f"{autor} - {titulo}")
                print(f"Ahora hay {ejemplares} ejemplares disponibles")

    def mostrarLibrosDisponibles(self):
        for ISBN in self.stock:
            if self.stock[ISBN].clase=="Comic":
                print(f"({self.stock[ISBN].ISBN}) {self.stock[ISBN].autor} - {self.stock[ISBN].titulo} - {self.stock[ISBN].color}")
            else:
                print(f"({self.stock[ISBN].ISBN}) {self.stock[ISBN].autor} - {self.stock[ISBN].titulo} - {self.stock[ISBN].tipo} - {self.stock[ISBN].ejemplares} ejemplares")



biblio = Biblioteca()
biblio.agregarLibro("75566866","50","Spiderman","Marvel","Comic","Color")
biblio.agregarLibro("54887116","170","Don Quijote","Cervantes","Libro","","Papel",5)
biblio.agregarLibro("78512445","210","Lazarillo de Tormes","Cervantes","Libro","","Digital",20)
biblio.agregarLibro("54887116","170","Don Quijote","Cervantes","Libro","","Papel",5)
biblio.agregarLibro("75566866","50","Spiderman","Marvel","Comic","Color")
biblio.mostrarLibrosDisponibles()