from datetime import datetime
from abc import ABC, abstractmethod


# -----------------------------
# Clase abstracta
# -----------------------------
class NotaBase(ABC):

    def __init__(self, titulo, descripcion):
        self.titulo = titulo
        self.descripcion = descripcion
        self.fecha_creacion = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    @abstractmethod
    def mostrar(self):
        pass

    @abstractmethod
    def tipo(self):
        pass


# -----------------------------
# Nota Normal
# -----------------------------
class NotaNormal(NotaBase):

    COLORES_VALIDOS = {"amarillo", "verde", "blanco", "cyan"}

    def __init__(self, titulo, descripcion, color):
        if color not in NotaNormal.COLORES_VALIDOS:
            raise ValueError("Color no válido para nota normal")

        super().__init__(titulo, descripcion)
        self.color = color

    def mostrar(self):
        print(
            f"\n📝 NOTA NORMAL"
            f"\n📌 Título: {self.titulo}"
            f"\n🗒️ Descripción: {self.descripcion}"
            f"\n🎨 Color: {self.color}"
            f"\n🗓️ Fecha: {self.fecha_creacion}"
            f"\n{'-'*45}"
        )

    def tipo(self):
        return "normal"


# -----------------------------
# Nota Urgente
# -----------------------------
class NotaUrgente(NotaBase):

    def __init__(self, titulo, descripcion):
        super().__init__(titulo, descripcion)
        self.color = "rojo"

    def mostrar(self):
        print(
            f"\n❗❗ NOTA URGENTE ❗❗"
            f"\n🔥 TÍTULO: {self.titulo.upper()}"
            f"\n⚠️  DESCRIPCIÓN: {self.descripcion}"
            f"\n🎨 Color: {self.color}"
            f"\n🗓️ Fecha: {self.fecha_creacion}"
            f"\n{'='*45}"
        )

    def tipo(self):
        return "urgente"


# -----------------------------
# Gestor de notas
# -----------------------------
class GestorNotas:

    def __init__(self):
        self.notas = []

    def crear_nota_normal(self, titulo, descripcion, color):
        nota = NotaNormal(titulo, descripcion, color)
        self.notas.append(nota)
        print("✔️ Nota normal creada")

    def crear_nota_urgente(self, titulo, descripcion):
        nota = NotaUrgente(titulo, descripcion)
        self.notas.append(nota)
        print("🚨 Nota urgente creada")

    def eliminar_nota(self, titulo):
        for nota in self.notas:
            if nota.titulo == titulo:

                # Si es urgente → pedir confirmación
                if nota.tipo() == "urgente":
                    conf = input("⚠️ ¿Seguro que quieres eliminar esta nota urgente? (s/n): ")
                    if conf.lower() != "s":
                        print("❌ Eliminación cancelada")
                        return

                self.notas.remove(nota)
                print("🗑️ Nota eliminada correctamente")
                return

        print("❌ No existe una nota con ese título")

    def listar_notas(self):
        if not self.notas:
            print("📭 No hay notas")
            return

        # Urgentes primero
        urgentes = [n for n in self.notas if n.tipo() == "urgente"]
        normales = [n for n in self.notas if n.tipo() == "normal"]

        print("\n📋 LISTADO DE NOTAS")
        print("===============================")

        for n in urgentes + normales:
            n.mostrar()


# -----------------------------
# PRUEBAS
# -----------------------------

gestor = GestorNotas()

gestor.crear_nota_normal("Compra", "Comprar leche", "amarillo")
gestor.crear_nota_normal("Deberes", "Hacer ejercicios POO", "verde")
gestor.crear_nota_urgente("Examen", "Estudiar, es mañana")

gestor.listar_notas()

gestor.eliminar_nota("Examen")  # pedirá confirmación

gestor.listar_notas()
