"""14. Haz un programa en Python que permita añadir elementos en el fichero del ejercicio
anterior. Tú programa debería de pedirte un usuario y una contraseña por consola y grabar la
pareja en el fichero con la misma sintaxis indicada. Para mayor seguridad, debería de pedirte la
contraseña dos veces y asegurarse de que ambas son iguales. Si no, no debería de hacer la
grabación y debería de mostrar un mensaje de error por pantalla. Un ejemplo de ejecución
podría ser así:
Introduce el nombre del usuario: manolo
Introduce la contraseña: 123
Vuelve a introducir la contraseña de nuevo: 1234
Las contraseñas no son iguales. No se puede grabar la nueva cuenta
Otro ejemplo:
Introduce el nombre del usuario: manolo
Introduce la contraseña: 123
Vuelve a introducir la contraseña de nuevo: 123
Cuenta de usuario grabada correctamente"""

fichero = "textos/login.txt"

usuario = input("Introduce el nombre del usuario: ").strip()
contrasena1 = input("Introduce la contraseña: ").strip()
contrasena2 = input("Vuelve a introducir la contraseña de nuevo: ").strip()

if contrasena1 != contrasena2:
    print("Las contraseñas no son iguales. No se puede grabar la nueva cuenta")
else:
    with open(fichero, "at", encoding="utf-8") as f:
        f.write(f"{usuario}:{contrasena1}\n")
    print("Cuenta de usuario grabada correctamente")
