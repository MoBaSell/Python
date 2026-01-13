from datetime import date

class Conductor:
    def __init__(self,nombre,nif, nacimiento, carnet, puntos):
        self.nombre=nombre
        self.nif=nif
        self.nacimiento=nacimiento
        self.carnet=carnet
        self.puntos=puntos

class Vehiculo:
    def __init__(self,matricula,venta, conductor):
        self.matricula=matricula
        self.venta=venta
        self.conductor=conductor

class Moto(Vehiculo):
    def __init__(self,matricula, venta,conductor):
        super().__init__(matricula,venta,conductor)

class Coche(Vehiculo):
    def __init__(self,matricula, venta,conductor):
        super().__init__(matricula,venta,conductor)

def años_desde_compra(vehiculo):
    return date.today().year - vehiculo.venta

def seguro_todo_riesgo_coche(coche,conductor):
    años = años_desde_compra(coche)

    if años == 0:
        precio = 400
    elif años == 1:
        precio=500
    elif años == 2:
        precio=700
    else:
        precio=años*250

    #Por puntos
    if conductor.puntos<8:
        precio+=100

    #POr menos de 2 años de carnet
    if conductor.carnet<2:
        precio+=200

    return precio

def seguro_terceros_coche(coche,conductor):
    precio=250

    if conductor.puntos<8:
        precio+=50

    if conductor.carnet<2:
        precio+=75

    return precio

def seguro_terceros_moto(moto,conductor):
    precio=200

    if conductor.puntos<8:
        precio+=25

    if conductor.carnet<2:
        precio+=50

    return precio

# --------------------------
#       PROGRAMA PRINCIPAL
# --------------------------

conductor1 = Conductor("José María Morales", 123456,57, 39, 10)
coche1 = Coche("6310NKB", 2024,conductor1)

print("EJEMPLO 1.")
print(f"Vehículo: coche. Matrícula: {coche1.matricula}. Año de compra: {coche1.venta}")
print(f"Conductor: {coche1.conductor.nombre}. Edad: {coche1.conductor.nacimiento}. Años de carnet: {coche1.conductor.carnet}. Puntos: {coche1.conductor.puntos}")
print("Precio del seguro a terceros:", seguro_terceros_coche(coche1, conductor1), "€")
print("Precio del seguro a todo riesgo:", seguro_todo_riesgo_coche(coche1, conductor1), "€\n")


conductor2 = Conductor("Inés Parado",123456, 18, 1, 8)
moto1 = Moto("6309NXR", 2025, conductor2)

print("EJEMPLO 2.")
print(f"Vehículo: moto. Matrícula: {moto1.matricula}. Año de compra: {moto1.venta}")
print(f"Conductor: {moto1.conductor.nombre}. Edad: {moto1.conductor.nacimiento}. Años de carnet: {moto1.conductor.carnet}. Puntos: {moto1.conductor.puntos}")
print("Precio del seguro a terceros:", seguro_terceros_moto(moto1, conductor2), "€")
print("No se hacen seguros a todo riesgo de motos")
