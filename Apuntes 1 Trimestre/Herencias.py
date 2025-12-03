class Padre:
    def __init__(self):
        self._titulo="Soy la clase Padre" #_Padre__titulo // en las herencias siempre usar un _ osea _titulo para q no de error

    def mostrar(self):
        print("PPP",self._titulo) #_Padre_titulo

class Madre:
    def __init__(self):
        self._titulo="Soy la clase Madre"

    def mostrar(self):
        print("MMM",self._titulo)

class Hijo(Padre, Madre): #da preferencia al q esté más a la izquierda
    def __init__(self):
        self._titulo="Soy la clase Hijo" #_Hijo_titulo

    def mostrar(self, mensaje):
        Madre.mostrar(self) #para que no de preferencia al de la izquierda llamamos al metodo de la clase padre que queremos
        #super().mostrar()
        print(mensaje)

objeto1=Padre()
objeto1.mostrar()

objeto3=Madre()
objeto3.mostrar()

objeto2=Hijo()
objeto2.mostrar("Mensaje Extra")

