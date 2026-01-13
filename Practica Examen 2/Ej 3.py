class Vehiculo:
    def __init__(self,matricula,tipo, año):
        self.matricula = matricula
        if tipo.lower() == "coche" or tipo.lower() == "moto":
            self.tipo = tipo
        else:
            self.tipo = "Invalido"
        self.año=año

class Conductor:
    def __init__(self, edad, carnet):
        self.edad = edad
        self.carnet = carnet
def calcularPrecio(dias, vehiculo, conductor):
    precio = 0
    if vehiculo.tipo == "coche":
        if conductor.edad < 25:
            precio = (precio+10)*dias
        if conductor.carnet < 2:
            precio = (precio+15)*dias
    elif vehiculo.tipo == "moto":
        if conductor.edad < 25:
            precio = (precio + 10) * dias
        if conductor.carnet < 2:
            precio = (precio + 15) * dias
    print(f"Vehiculo {vehiculo.matricula} - Precio total: {precio}€")

vehiculo = Vehiculo("984982567", "coche", 1)
conductor = Conductor(22,2)
calcularPrecio(15, vehiculo, conductor)