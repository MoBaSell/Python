import random
dados= int(input("Introduce el numero de dados: "))
intentos=0

tiradas=[]
while (tiradas.count(tiradas[0]) != dados):
    for i in range(dados):
      tiradas.insert(i, random.randint(1, 6))

    intentos = intentos + 1
    print(tiradas)

print("He tenido que lanzar los dados", intentos, "veces para que todos sean iguales")









