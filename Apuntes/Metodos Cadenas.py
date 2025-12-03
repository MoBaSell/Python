texto3 ="Hola"+"mundo"+"cruel"+str(33)
for posicion in range(0,len(texto3)):
    print(posicion,"-",texto3[posicion])

print(texto3.upper())
print(texto3.lower())
print(texto3.swapcase())
print(texto3)
print(texto3.find("3")) #Nos devuelve la posicion
print(texto3.find("mu"))
print(texto3.find("s")) #-1 si no hay
print(texto3.count("o"))#cuenta la cantidad de caracteres que hay

texto="Hola mundo cruel"
print(texto.replace(" ","")) #reemplaza un caracter por otro
print(texto.find("o",2,len(texto)-1)) #se indica por donde se empieza a buscar

print(texto.replace(" ","X"))
print(texto.replace(" ","X",1)) #contador para empezar
