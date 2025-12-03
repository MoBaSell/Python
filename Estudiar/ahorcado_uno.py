from dataclasses import replace

frase=str(input("Ingrese la frase: "))
letra=input("Que letra quieres mantener?")
for n in range(len(frase)):
    if frase[n]==letra:
        print(letra,end="")
    elif frase[n]==" ":
        print(" ",end="")
    else:
        print("*",end="")

