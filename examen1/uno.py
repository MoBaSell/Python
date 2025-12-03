numero1=int(input("Introudce el primer numero: "))
numero2=int(input("Introudce el segundo numero: "))
capicuas=[]
total=0

if numero1>numero2:
    mayor=numero1
    menor=numero2
else:
    mayor=numero2
    menor = numero1



for n in range(menor,mayor+1):
    num = ""
    num += str(n)
    longitudMax=len(str(mayor))
    longitudMin = len(str(menor))
    if int(n) < 10 and mayor == menor:
        capicuas.append(n)
        total += 1
    elif int(n) < 10:
        capicuas.append(n)
        total += 1
    elif int(n) < 10 and mayor == menor:
        capicuas.append(n)
        total += 1
    elif len(num) == 2 and num[0] == num[1]:
        capicuas.append(n)
        total += 1
    elif len(num) == 3 and num[0] == num[2]:
        capicuas.append(n)
        total += 1
    #for i in range(longitudMin,longitudMax):


    #else:
    #   print("No hay nungún número capicúa entre",menor,"y",mayor)

resultado=str(capicuas)
resultado=resultado.replace("[","").replace("]","")

print("Numero capicuas entre",menor,"y",mayor,":",resultado)
print("Hay un total de",total,"números capicúas")


