"""8. Estamos generando un fichero con los nombres de los personajes para un juego de rol y
queremos que estos sean aleatorios. Para ello contamos con dos listas, una de nombres y otra de
apellidos como estas:
nombres=[“Ash”, “Momo”, “Monkey”, “Naruto”, “Nico”, “Ken”,
“Roronoa”, “Touka”]
apellidos=[“Ketchum”, “Ayase”, “D. Luffy”, “Uzumaki”, “Robin”,
“Kaneki”, “Zoro”, “Kirishima”]
Hay, como ves, ocho nombres y ocho apellidos. Es el máximo de personajes que admitirá nuestro
juego. Tu programa debería de pedir por teclado un número entre el 1 y el 8 que serían el número de
personajes que necesitamos para la partida y generar los nombres tomando aleatoriamente un
nombre y un apellido sin repetir nunca ninguno. Por ejemplo así:
Cuantos personajes tendrá tu partida: 4
Personajes:
Momo Uzumaki
Touka Kirishima
Ash Robin
Ken Ayase
Además de generar la salida anterior tu programa debería de crear un fichero que se llame
personajes.txt y escribir en él el nombre de los personajes generados. En el ejemplo anterior tu
fichero personajes.txt tendría este contenido:
Momo Uzumaki
Touka Kirishima
Ash Robin
Ken Ayase
Tu programa debería de detectar que en la entrada por teclado no se meta un número entero o que
este sea inferior a 1 o superior a 8. En todos esos casos que le impedirían funcionar correctamente
debería de mostrar un error en consola y no hacer nada mas."""

import random

nombres = ["Ash", "Momo", "Monkey", "Naruto", "Nico", "Ken", "Roronoa", "Touka"]
apellidos = ["Ketchum", "Ayase", "D. Luffy", "Uzumaki", "Robin", "Kaneki", "Zoro", "Kirishima"]

try:
    num = int(input("Cuantos personajes tendrá tu partida: "))
    if num < 1 or num > 8:
        raise ValueError("Número fuera de rango")
except ValueError:
    print("Error: introduce un número entero entre 1 y 8")
    exit()  # Salir del programa

nombres_aleatorios = random.sample(nombres, num)
apellidos_aleatorios = random.sample(apellidos, num)

personajes = [f"{nombres_aleatorios[i]} {apellidos_aleatorios[i]}" for i in range(num)]

print("Personajes:")
for p in personajes:
    print(p)

f = open("textos/personajes.txt", "w", encoding="utf-8")
for p in personajes:
    f.write(p + "\n")
f.close()
