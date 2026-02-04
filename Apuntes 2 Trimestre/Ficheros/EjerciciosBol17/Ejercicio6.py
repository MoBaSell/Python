"""6. Escribe un programa usando POO que, tomando el mismo fichero clientes.txt del ejercicio
anterior, tenga una clase que se llame cliente donde guarde la información de los clientes que se
hayan leído del fichero.
Tu clase debería de tener un constructor para crear el objeto que reciba la línea tal y como se lee del
fichero. Así:
cliente01 = Cliente(“Diego Norrea 28222777J”)
Tu clase deberá de contar con atributos separados para el nombre, el apellido y el NIF.
Debes de crear una funcion que se llame mostrar que nos muestre la información del cliente por
consola en el siguiente formato:
28222777J – Norrea, Diego
Por último, usando esta clase como soporte, haz un listado del contenido del fichero por consola
que debería de quedar así:
28222777J – Norrea, Diego
07333888X – Perado, Inés
97221345Y - Imedio , Demetrio
22876345M – Rija, Roberto
12987543C – Tosidad, Rubém
32879563V – Adistancia, Armando
18000777H – Tequilla, Germán
"""

class Cliente:
    def __init__(self, linea):
        nombre, apellido, nif = linea.strip().split()
        self.nombre = nombre
        self.apellido = apellido
        self.nif = nif

    def mostrar(self):
        print(f"{self.nif} – {self.apellido}, {self.nombre}")

def listar_clientes():
    f = open("textos/clientes.txt", "r", encoding="utf-8")
    lineas = f.readlines()
    f.close()

    for linea in lineas:
        cliente = Cliente(linea)
        cliente.mostrar()

def listar_clientes_con_with():
    with open("textos/clientes.txt", "r", encoding="utf-8") as f:
        lineas = f.readlines()

    for linea in lineas:
        cliente = Cliente(linea)
        cliente.mostrar()


listar_clientes()
print()
listar_clientes_con_with()