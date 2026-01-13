"""


Queremos implementar una aplicación para la gestión de un instituto con las siguientes
características:
Las clases con los que trabajaremos son: Profesor, Alumno, Ciclo, Grupo y Módulo
Profesor y Alumno son clases con elementos comunes que se crearan por herencia de otra
clase (abstracta) llamada Persona
Para cada Alumno guardaremos el nombre, el apellido, la edad el ciclo en el que está
matriculado y el grupo en el que se le imparten clases. Tendrá, además, una variable
booleana que se calculará a partir de la edad para saber si es mayor o menor de edad de
forma rápida
Para cada profesor guardaremos el nombre, el apellido, el grupo del que es tutor (podría no
ser de ninguno) y el departamento al que pertenece (que sólo puede ser Informática,
Empresa o Inglés)
Para cada Módulo guardaremos el nombre, si es de primer año o de segundo, el número de
horas lectivas que se imparten a la semana y si es un módulo optativo o no
Por cada ciclo guardaremos el nombre, si es de grado medio o superior y los módulos que se
imparten.
Por último, por cada grupo guardaremos un nombre distintivo (DAM1, por ejemplo), el ciclo,
el curso (primero o segundo), el tutor, el número de alumnos y una lista con los alumnos
matriculados en él)
- Piensa en la estructura de clases necesaria para recrear esto y créala. Añade los
constructores. Los grupos se crearan inicialmente sin alumnos.
- Crea un método para añadir un alumno a un grupo.
- Crea un método para eliminar a un alumno de un grupo
- Crea un método para listar toda la información que tengas de un grupo, incluidos los
módulos que se imparten en el
"""




class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

class Alumno(Persona):
    def __init__(self, nombre, apellido, edad, ciclo=None, grupo=None):
        super().__init__(nombre, apellido)
        self.edad = edad
        self.ciclo = ciclo
        self.grupo = grupo
        self.mayor = edad >= 18  # True si es mayor de edad, False si no

class Profesor(Persona):
    def __init__(self, nombre, apellido, departamento, grupo=None):
        super().__init__(nombre, apellido)
        self.departamento = departamento  # Informática, Empresa, Inglés
        self.grupo = grupo  # Puede ser None si no es tutor

class Modulo:
    def __init__(self, nombre, año, horas, optativo=False):
        self.nombre = nombre
        self.año = año  # 1 o 2
        self.horas = horas
        self.optativo = optativo

class Ciclo:
    def __init__(self, nombre, nivel, modulos=None):
        self.nombre = nombre
        self.nivel = nivel  # "Grado Medio" o "Grado Superior"
        if modulos:
            self.modulos = modulos
        else:
            self.modulos = []

class Grupo:
    def __init__(self, nombre, ciclo, curso, tutor=None):
        self.nombre = nombre  # DAM1, etc.
        self.ciclo = ciclo
        self.curso = curso  # 1 o 2
        self.tutor = tutor
        self.alumnos = []  # Inicialmente vacío

    # Método para añadir alumno
    def añadir_alumno(self, alumno):
        alumno.grupo = self
        self.alumnos.append(alumno)

    # Método para eliminar alumno
    def eliminar_alumno(self, alumno):
        if alumno in self.alumnos:
            self.alumnos.remove(alumno)
            alumno.grupo = None

    # Método para listar toda la información del grupo
    def mostrar_info(self):
        print(f"Grupo: {self.nombre}")
        print(f"Ciclo: {self.ciclo.nombre} ({self.ciclo.nivel})")
        print(f"Curso: {self.curso}")
        print(f"Tutor: {self.tutor.nombre if self.tutor else 'Sin tutor'}")
        print(f"Número de alumnos: {len(self.alumnos)}")
        print("Alumnos:")
        for a in self.alumnos:
            print(f" - {a.nombre} {a.apellido}, {a.edad} años, {'Mayor' if a.mayor else 'Menor'}")
        print("Módulos del ciclo:")
        for m in self.ciclo.modulos:
            print(f" - {m.nombre} ({'Optativo' if m.optativo else 'Obligatorio'}), Año {m.año}, {m.horas}h/semana")

# Crear algunos módulos
m1 = Modulo("Programación", 1, 8, False)
m2 = Modulo("Bases de Datos", 1, 6, False)
m3 = Modulo("Inglés Técnico", 1, 3, True)

# Crear un ciclo
ciclo_daw = Ciclo("DAW", "Grado Superior", [m1, m2, m3])

# Crear un profesor tutor
tutor1 = Profesor("Javier", "Puche", "Informática")

# Crear un grupo
grupo_daw2 = Grupo("DAW2", ciclo_daw, 1, tutor1)

a1 = Alumno("Mohamed", "Bada", 22, ciclo_daw)
a2 = Alumno("Freddy", "De Andrade", 24, ciclo_daw)

grupo_daw2.añadir_alumno(a1)
grupo_daw2.añadir_alumno(a2)

grupo_daw2.mostrar_info()

