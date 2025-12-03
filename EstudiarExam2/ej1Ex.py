pin=input("introduce el pin:")

def cifrar(numero):
    linea=""
    if numero==0:
        cifrado = ("XXXXXXXXX0",)
        return cifrado
    for n in range(1,11):
        if n==numero:
            linea+="0"
        else:
            linea+="X"

    cifrado=(linea,)
    return  cifrado

for n in pin:
    print(n)
    salida=str(cifrar(int(n))).replace("(","").replace(")","").replace("'","").replace(",","")
    print(salida)
    print()


