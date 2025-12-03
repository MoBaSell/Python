adivinada = False
frase=str(input("Ingrese la frase: "))

progreso=[]

for c in frase:
    if c == " ":
        progreso.append(" ")
    else:
        progreso.append("*")

while adivinada==False:
    contador = 0
    letra=input("Que letra quieres mantener?")
    veces = frase.count(letra)
    print("La letra", letra, "aparece en", veces, "ocasiones")

    resultado=""
    for n in range(len(frase)):
        if frase[n] == letra:
            resultado += frase[n]
        elif frase[n] == " ":
            resultado += " "
        else:
            resultado += "*"
            contador+=1
    print(resultado)
    if contador ==0:
        adivinada =  True



