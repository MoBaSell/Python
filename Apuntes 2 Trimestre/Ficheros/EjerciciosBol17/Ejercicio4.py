"""4. Escribe un programa usando POO que, tomando el mismo fichero codigos.txt del ejercicio 3,
tenga una clase que se llame IBAN donde guarde la información de los códigos IBAN correctos que
se hayan leído del fichero.
Tu clase debería de tener, al menos, un constructor para crear el objeto y una funcion llamado
mostrar para que se visualice la información del código por consola. El constructor recibirá el código
IBAN en formato de cadena de texto. Así:
codigoIBAN01 = Iban(“ES1234567890123456789012”)
Y debería de admitir como argumento de entrada cualquier IBAN válido independientemente de los espacios en blanco tal y como se describe en el anterior ejercicio.
Tu clase deberá de contar con atributos separados para los diferentes elementos del IBAN (pais, dc,
entidad, sucursal, dc_cuenta y num_cuenta). La funcion mostrar, antes mencionado, nos listará los
códigos de forma similar a como se describe en el ejercicio anterior.
En definitiva, tu programa debe de funcionar igual que el ejercicio 3 pero usando POO. Puedes,
si quieres, hacer este ejercicio en lugar del 3 (y tendrás la misma puntuación en ambos) pero no
al revés."""

#Con Exepciones
"""class IBAN:
    def __init__(self, codigo):
        # Quitamos espacios
        self.codigo = codigo.replace(" ", "")

        if not self.es_valido():
            raise ValueError("IBAN no válido")

        # Atributos del IBAN
        self.pais = self.codigo[0:2]
        self.dc = self.codigo[2:4]
        self.entidad = self.codigo[4:8]
        self.sucursal = self.codigo[8:12]
        self.dc_cuenta = self.codigo[12:14]
        self.num_cuenta = self.codigo[14:24]

    def es_valido(self):
        return (
            len(self.codigo) == 24 and
            self.codigo[:2].isalpha() and
            self.codigo[2:].isdigit()
        )

    def mostrar(self):
        print(f"País: {self.pais}")
        print(f"DC: {self.dc}")
        print(f"Entidad: {self.entidad}")
        print(f"Sucursal: {self.sucursal}")
        print(f"DC cuenta: {self.dc_cuenta}")
        print(f"Número de cuenta: {self.num_cuenta}\n")


def procesar_codigos(nombre_fichero):
    correctos = 0
    incorrectos = 0

    print(f"Códigos correctos en el fichero {nombre_fichero}:")

    with open(nombre_fichero, "rt") as f:
        for linea in f:
            codigo = linea.strip()

            try:
                iban = IBAN(codigo)
                iban.mostrar()
                correctos += 1
            except ValueError:
                incorrectos += 1

    print(f"Hay {correctos} códigos correctos y {incorrectos} incorrectos")

"""
class IBAN:
    def __init__(self, codigo):
        self.codigo = codigo.replace(" ", "")

        self.pais = ""
        self.dc = ""
        self.entidad = ""
        self.sucursal = ""
        self.dc_cuenta = ""
        self.num_cuenta = ""

        if self.es_valido():
            self.pais = self.codigo[0:2]
            self.dc = self.codigo[2:4]
            self.entidad = self.codigo[4:8]
            self.sucursal = self.codigo[8:12]
            self.dc_cuenta = self.codigo[12:14]
            self.num_cuenta = self.codigo[14:24]

    def es_valido(self):
        return (
            len(self.codigo) == 24 and
            self.codigo[:2].isalpha() and
            self.codigo[2:].isdigit()
        )

    def mostrar(self):
        print(f"País: {self.pais}")
        print(f"DC: {self.dc}")
        print(f"Entidad: {self.entidad}")
        print(f"Sucursal: {self.sucursal}")
        print(f"DC cuenta: {self.dc_cuenta}")
        print(f"Número de cuenta: {self.num_cuenta}\n")

def procesar_codigos(nombre_fichero):
    correctos = 0
    incorrectos = 0

    print(f"Códigos correctos en el fichero {nombre_fichero}:")

    with open(nombre_fichero, "rt") as f:
        for linea in f:
            codigo = linea.strip()
            iban = IBAN(codigo)

            if iban.es_valido():
                iban.mostrar()
                correctos += 1
            else:
                incorrectos += 1

    print(f"Hay {correctos} códigos correctos y {incorrectos} incorrectos")


procesar_codigos("textos/cuentas.txt")