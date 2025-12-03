pin=input("introduce el pin:")


def cifrar(numero):
    linea=""
    cont=0
    texto = str(numero)
    longitud = len(texto)
    if(numero==0):
        ceros=4-longitud
        cifrado = ("XXXXXXXXXX",)
        return cifrado

    for cifra in texto:
        x=10-int(cifra)
        for i in range(0,x):
            linea+="X"
        for l in range(0,int(cifra)):
            linea+="0"

    cifrado = (linea,)
    return cifrado

for n in pin:
    salida=str(cifrar(int(n))).replace("(","").replace(")","").replace("'","").replace(",","")
    print(salida)