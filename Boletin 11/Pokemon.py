import random


class Pokemon:
    def __init__(self, codigo, nombre, evolucion=None):
        self.__codigo=codigo
        self.__nombre=nombre
        self.__evolucion=evolucion
        self.__pv=random.randint(50,100)

    def ficha(self): #devuelve el objeto en cadena
        print("------------------")
        print(self.__codigo, " - ",self.__nombre)
        print("PV:",self.__pv)
        if self.__evolucion is not None:
            print("Evoluciona en:",self.__evolucion.__nombre)
        else:
            print("Evoluciona en: Ninguno")
        print("------------------")
    def evoluciona(self):
        if self.__evolucion==None:
            evo=self
            print("Este pokemon no sabe evolucionar")
            return self
        else:
           evo=self.__evolucion
        return  evo
    def combateContra(self, contrincante):
        while self.__pv>0 and contrincante.__pv>0:
            danyo=random.randint(25,75)
            if contrincante.__pv <=0:
                print(contrincante.__nombre,"ha sido derrotado")
            else:
                danyo = random.randint(25, 75)
                self.__pv-=danyo
                if self.__pv<=0:
                    print(self.__nombre, "ha sido derrotado")
                else:
                    print("Ninguno de los pokemos ha vencido")

p3= Pokemon(3,"Yvisaur")
p2= Pokemon(2,"Venasaur",p3)
p1 = Pokemon(1,"Bulbasur",p2)

p1.ficha()
p2.ficha()
p3.ficha()
p1=p1.evoluciona()
p3=p3.evoluciona()
p1.ficha()
p3.ficha()
p1.combateContra(p3)