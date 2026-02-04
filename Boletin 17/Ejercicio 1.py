def compararFicheros(fichero1, fichero2):

    fichero=open(f"{fichero1}.txt", "rt")
    texto1=fichero.read()
    fichero.close()

    fichero=open(f"{fichero2}.txt", "rt")
    texto2=fichero.read()
    fichero.close()

    if texto1==texto2:
        return True
    else:
        return False


