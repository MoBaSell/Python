class CuentaCorriente:
    __numCuentas=0 #Variable estatica

    def __init__(self, codigo, titular, saldo=5000): #constructor
        self.__codigo = codigo #self equivale a this
        self.__titular = titular
        self.__saldo = saldo
        CuentaCorriente.__numCuentas+=1

    @property #se comporta como un atributo
    def saldo(self): #el metodo se tiene que llamar igual q la variable
        return self.__saldo

    #def setSaldo(self, saldo):
    #    self.__saldo=saldo

    @saldo.setter #para definir el metodo como seter y q se comporte como atributo
    def saldo(self, saldo):
        self.__saldo=saldo

    @classmethod #para metodos
    def getNumCuentas(cls):
        return(cls.__numCuentas)

    @staticmethod #para metodos estaticos, metodos que no vamos a modificar
    def devolverDatosSucursal():
        print("Calle del Pez, 7. 28032. Madrid")

    def __str__(self): #devuelve el objeto en cadena
        txt=str(self.__codigo) + " - "+self.__titular+": "+str(self.__saldo)
        return txt


c1 = CuentaCorriente(234567,"Mohamed Bada Sellami",10000.55)
c2 = CuentaCorriente(234568,titular="Kerin Aguilera")

c2.saldo=59876.44
print(c2.saldo)

print(CuentaCorriente.getNumCuentas())
c2.devolverDatosSucursal()
CuentaCorriente.devolverDatosSucursal() #al ser un metodo estatico es el mismo para todos los objetos

print(c1._CuentaCorriente__saldo) #al ser privado no nos deja acceder a el solo con el nombre


class Alumno: #esto es un registro
    pass

alumno1=Alumno()
alumno1.nombre="Juan"
alumno1.apellidos="Balas"
alumno1.edad=24
alumno1.telefono=63598596

print(c1) #para llamar al metodo str, tambien se puede poner con str(c1)
