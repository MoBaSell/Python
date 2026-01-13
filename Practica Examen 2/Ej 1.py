class Libro :
    def __init__(self,ISBN, titulo, autor, publicacion):
        self.ISBN = ISBN
        self.titulo = titulo
        self.autor = autor
        self.publicacion = publicacion
        self.prestado = False


class Biblioteca:
    def __init__(self):
        self.libros={}

    def agregarLibro(self,ISBN, titulo, autor,año):
        if ISBN in self.libros:
            print("Error: ISBN ya existente")
        else:
            libro =Libro(ISBN,titulo,autor,año)
            self.libros[ISBN]=libro
            print(f"Libro '{titulo}' añadido correctamente")
    def prestarLibro(self,ISBN):
        if ISBN in self.libros:
            if self.libros[ISBN].prestado:
                print("Error: EL libro ya está prestado")
            else:
                self.libros[ISBN].prestado = True
                print(f"Libro '{self.libros[ISBN].titulo}' prestado correctamente")
        else:
            print(f"No existe un libro con ISBN '{ISBN}'")
    def mostrarLibrosDisponibles(self):
        cont =0
        for ISBN in self.libros:
            if self.libros[ISBN].prestado == False:
                print(f"Titulo: {self.libros[ISBN].titulo} Autor: {self.libros[ISBN].autor} Publicacion: {self.libros[ISBN].publicacion} ISBN: {self.libros[ISBN].ISBN}")
                cont +=1
        if cont == 0:
            print("No hay libros disponibles")

biblio = Biblioteca()
biblio.agregarLibro("123456789","El Quijote","Cervantes",1985)
biblio.agregarLibro("123456789","El Quijote","Cervantes",1985)
biblio.agregarLibro("854869987","Lazarillo de Tormes","Cervantes",1970)
biblio.prestarLibro("123456789")
biblio.prestarLibro("123456789")
biblio.prestarLibro("12345678")
#biblio.prestarLibro("854869987")
biblio.mostrarLibrosDisponibles()