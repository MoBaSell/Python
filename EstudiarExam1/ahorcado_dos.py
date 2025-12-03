frase=str(input("Ingrese la frase: "))
letra=input("Que letra quieres mantener?")
texto=[]

for n in range(len(frase)):
    if frase[n]==letra:
        texto.append(frase[n])
        print(letra,end="")
    elif frase[n]==" ":
        texto.append(frase[n])
        print(" ",end="")
    else:
        texto.append(frase[n])
        print("*",end="")
print()
letra2=input("introduce la letra que quieres contar: ")
veces = frase.count(letra2)
print("La letra",letra2,"aparece en",veces,"ocasiones")

resultado=""
for n in range(len(frase)):
    if frase[n]==letra2 or frase[n]==letra:
        resultado+=frase[n]
    elif frase[n] == " ":
        resultado += " "
    else:
        resultado += "*"

print(resultado)