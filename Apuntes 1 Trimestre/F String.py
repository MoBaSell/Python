nombre="Mohamed"
edad=21
sueldo=12000.55

print("Mi  nombre %s, tengo %d años y cobro %.2f euros al mes" %(nombre,edad,12000.55)) # s para String, d para años, f para decimales

#f string
print(f"Mi  nombre {nombre}, tengo {edad} años y cobro {sueldo :.2f} euros al mes") #los modificadores van dentro de la variable// .2f para redondear a 2

ratio=0.08394
print(f"Porcentaje: {ratio:.2%}") #el % nos lo convierte a porcentaje

habitantes=712545664
print(f"Población: {habitantes:,} habitantes") #separar las unidades de millar

num1=45
num2=123
print(f"{num1: 4d}\n{num2 :4d}") #les dedica 4 espacios al numero // si ponemos 04d los espacios vacios los llena de ceros
texto="Python"
print(f"***{texto:<20}***") #lo alinea a la izquierda
print(f"***{texto:>20}***") #alinea a la derecha
print(f"***{texto:^20}***") #alinea en el centro
print(f"{num1=}\n{num2=}")

#f string de varias lineas
def devuelveNombre():
    return nombre

ficha=f"""
Ficha del alumno/a:
=================
Nombre: {devuelveNombre()}
Edad: {edad} años
Salario: {sueldo:.2f} {{euros}}
"""
print(ficha)

numero=32
print(f"¿numero es par? {'verdadero' if numero%2==0 else 'falso'}")

print(f"Valoración: {'Alto' if numero > 50 else 'Medio' if numero>25 else 'Bajo'}")