from itertools import count

lista=[20,45,55,29,20,24,14,45,20]
numero=""
total=0
for n in lista:
    veces=lista.count(n)

    if veces>1 and not str(n) in numero:
        print("El número",n,"aparece",veces,"veces")
        numero += str(n)
        total+=1
if total==0:
    print("No hay elementos repetidos")