tupla = (1,2,3) #se definen con parentesis
tupla2 = ("Ana","Pepe","Pedro")
tupla3 = ("Maria",28.5,False)
tupla4 = 4,5,6 #se puede poner sin parentesis
print(tupla)
print(tupla4) #pero a la hora de mostrarla si se muestran los paréntesis
pi=(3.14159,) #para crear una de un solo elemento ponemos una , al final, sino lo detecta como un valor
print(pi)

lista=["elem1","elem2"]
tupla6=tuple(lista) #pasar lista a tupla
print(tupla6)
lista2=list(tupla4) #pasar tupla a lista
print(lista2)
texto=str(tupla6) #pasar tupla a texto
print(texto)

tupla7=(1,2,(1,3,4),5,[1,2,3],7)
print(tupla7)
print(tupla7[1])
print(tupla7[4])
tupla7[4][0]=33 #para modificar lista dentro de tupla
print(tupla7[4])