numero=input("Ingresa un numero: ")

def aDecimal(numero):
    entero=int(numero)
    texto=str(entero)

    if not numero.isdigit():
        return -1
    for n in texto:
        if n!='0' and n!='1':
            return -1

    decimal=int(texto,2)
    return decimal

print(aDecimal(numero))