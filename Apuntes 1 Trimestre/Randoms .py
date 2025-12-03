import random

azar = random.randint(1,6) #incluye ambos numeros, a diferencia del for que no incluye el último
print(azar)
print()

#redondeo
pi = 3.14159
print(round(pi,2))
print(round(pi,3))
print(round(pi,4))
print(pi)

print()
for _ in range(0,5): #se puede poner _ en vez de i
    print(random.randint(1,6))

    mayor=max(34.5,55,67.2,-1.4,44,23)
    print("El mayor es",mayor)
    menor=min(34.5,55,67.2,.14,44,23)
    print("El menor es",menor)