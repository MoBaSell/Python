from abc import ABC, abstractmethod
from datetime import datetime

# Año actual según el enunciado
ANIO_ACTUAL = 2025


class Conductor:
    def __init__(self, nombre, nif, anio_nacimiento, anio_carnet, puntos):
        self.nombre = nombre
        self.nif = nif
        self.anio_nacimiento = anio_nacimiento
        self.anio_carnet = anio_carnet
        self.puntos = puntos

    @property
    def edad(self):
        return ANIO_ACTUAL - self.anio_nacimiento

    @property
    def años_carnet(self):
        return ANIO_ACTUAL - self.anio_carnet


class Vehiculo(ABC):
    def __init__(self, matricula, anio_venta, conductor, tipo_seguro):
        self.matricula = matricula
        self.anio_venta = anio_venta
        self.conductor = conductor
        self.tipo_seguro = tipo_seguro  # 'todo_riesgo' o 'terceros'

    @property
    def antiguedad(self):
        # El primer año cuenta como año 1 (ej: comprado en 2025 es año 1)
        return (ANIO_ACTUAL - self.anio_venta) + 1

    @abstractmethod
    def calcular_precio_seguro(self):
        pass


class Coche(Vehiculo):
    def calcular_precio_seguro(self):
        precioBase = 0

        if self.tipo_seguro == "todo_riesgo":
            # Lógica año a año
            if self.antiguedad == 1:
                precioBase = 400
            elif self.antiguedad == 2:
                precioBase = 500
            elif self.antiguedad == 3:
                precioBase = 700
            else:
                precioBase = self.antiguedad * 250

            # Plus por puntos
            if self.conductor.puntos < 8:
                precioBase += 100

        elif self.tipo_seguro == "terceros":
            precioBase = 250
            if self.conductor.puntos < 8: precioBase += 100
            if self.conductor.edad < 24: precioBase += 50
            if self.conductor.años_carnet < 2: precioBase += 75

        return precioBase


class Moto(Vehiculo):
    def __init__(self, matricula, anio_venta, conductor):
        # Las motos solo tienen seguro a terceros según el enunciado
        super().__init__(matricula, anio_venta, conductor, "terceros")

    def calcular_precio_seguro(self):
        precioBase = 200
        if self.conductor.puntos < 8: precioBase += 150
        if self.conductor.edad < 24: precioBase += 25
        if self.conductor.años_carnet < 2: precioBase += 50
        return precioBase