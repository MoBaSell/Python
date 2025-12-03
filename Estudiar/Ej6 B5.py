numero=input("Introduce un numero: ")
veces=[]
for n in numero:
    if n in veces:
        veces[n]+=1
    else:
        veces[n]=1
print("el número",numero,"tiene el siguiente recuento de cifras:")
for n in veces:
    print(n,"->",veces[n])