"""19. Vamos a hacer ahora a crear un programa con una clase que se llame Empleado y que
contenga los siguientes atributos:
- nombre
- apellidos
- cargo
- salario
- edad
Tú clase recibirá en el constructor una línea como la escrita en el fichero anterior. Así, por
ejemplo:
Empleado(“Imedio, Demetrio;Programador Categoría 2;1599.56;34”)
Deberás, además, crear una función llamada mostrar que muestre la siguiente salida:
Empleado: Demetrio Imedio
Cargo: Programador Categoría 2
Años hasta su jubilación ordinaria: 33
Salario neto anual: 22393.84
Sabiendo que la jubilación ordinaria se produce a los 67 años y que el salario neto anual se
calcula multiplicando el salario mensual por 14 pagas que recibe el empleado al año"""


class Empleado:
    def __init__(self, linea):
        # Separar campos
        partes = linea.strip().split(";")
        apellidos_nombre = partes[0]  # "Apellidos, Nombre"
        self.cargo = partes[1]
        self.salario = float(partes[2])
        self.edad = int(partes[3])

        # Separar nombre y apellidos
        apellidos, nombre = apellidos_nombre.split(", ")
        self.nombre = nombre
        self.apellidos = apellidos

    def mostrar(self):
        print(f"Empleado: {self.nombre} {self.apellidos}")
        print(f"Cargo: {self.cargo}")
        print(f"Años hasta su jubilación ordinaria: {67 - self.edad}")
        print(f"Salario neto anual: {self.salario * 14:.2f}\n")

if __name__ == "__main__": #evita correr esto en mi otro script
    lineas = [
        "Imedio, Demetrio;Programador Categoría 2;1599.56;34",
        "Borriquero, Luis Ricardo;Analista;1341.60;46",
        "Cortada del Rosal, Rosa;Administrador de bases de datos;2256.99;58"
    ]

    for linea in lineas:
        emp = Empleado(linea)
        emp.mostrar()
