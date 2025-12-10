from abc import abstractmethod, ABCMeta


class Abstracta(metaclass=ABCMeta):
    def metodoNormal(self):
        print("Hola mundo")

    @abstractmethod
    def metodoAbstracto(self):
        pass

class Hija(Abstracta):
    def metodoAbstracto(self):
        print("Adios Mundo")
elemento = Hija()
elemento.metodoNormal()
elemento.metodoAbstracto()

profesores = ["José María","Natalia","Agustin"]
iterador=iter(profesores)
print(next(iterador))
print(next(iterador))
print(next(iterador)) #sirve para mostrar el siguiente elemento
print(next(iterador,"STOP"))#el segundo parámetro se muestra cuando nos pasamos y q no muestre la excepcion)))

class DiasdelaSemana:
    def __init__(self,dia=0):
        self.dias=["Lunes","Martes","Miercoles","Jueves","Viernes","Sábado","Domingo"]
        self.dia=dia

    def __iter__(self):
        return self

    def __next__(self, stop=None):
        #if self.dia>=len(self.dias):
        #    raise  StopIteration
        dia_actual=self.dias[self.dia]
        if self.dias == 6:
            self.dia=0
        else:
            self.dia+=1
        return  dia_actual

semana = DiasdelaSemana(1)
iterador=iter(semana)
print(next(iterador))
print(next(iterador))
print(next(iterador))
print(next(iterador))
print(next(iterador))
print(next(iterador))
print(next(iterador))
