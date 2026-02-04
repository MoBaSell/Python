"""15. Haz un programa en Python que convierta las parejas usuario:password en objetos de una
clase Consideraciones a tener en cuenta:
- El constructor de la clase debe de recibir como argumento una línea con el usuario y la
contraseña con el mismo formato que en el ejercicio 1 (“josemaria:abc123”, por ejemplo). No
tiene que leerla del fichero ni del teclado. Por lo demás, define la clase de la forma mas
apropiada que veas para lo que tienes que hacer.
- Crea una funcion que nos de una valoración de la solidez de la contraseña teniendo en cuenta
su longitud y los tipos de caracteres que usa con la siguiente pauta.
Tú funcion dará una puntuación de la contraseña en función de lo siguiente:
Contraseña de mas de 8 caracteres +1
Contraseña que incluye letras (ya sean mayúsculas o minúsculas) +1
Contraseña que incluye mayúsculas y minúsculas simultaneamente +1
Contraseña que incluye números +1
Contraseña que incluye otros signos + 1
La salida por consola de esta funcion debería de ser así:
Usuario: josemaria
Password: abc123
Fortaleza de la contrase´ña: 2
Otro ejemplo:
Usuario: alberto
Password: M4d4g4scar
Fortaleza de la contrase´ña: 4"""

import re

class Cuenta:
    def __init__(self, linea):
        if ":" not in linea:
            raise ValueError("Formato incorrecto, debe contener ':'")
        usuario, password = linea.split(":", 1)
        self.usuario = usuario
        self.password = password

    def fortaleza(self):
        score = 0
        pw = self.password

        if len(pw) > 8:
            score += 1

        if any(c.isalpha() for c in pw):
            score += 1

        if any(c.islower() for c in pw) and any(c.isupper() for c in pw):
            score += 1

        if any(c.isdigit() for c in pw):
            score += 1

        if re.search(r"[^a-zA-Z0-9]", pw):
            score += 1

        return score

    def mostrar(self):
        """Muestra usuario, password y fortaleza"""
        print(f"Usuario: {self.usuario}")
        print(f"Password: {self.password}")
        print(f"Fortaleza de la contraseña: {self.fortaleza()}\n")

#aqui deberia haber usado los ficheros
lineas = [
    "josemaria:abc123",
    "alberto:M4d4g4scar.",
    "sara:Romeo1!",
    "juan:12345678",
]

for linea in lineas:
    cuenta = Cuenta(linea)
    cuenta.mostrar()
