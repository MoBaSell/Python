numero=int(input("Introduce un numero: "))

for n in range(1,numero+1):
    if(numero%n==0):
        print(n)