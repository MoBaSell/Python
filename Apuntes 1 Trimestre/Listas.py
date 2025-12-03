lista1 = [] #primera forma
lista2 = list() #segunda forma
lista3 = [2,4,589,33,1,333,3,44,6,7,333,2]
lista4=["Moha","Alvaro","Eva"]
lista5=[34,"José Maria",False,45.6,2,"Pérez",[1,5,"DAM"]]

for elemento in lista5:
    print(elemento)

for i in range(0, len(lista5)):
    print(i,"-",lista5[i])

print(lista5[6][2]) #mostrar elemetos de la lista que esta en la primera lista

matriz=[[1,2,3],[4,5,6],[7,8,9]] #matriz

print(matriz[2][0])

#lista6=lista3+lista4
#print(lista6)
#lista3.extend(lista4) #en este caso se pierde el valor original de lista 3
#print(lista3)

lista3.append(8) #insertar valor al final
print(lista3)
lista3.insert(1,333) #insertar valor en la posicion indicada
print(lista3)

elemento=lista3.pop(-2) #elimina el ultimo valor de la lista pero se puede recuperar en una variable
# si le pone un numero se elimina el que se encuentra en la posicion
print(elemento)
print(lista3)

#lista4.remove("Eva") #Elimina el elemento indicado
print(lista4)

lista3.sort() #ordena la lista
print(lista3)

lista3.sort(reverse=True) #orden reverso
print(lista3)

if 333 in lista3:
    print("Esta en la lista")
    print("Aparece", lista3.count(333), "veces")
else:
    print("No está en la lista")

texto="Hola Mundo"
lista2=list(texto) #listar cada caracter de una cadena en una lista
print(lista2)

texto2=str(lista3) #str conviete la lista en una cadena de texto
print(texto2)
texto2=texto2.replace("[","")
texto2=texto2.replace("]","")
print(texto2)

vector=matriz[1]
print(vector)

print(lista3[3:]) #desde la posicion 3
print(lista3[:6]) #desde la posicion 6 desde atras
print(lista3[1::2]) #pares
print(lista3[::-1]) #descendiente

