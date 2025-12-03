import re
patron=r"[6-8][0-9]{8}"
num1="655111222"
num2="913333656"

#Ninguno devuelve un booleano, devuelven objetos

if re.match(patron, num1): #match solo compara el principio con el patrón
    print("num1 Es un telefono móvil")
else:
    print("num1 No es un teléfono móvil")
if re.match(patron, num2):
    print("num2 Es un telefono móvil")
else:
    print("num2 No es un telefono móvil")
print()

if re.search(patron, num1): #si encuentra algo en la cadena que cumple con el patron lo da como bueno
    print("num1 Es un telefono móvil")
else:
    print("num1 No es un teléfono móvil")
if re.search(patron, num2):
    print("num2 Es un telefono móvil")
else:
    print("num2 No es un telefono móvil")
print()

if re.fullmatch(patron, num1): #tiene que cumplir exactamente con el patron para ser válido
    print("num1 Es un telefono móvil")
else:
    print("num1 No es un teléfono móvil")
if re.fullmatch(patron, num2):
    print("num2 Es un telefono móvil")
else:
    print("num2 No es un telefono móvil")
print()
patron=r"[A-Za-zÑñáéíóúÁÉÍÓÚ]{4,8}" #entre 4 y 8 // ? 1 o 0 , * de 0 a los q quieras, + de 1 a los q quieras
texto="ABRDFGIP"
if re.fullmatch(patron, texto):
    print("Es válido")
else:
    print("No es válido")
print()

#validar matricula
patron=r"[0-9]{4}[\s | - ]?[B-DF-HJ-NPR-TV-Z]{3}"

patron=r"[^579]" #no que va detrás de ^ no es válido
texto="0"

if re.fullmatch(patron, texto):
    print("Es válido")
else:
    print("No es válido")
