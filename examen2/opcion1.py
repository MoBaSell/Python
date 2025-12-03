pin=input("introduce el pin:")



def cifrar(numero):
    linea=""
    lista=[]
    cont=0
    texto = str(numero)
    longitud = len(texto)
    if(longitud<4):
        ceros=4-longitud
        for a in range(0,ceros):
            texto+="0"
        texto=texto[::-1]
    for cifra in texto:
        linea = ""

        if cifra=='0':
            cifrado = ("XXXXXXXXXX",)
            return cifrado
        x=10-int(cifra)
        for i in range(0,x):
            linea+="X"
        for l in range(0,int(cifra)):
            linea+="0"
        lista+=linea
    lista.replace("(","").replace(")","").replace("'","").replace(",","")
    cifrado=(lista,)

    return  cifrado

salida=str(cifrar(int(pin)))
print(salida)
