texto = "Hola mundo"
print(texto[3:8]) #Coge el caracter desde el primer indice hasta el sigueinete
# se incluye el primero pero no el segundo
print(texto[3:])
print(texto[:8])
print(texto[-1]) #ultimo caracter
print(texto[2:-2:2]) #el tercer parámetro indica el salto
print(texto[1::2]) #por ejemplo para mostrar los pares
print(texto[::-1]) #para darle la vuelta a la cadena

texto2 ="Hola"+"mundo"+"cruel"
print(texto2)
print("Hola","mundo","cruel")
print("Hola"+"mundo"+"cruel") # , para espacios y + para concatenar
print("Hola","mundo","cruel",33)
texto3 ="Hola"+"mundo"+"cruel"+str(33) #str pasa una variable o valor a string
print(texto3)

for caracter in texto3:
    print(caracter, end="-")
print("\n",len(texto3)) #devuelve la longitud
for posicion in range(0,len(texto3)):
    print(posicion,"-",texto3[posicion])

