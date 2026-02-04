"""16. Haz un programa en Python que haga lo siguiente:
- Lea del fichero del ejercicio 11 y convierta las parejas usuario:contraseña en objetos de una
clase
- Grabe los objetos en un fichero binario que se llame login.bin
- Lea del fichero binario que has escrito y muestre el contenido de los objetos por consola
Tú programa debería de funcionar independientemente del número de elementos que haya en
el fichero, tanto a la hora de grabarlo en disco como de leerlo posteriormente.
Ejemplo de ejecución:
Fichero origen: /home/josemaria/login.txt
Fichero destino: login.bin
Número de cuentas encontradas: 2
Listado de cuentas:
Usuario: josemaria
Password: abc123
Fortaleza de la contrase´ña: 2
Usuario: alberto
Password: M4d4g4scar
Fortaleza de la contrase´ña: 4"""

import pickle
from Ejercicio15 import Cuenta

fichero_origen = "textos/login.txt"
cuentas = []

try:
    f = open(fichero_origen, "r")
    lineas = f.readlines()
    f.close()
except FileNotFoundError:
    print(f"Error: el fichero '{fichero_origen}' no existe")
    exit()

for linea in lineas:
    linea = linea.strip()
    if not linea or ":" not in linea:
        continue
    try:
        cuentas.append(Cuenta(linea))
    except ValueError:
        continue

print(f"Número de cuentas encontradas: {len(cuentas)}")

f = open("textos/login.bin", "wb")
pickle.dump(cuentas, f)
f.close()

f = open("textos/login.bin", "rb")
cuentas_leidas = pickle.load(f)
f.close()

print("Listado de cuentas:")
for cuenta in cuentas_leidas:
    cuenta.mostrar()