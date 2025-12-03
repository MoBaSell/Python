conjunto1 = {"Ana","Pedro","Luis","Eva"}
print(conjunto1)
#para pasar a conjunto usamos el set()

for nombre in conjunto1:
    print(nombre)

print(len(conjunto1))
conjunto1.add("Manuel")
conjunto1.add("Manuel")
print(conjunto1)
conjunto1.remove("Ana")
print(conjunto1)
conjunto1.discard("Eustaquio") #si el elemento no esta no da error / elimina elementos
conjunto1.discard("Eva")
print(conjunto1) #pero si esta si lo elimina

print(conjunto1.pop()) #recupera y elimina
print(conjunto1)

conjunto1.clear() #elimina todo el contenido
print(conjunto1) #cuando esta vacio nos aparece set()

profesPrimero={"Natalia","Jose Maria","Pedro","Yago"}
profesSegundo={"Jose Maria","Agustin","Puche","Pedro"}

print(profesPrimero & profesSegundo) #para intersección
print(profesPrimero | profesSegundo) #para union
print(profesPrimero - profesSegundo) #resta los que estan en el otro y deja los que no están
print(profesSegundo - profesPrimero) #lo mismo

#lo mismo pero con métodos
print(profesPrimero.intersection(profesSegundo))
print(profesPrimero.union(profesSegundo))
print(profesSegundo.difference(profesSegundo))
print(profesSegundo.difference(profesPrimero))


