valida=False
while valida==False:
    fraccion = input("Escribe tu fracción")
    numeros = fraccion.split("/")
    if fraccion.count("/")>1:
        valida=False
        print("Formato incorrecto!")
    elif fraccion[0]=="/" or fraccion[-1]=="/":
        valida=False
        print("Formato incorrecto!")
    elif numeros[0].__contains__(".") or numeros[1].__contains__("."):
        valida=False
        print("Formato incorrecto!")
    elif not numeros[0].isdigit() or not numeros[1].isdigit():
        valida=False
        print("Formato incorrecto!")

    elif int(numeros[1])==0:
        valida = False
        print("Formato incorrecto!")
    else:
        valida=True
solucion=int(numeros[0])/int(numeros[1])
print("Solución:",round(solucion,3))