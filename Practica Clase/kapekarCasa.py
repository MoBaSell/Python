numero=input("introduce un numero")

kapekar=False

def ascendente(numero):
    numAscendente=int(''.join(sorted(str(numero))))
    return numAscendente

def descendente(numero):
    mumDescendente=int(''.join(sorted(str(numero),reverse=True)))
    return mumDescendente



while len(set(numero))!=4 or not numero.isdigit() or len(numero)!=4:
    numero=int(input("introduce un numero de cifras difrentes: "))

numero = int(numero)
intentos=0
print("Pasos para obtener la constante de kaprekar a partir del número",numero)

while not kapekar:
    numAsc=ascendente(numero)
    numDesc=descendente(numero)
    numero=numDesc-numAsc
    intentos+=1

    print(numAsc,"-",numDesc,"=",numero)

    if numero==6174:
        kapekar=True
        print("Constante de kaprekar obtenida con",intentos,"operaciones")




