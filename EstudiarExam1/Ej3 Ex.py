texto=input("Escribe un texto:")
espacios=0
vocales=0
for n in range(len(texto)):
    if texto[n]==" ":
        espacios+=1
    if texto[n]=="a" or texto[n]=="e" or texto[n]=="i" or texto[n]=="o" or texto[n]=="u":
        vocales+=1
nuevo=texto.replace(" ","")
nuevo=nuevo.replace("a","")
nuevo=nuevo.replace("e","")
nuevo=nuevo.replace("i","")
nuevo=nuevo.replace("o","")
nuevo=nuevo.replace("u","")

print("Sin vocales ni espacios:",nuevo)
print("Vocales suprimidas:",vocales)
print("Espacios en blanco suprimidos:",espacios)