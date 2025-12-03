dict1={"nombre":"Mohamed","edad":57,"activo":True}
dict2=dict(color="azul",modelo="Caddy",submodelo="Outdoor",motor=2.0)
print(dict1)
print(dict2)
dict3={24:"Charcuteria Manolo",26:"Medias Puri",28:"Bar el Torrezno"}
print(dict3)

print(dict3[26])
print(dict2["modelo"]) #si la clave no existe rompe el programa
print(dict2.get("motor","Esa clave no existe")) #si la clave no existe devuelve none y no rompe el programa/ la segunda parte es para personalizar el error

for elemento in dict3:
    print(elemento)

for elemento in dict3:
    print(elemento, dict3[elemento])

print(list(dict2.keys())) #claves
print(list(dict2.values())) #valores
print(list(dict2.items())) #devuelve una lista de tuplas

#para añadir un elemento y clave nueva / si se pone una clave que ya existe se sustituye el valor
dict3[30]="Peluquería Canina el galgo"
print(list(dict3.items()))

# update para actualizar el diccionario
dict4={"activo":False,"dni":"28777666X","telefono":655321698}
dict1.update(dict4)
print(list(dict1.items()))

#clear para borra todo el diccionario
#dict1.clear()
#print(dict1)

valor= dict1.pop("edad")#elimina elemento por clave y nos devuelve el valor
print(dict1)
print(valor)

valor=dict1.popitem()#elimina el último elemento introducido
print(dict1)
print(valor)
