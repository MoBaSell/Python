def saludo(nombre,despedida):
    return "Hola "+nombre+despedida
nombre="Mohamed"
print(saludo(nombre,", que maricon soy, damelo todo papi"))
print(saludo(nombre,", que te vaya bien"))

def miFuncion(mensaje):
    print(mensaje) #las variables no existen fuera de la funcion a diferencia de los demas bucles

miFuncion("Hola mundo")

def devuelveNumeros():
    return 1, 2, 3
n1, n2, n3= devuelveNumeros()
print(n1, n2, n3, sep="-")

def funcion(valor):
    valor*=5
    print(valor)

n=2
funcion(n)
print(n)

print()
def saludo2(nombre="Rafael",despedida=" Te veo pronto!"): #valores por defecto
    print("Vamos allá")
    return "Hola "+nombre+despedida
nombre="Mohamed"
print(saludo2(nombre, " Que te vaya bien"))
print(saludo2("Antonio"))
print(saludo2(despedida=" Adios,adios", nombre="Luis"))
print()

def muestraProfes(veces,*nombres):
   for _ in range(veces):
     for n in nombres:
         print(n)

muestraProfes(2,"Agustin")
print()
muestraProfes(3,"Jose Maria","Ana","Puche")

def repiteNombre(veces, nombre):
    for _ in range(veces):
        print(nombre,end=" *** ")
    print()

datos=[2,"Pepe"]
datos2=[4,"Luis"]
repiteNombre(*datos) #* para pasar datos empaquetados en listas, conjuntos etc
repiteNombre(*datos2)
repiteNombre(*[3,"Eva"])

