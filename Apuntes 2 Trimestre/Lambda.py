#funcion normal
def cuadrado(x):
    return x**2

print(cuadrado(25))

#funcion lambda
cuadradoLambda=lambda x: x**2
print(cuadradoLambda(25))

sumaLambda= lambda x,y,z: x+y+z
print(sumaLambda(1,2,3))

media=lambda *lista: sum(lista)/len(lista)
print(media(3,5,6,8,4,7,9,4))