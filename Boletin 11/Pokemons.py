"""
Queremos implementar una clase para gestionar un juego de Pokemon con las siguientes
características:
- Los atributos base que manejaremos serán código, nombre y tipo
- Sólo trabajaremos con pokemon de primera generación por lo que el código estará entre el
1 y el 151, ambos incluidos
- Los posibles tipos son Normal, Agua, Fuego, Planta, Volador, Lucha, Veneno, Eléctrico,
Tierra, Roca, Psíquico, Hielo, Bicho, Fantasma y Dragón.
- Cada pokemon debe de ser de un tipo, pero podría ser de dos. Nunca más
- No necesitamos setters (ya que un pokemon una vez creado no puede modificar sus
características) pero si getters apropiados para todas ellas
- Además, crearemos una función que se llame evolución que permitirá que un pokemon
evolucione en otro diferente. Para ello si un pokemon puede evolucionar en otro debe de
tener de alguna forma una referencia al pokemon en el que evoluciona.
"""
import random
from enum import Enum

class PokemonTipo(Enum):
    NORMAL = "Normal"
    AGUA = "Agua"
    FUEGO = "Fuego"
    PLANTA = "Planta"
    VOLADOR = "Volador"
    LUCHA = "Lucha"
    VENENO = "Veneno"
    ELECTRICO = "Eléctrico"
    TIERRA = "Tierra"
    ROCA = "Roca"
    PSIQUICO = "Psíquico"
    HIELO = "Hielo"
    BICHO = "Bicho"
    FANTASMA = "Fantasma"
    DRAGON = "Dragón"

class Pokemon:
    def __init__(self,nombre,codigo,tipo1,tipo2=None,evolucion=None):
        if 1 > codigo or codigo > 151: raise ValueError("Código fuera de rango.")
        if not isinstance(tipo1,PokemonTipo): raise ValueError("Tipo no valido.")
        if tipo2 is not None:
            if not isinstance(tipo2, PokemonTipo): raise ValueError("Tipo no valido.")
        self.__nombre = nombre
        self.__codigo = codigo
        self.__tipos = [tipo1] if tipo2 is None else [tipo1, tipo2]
        self.__evolucion = evolucion
        self.__Hp = random.randint(50, 100)

#region Properties
    @property
    def evolucion(self):
        return self.__evolucion
    @property
    def tipos(self):
        return self.__tipos
    @property
    def nombre(self):
        return self.__nombre
    @property
    def codigo(self):
        return self.__codigo
    @property
    def Hp(self):
        return self.__Hp
#endregion

#region Funciones
    def evoluciona(self):
        if self.evolucion is None:   #self.__evolucion==None:
            print("No evoluciono, ya soy todo poderoso")
            return self
        return self.evolucion

    def __str__(self):
        tipos_str = ", ".join(t.value for t in self.tipos)
        return (f"Codigo: {str(self.codigo).zfill(3)}\nNombre: {self.nombre}\nTipo: {tipos_str}\n"
                f"{'' if self.evolucion is None else f"Evolucion: {self.evolucion.nombre}\n"}HP: {self.Hp}\n")

    def ataca(self,adversario):
        if self.checkHp():
            atk=random.randint(25,75)
            print(f"{self.nombre}: Ataco a {adversario.nombre} haciendo {atk} de daño")
            adversario.reciboDaño(atk)

    def reciboDaño(self,daño):
        if self.checkHp():
            self.__Hp=0 if self.Hp-daño<=0 else self.Hp-daño
            if self.Hp == 0:
                print(f"{self.nombre}: He sido derrotado")

    def checkHp(self):
        if self.Hp<=0:
            return False
        return True
    #endregion

Poke3=Pokemon("Charizard",3,tipo1=PokemonTipo.FUEGO,tipo2=PokemonTipo.VOLADOR)
Poke2 = Pokemon("Charmeleon", 2, tipo1=PokemonTipo.FUEGO, evolucion=Poke3)
Poke1=Pokemon("Charmander",1,tipo1=PokemonTipo.FUEGO,evolucion=Poke2)

print(Poke1)
print(Poke2)
print(Poke3)

"""Poke1=Poke1.evoluciona()
print(Poke1)
Poke3=Poke3.evoluciona()
print(Poke3)"""

while Poke1.checkHp() and Poke2.checkHp():
    Poke1.ataca(Poke2)
    Poke2.ataca(Poke1)
print("Combate finalizado")