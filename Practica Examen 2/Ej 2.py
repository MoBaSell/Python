class Alumno:
    def __init__(self,DNI, nombre,curso,media):
        self.DNI = DNI
        self.nombre = nombre
        self.curso = curso
        self.media = media
    def getNombre(self):
        return self.nombre
    def getMedia(self):
        return  self.media
    def getDNI(self):
        return self.DNI
alumnos={}

def agregarAlumno(DNI,nombre,curso,media):
    if DNI in alumnos:
        print("Error: Alumno con DNI duplicado")
    elif media > 10 or media < 1:
        print("Error: Nota inválida")
    else:
        alumno=Alumno(DNI,nombre,curso,media)
        alumnos[DNI]=alumno
        print(f"Alumno {nombre} con DNI {DNI} agregada correctamente")

def mostrarAprobados():
    cont =0
    for alumno in alumnos.values():
        if alumno.getMedia() >= 5:
            cont += 1
            print(f"[{alumno.getDNI()}] {alumno.getNombre()} - Nota: {alumno.getMedia()}")
    if cont == 0:
        print("No hay alumnos aprobados")
def eliminarAlumno(DNI):
    if DNI in alumnos:
        print("Alumno eliminado correctamente")
        del alumnos[DNI]
    else:
        print("Error: Alumno no encontrado")


agregarAlumno("45556554","Moha","Daw 2",8)
mostrarAprobados()
eliminarAlumno("984982567")
eliminarAlumno("45556554")
