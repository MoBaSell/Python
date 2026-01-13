class CuentaCorriente:
    __numCuentas=0 #Variable estatica

    def __init__(self, codigo, titular, saldo=5000): #constructor
        self.__codigo = codigo #self equivale a this
        self.__titular =[]
        self.__titular.append(titular)
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
        txt=str(self.__codigo) + " - "+str(self.__titular) + ": "+str(self.__saldo)
        return txt
    def __add__(self, segundaCuenta):
        self.__saldo +=segundaCuenta.__saldo
        self.__titular +=segundaCuenta.__titular
        return self

c1 = CuentaCorriente(234567,"Mohamed Bada Sellami",10000.55)
c2 = CuentaCorriente(234568,titular="Kerin Aguilera")

c2.saldo=59876.44
print(c2.saldo)

c1=c1+c2
print(str(c1))