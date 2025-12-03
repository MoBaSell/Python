import random

dados=int(input("Ingrese la cantidad de dados: "))
contador=0
igual=False
estadistica=[0,0,0,0,0,0]

while igual==False:
    tiradas=[]
    contador+=1
    for n in range(dados):
        valor=random.randint(1,8)
        if valor==7 or valor==8:
            tiradas.append(6)
            estadistica[6 - 1] += 1
        else:
            tiradas.append(valor)
            estadistica[valor-1]+=1

    if tiradas.count(tiradas[0]) == dados:
        igual=True

    resultado=str(tiradas)
    resultado=resultado.replace("[","")
    resultado=resultado.replace("]","")
    resultado=resultado.replace(",","-")
    print(resultado)
totalDados=contador*dados

print("El número 1 ha salido el",round(estadistica[0]*100/totalDados,2),"de las veces")
print("El número 2 ha salido el",round(estadistica[1]*100/totalDados,2),"de las veces")
print("El número 3 ha salido el",round(estadistica[2]*100/totalDados,2),"de las veces")
print("El número 4 ha salido el",round(estadistica[3]*100/totalDados,2),"de las veces")
print("El número 5 ha salido el",round(estadistica[4]*100/totalDados,2),"de las veces")
print("El número 6 ha salido el",round(estadistica[5]*100/totalDados,2),"de las veces")


print("He tenido que tirar los dados",contador,"veces para que todos sean iguales")