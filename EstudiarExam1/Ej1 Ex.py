import random
numero=int(input("Escribe un número:"))

while numero<10:
    print("El numero debe ser mayor a 10")
    numero = int(input("Escribe un número:"))

aleatorio=0
numeros=[]
for n in range(5):
    aleatorio=random.randint(1,numero)
    while numeros.count(aleatorio)>=1 or aleatorio%2!=0:
        aleatorio=random.randint(1,numero)
    numeros.append(aleatorio)

print("5 números pares aleatorios y diferentes comprendidos entre el 1 y el",numero,":")

for n in range(len(numeros)):
    print(numeros[n])