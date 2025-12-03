numero = input("Introduce un numero de 4 cifras difrentes: ")
kaprekar=False

while len(set(numero)) != 4:
    numero = input("Error! Introduce un numero de 4 cifras difrentes: ")

while not numero.isdigit():
    numero = input("Error! Introduce un numero entero: ")

def mayorMenor(numero):
    descendente = ''.join(sorted(numero, reverse=True))
    return int(descendente)

def menorMayor(numero):
    ascendente = ''.join(sorted(numero))
    return int(ascendente)

while kaprekar==False:
    descendente = mayorMenor(numero)
    ascendente = menorMayor(numero)

    numero = descendente - ascendente
    print(descendente,"-",ascendente,"=",numero)
    if numero!=6174:
        kapekar=False
    else:
        kapekar=True




