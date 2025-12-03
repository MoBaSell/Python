import random

dados= int(input("Introduce el numero de dados: "))
caras= int(input("Introduce el numero de caras: "))
while caras%2!=0:
    caras= int(input("Introduce el numero de caras par: "))

for n in range(1,dados+1):
    tirada=random.randint(1,caras)
    print("Dado",n,":",tirada)
