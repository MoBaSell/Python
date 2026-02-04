"""20. Crea una función que reciba un empleado (de la clase que has creado en el ejercicio
anterior) y el nombre de un fichero y te añada el empleado al fichero. La llamada a esta
función debería de ser así:
grabarEmpleado(“/home/josemaria/empleados.bin”, empleado1)
Siendo /home/josemaria/empleados.bin el fichero donde haremos la grabación y empleado1
el nombre del objeto de la clase Empleado que queremos grabar en el.
Las condiciones que debes de cumplir son las siguientes:
El fichero debe de ser binario porque queremos grabar los empleados como objetos
- Puede que el fichero no exista, que exista y esté vacío o que ya tenga empleados grabados en
él. Tú programa debería de ser capaz de resolver cualquiera de esas tres situaciones: Si no
existe, lo creas. Si existe y está vacío escribes en él tu objeto. Si el fichero ya tiene objetos
grabados el nuevo debería de añadirse a los que ya existen.
Tu programa debería, finalmente, volver a abrir el fichero y hacer un listado del nombre, los
apellidos y la edad de todos los empleados que existan grabados en él con este formato:
Demetrio Imedio (34)
Luis Ricardo Borriquero (46)
Francisco Lorín (24)
Rosa Cortada del Rosal (58)
"""
import pickle
from Ejercicio19 import Empleado

def grabarEmpleado(fichero_bin, empleado):
    try:
        f = open(fichero_bin, "rb")
        try:
            empleados = pickle.load(f)
        except EOFError:  # Fichero vacío
            empleados = []
        f.close()
    except FileNotFoundError:  # Fichero no existe
        empleados = []

    empleados.append(empleado)

    f = open(fichero_bin, "wb")
    pickle.dump(empleados, f)
    f.close()

    print("Listado de empleados:")
    for emp in empleados:
        print(f"{emp.nombre} {emp.apellidos} ({emp.edad})")

empleado1 = Empleado("Imedio, Demetrio;Programador Categoría 2;1599.56;34")
empleado2 = Empleado("Borriquero, Luis Ricardo;Analista;1341.60;46")
empleado3 = Empleado("Lorin, Francisco;Administrativo;1095;24")

fichero_bin = "textos/empleados.bin"

grabarEmpleado(fichero_bin, empleado1)
grabarEmpleado(fichero_bin, empleado2)
grabarEmpleado(fichero_bin, empleado3)
