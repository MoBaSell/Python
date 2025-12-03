lista = {"Ana","Verónica","Luis","Rafael"}
for nombre in lista:
    print(nombre)

for i in range(len(lista)):
    print(i,"-",list(lista)[i])

for i, nombre in enumerate(lista):
    print(i,"-",nombre)

#num1 = 4
#num2= num1
#num2*=2
#print(num1)

num1=[4]
num2=num1
num2[0]*=2
print(num1) #sale 8 por num2 referencia a num1

num1=[4]
num2=num1.copy()
num2[0]*=2
print(num1) #sale 4 porque tenemos una copia