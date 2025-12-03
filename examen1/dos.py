import random
texto=input("Introduce una cadena: ")
cadena=[]
for n in texto:
    cadena.append(n)

random.shuffle(cadena)
texto="".join(cadena)

print(texto)