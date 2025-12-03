numero=input("Ingresa un numero: ")

def toBinario(numero):
    if(len(numero.split("."))==2):
        return -1
    entero=int(numero)
    texto=str(entero)

    if not texto.isdigit():
        return -1
    if entero<0:
        return -1
    if entero>255:
        return -1
    binario=bin(entero)
    return binario[2:]

print(toBinario(numero))