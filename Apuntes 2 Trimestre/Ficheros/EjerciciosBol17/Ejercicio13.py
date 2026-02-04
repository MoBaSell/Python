"""13. Escribe un programa en python para desarrollar una función de login con las siguientes
características:
- Los usuarios y contraseñas válidos estarán almacenados en un fichero con la sintaxis
usuario:contraseña. Suponemos que el fichero es correcto y no habrá errores en su formato.
Tampoco puede haber usuarios repetidos. Un ejemplo de fichero podría ser este:
josemaria:abc
sara:romeo1
alberto:M4d4g4scar+
juan:TOPO
- Los dos puntos que separan usuario y contrasñea son eso, un separador y no pertenece ni a
uno ni a otro. Por motivos evidentes el carácter : no se permite que forme parte ni del usuario
ni de la contraseña. Es decir, en cada línea del fichero debe de aparecer un carácter : como
separador pero no puede aparecer ningún otro.
- La ubicación del fichero de contraseñas se guarda en una variable del programa llamada fichero. Así:
fichero = “/home/josemaria/login.txt”
Tu programa debería de pedir por teclado usuario y contraseña y validar si son correctas
contrastando con lo guardado en el fichero. Si el login es correcto debería de decirlo. Si no lo
es debería de informar del problema encontrado, reconociendo al menos las siguientes
casuísticas:
- fichero inexistente o imposible acceder a él
- fichero vacío
- usuario no encontrado
- contraseña incorrecta"""

fichero = "textos/login.txt"

usuario_input = input("Usuario: ").strip()
contrasena_input = input("Contraseña: ").strip()

try:
    f = open(fichero, "r", encoding="utf-8")
    lineas = f.readlines()
    f.close()
except FileNotFoundError:
    print(f"Error: no se puede acceder al fichero '{fichero}'")
    exit()

if not lineas:
    print(f"Error: el fichero '{fichero}' está vacío")
    exit()

usuarios = {}
for linea in lineas:
    linea = linea.strip()
    if ":" not in linea:
        continue  # Ignorar líneas sin ':'
    usuario, contrasena = linea.split(":", 1)
    usuarios[usuario] = contrasena

if usuario_input not in usuarios:
    print("Usuario no encontrado")
else:
    if usuarios[usuario_input] == contrasena_input:
        print("Login correcto")
    else:
        print("Contraseña incorrecta")
