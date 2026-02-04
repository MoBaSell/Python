"""10. Sabrás, por el módulo de Redes, que las redes de Clase A tienen máscara /8, las clase B
máscara /16 y las clase C /24. Tenemos un fichero llamado redes.txt con el siguiente formato:
192.168.10.0/24
200.30.30.0/24
172.16.0.0/16
11.0.0.0/8
130.20.0.0/16
Haz un programa en Python que lea de ese fichero y nos de una salida en consola listando las redes
clasificadas por tipo de la siguiente forma:
Redes Clase A:
11.0.0.0/8
Redes Clase B:
172.16.0.0/16
130.20.0.0/16
Redes Clase C:
192.168.10.0/24
200.30.30.0/24
NOTAS:
 El contenido del fichero redes.txt que aparece aquí es sólo un ejemplo. Tu programa debería
de funcionar correctamente con cualquier fichero con ese formato.
"""
f = open("textos/redes.txt", "rt")
lineas = f.readlines()
f.close()

clase_a = []
clase_b = []
clase_c = []

for linea in lineas:
    linea = linea.strip()
    if not linea:
        continue

    ip, mascara = linea.split("/")

    if mascara == "8":
        clase_a.append(linea)
    elif mascara == "16":
        clase_b.append(linea)
    elif mascara == "24":
        clase_c.append(linea)

print("Redes Clase A:")
for r in clase_a:
    print(r)

print("Redes Clase B:")
for r in clase_b:
    print(r)

print("Redes Clase C:")
for r in clase_c:
    print(r)
