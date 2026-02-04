"""1. Crea una función en python que se llame compararFicheros y que reciba como argumento el
nombre de dos ficheros de texto. La función debería de devolver un valor booleano indicando
si el contenido de ambos ficheros es exactamente el mismo o no."""

#si uso with no tengo que preocuparme de cerrar los ficheros ni errores
def compararFicherosWith(fichero1, fichero2):
    with open(fichero1, "r", encoding="utf-8") as f1, open(fichero2, "r", encoding="utf-8") as f2:
        return f1.read() == f2.read()


def compararFicheros(fichero1, fichero2):
    f1 = None
    f2 = None
    try:
        f1 = open(fichero1, "r", encoding="utf-8")
        f2 = open(fichero2, "r", encoding="utf-8")

        return f1.read() == f2.read()
    finally: #se ejecuta siempre al final
        if f1 is not None:
            f1.close()
        if f2 is not None:
            f2.close()
