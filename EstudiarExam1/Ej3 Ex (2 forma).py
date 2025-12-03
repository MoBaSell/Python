texto = input("Escribe un texto: ")
espacios = 0
vocales = 0

for n in texto:
    if n == " ":
        espacios += 1
    elif n in "aeiou":
        vocales += 1

# Eliminar vocales y espacios
nuevo = texto
for c in "aeiou ":
    nuevo = nuevo.replace(c, "")

print("Sin vocales ni espacios:", nuevo)
print("Vocales suprimidas:", vocales)
print("Espacios en blanco suprimidos:", espacios)
