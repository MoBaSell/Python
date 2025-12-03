contrasenia=input("Introduce la contraseña: ")
respuesta=input("Introduce la contraseña otra vez: ")
intentos=0
while contrasenia!=respuesta:
    contrasenia=input("Introduce la contraseña correcta:")
    respuesta=input("Introduce la contraseña otra vez:")
    intentos=intentos+1
print("La contraseña es correcta")
print(intentos,"invalidos")