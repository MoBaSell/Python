"""3. Un código bancario en formato IBAN en nuestro país está formado por 24 caracteres de los
cuales los dos primeros son letras y los restantes 22 son dígitos númericos comprendidos entre el 0
y el 9. Por ejemplo, el siguiente sería un IBAN válido
ES1234567890123456789012
Es corriente verlos escritos tanto de esta forma, sin espacios, como con diferentes separaciones
para que sea más cómodo. Por ejemplo, los siguientes también serían IBAN válidos:
ES12 3456 7890 1234 5678 9012
ES12 3456 7890 12 3456789012
ES 12 3456 7890 123456789012
Escribe una función que reciba como argumento un nombre de fichero que tendrá un listado de
códigos de este tipo. Algunos serán válidos y otros no. Tu programa debería de mostrar por consola
sólo los válidos. Por ejemplo, si el contenido del fichero codigos.txt recibido fuese este:
ES1234567890123456789012
UK12345678901234567
3312 3456 7890 1234 5678 9012
ES12 3456 7890 12 345678901299999
FR32 5456 7898 22 0456789012
ES 12 3456 7XX0 123456789012
Tu programa debería de dar la siguiente salida en consola:
Códigos correctos en el fichero codigos.txt:
País: ES
DC: 12
Entidad: 3456
Sucursal: 7890
DC cuenta: 12
Número de cuenta: 3456789012
País: FR
DC: 32
Entidad: 5456
Sucursal: 7898
DC cuenta: 22
Número de cuenta: 0456789012
Hay 2 códigos correctos y 4 incorrectos
Como puedes ver, los distintos elementos del código son los dígitos del mismo tal y como aparecen
ordenados en él. Y, como siempre, cuida de que la salida sea igual a la que se muestra aquí"""

def es_iban_valido(codigo):
    codigo = codigo.replace(" ", "")
    return len(codigo) == 24 and codigo[:2].isalpha() and codigo[2:].isdigit()

def procesar_codigos(nombre_fichero):
    correctos = 0
    incorrectos = 0

    print(f"Códigos correctos en el fichero {nombre_fichero}:")

    with open(nombre_fichero, "rt") as f:
        for linea in f:
            codigo = linea.strip()

            if es_iban_valido(codigo):
                mostrar_iban(codigo)
                correctos += 1
            else:
                incorrectos += 1

    print(f"Hay {correctos} códigos correctos y {incorrectos} incorrectos")

def mostrar_iban(codigo):
    c = codigo.replace(" ", "")

    print(f"País: {c[0:2]}")
    print(f"DC: {c[2:4]}")
    print(f"Entidad: {c[4:8]}")
    print(f"Sucursal: {c[8:12]}")
    print(f"DC cuenta: {c[12:14]}")
    print(f"Número de cuenta: {c[14:24]}\n")

procesar_codigos("textos/cuentas.txt")
