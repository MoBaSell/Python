import random


numeros=[]
for n in range(10):
    aleatorio= random.randint(1,1000)
    numeros.append(aleatorio)
print("10 números entre el 1 y el 1000")
resultado=str(numeros)
resultado=resultado.replace("[","")
resultado=resultado.replace("]","")
print(resultado)

pares=0
impares=0
for n in numeros:
    if n%2==0:
        pares+=1
    else:
        impares+=1
print("He generado",pares,"números pares y",impares,"impares")
mayor=max(numeros)
menor=min(numeros)
print("El número mayor ha sido el",mayor,"y el menor el",menor)