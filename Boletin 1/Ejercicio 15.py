import random
numero1= int(input("Introduce el primer número: "))
numero2= int(input("Introduce el segundo número: "))

if(numero1>numero2):
    print(random.randint(numero2,numero1))
else:
    print(random.randint(numero1,numero2))