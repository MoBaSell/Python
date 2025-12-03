import random
numero=0
suma=0
while(numero!=666):
    numero=random.randint(1,1000)
    print(numero)
    if(numero!=666):
        suma+=numero
print("Faltan",suma,"dias para que se acabe todo!!")