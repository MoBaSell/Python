print("Hola mundo") #comentario hasta el final de línea
# Esto es un comentario
"""
comentario
en 
bloque
"""
edad=56  #se puede cambiar el tipo de la variable en cualquier momento
print(edad)
texto="Cincuenta y seis"
print(texto)
precio=54.6
acertado= True
MESES_ANNO=12 #no existen las constantes por lo que las marcamos en mayuscula
nuevo=precio * (5 + edad)
print(10/3)
print(acertado)


texto = "hola"
curso=2
ciclo = "DAW"
#print(texto+" "+"Mundo")
print(texto, "Mundo", end=" *** ", sep="-")# end sustituye el salto de linea predeterminado por lo que queramos
                                           # sep para cambiar el separador
print("Bienvenidos todos los de",curso,ciclo)


edad=input("Intoduce tu edad: ")#para leer por teclado
if int(edad) < 18: #tenemos que pasar edad a entero
    print("Eres mayor de edad")
elif edad==18:
    print("Tienes exactamente 18 años")
else:
    print("Eres mayor de edad")

sueldo= float(input("Dime tu sueldo: ")) #float pasa a decimales
if sueldo > 18000.56:
    print("Debes de ser rico")
if edad==100:
    pass #para dejar un bloque o if vacio ponemos un pass
else:
    print("No se si tienes para piso...")

for n in range(0,10):#podemos poner un 10 solo y empieza automaticamente en 0
    print(n)
print("")
for n in range(0,10,2):#el tercer valor inidica el paso o salto
    print(n)
print("")
for n in range(10,0,-1):#para descendiente
    print(n)
print("")
for c in "Hola mundo": #para recorrer una cadena
    print(c)


#bucle while
print("")
print("Bucle while")
i=0
while(i<10):
    print(i)
    i+=1