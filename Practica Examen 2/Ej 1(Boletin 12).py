from datetime import datetime

class Nota:
    COLORES_VALIDOS = {"amarillo", "verde", "blanco", "cyan"}

    def __init__(self,titulo, descripcion,color):
        if color not in Nota.COLORES_VALIDOS:
            raise ValueError(f"Color inválido: {color}. Debe ser uno de {Nota.COLORES_VALIDOS}")

        self.titulo = titulo
        self.descripcion = descripcion
        self.color = color
        self.fecha_creacion = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    def __str__(self):
        return (
            f"Título: {self.titulo}\n"
            f"Descripción: {self.descripcion}\n"
            f"Color: {self.color}\n"
            f"Fecha de creación: {self.fecha_creacion}\n"
            f"{'-' * 40}"
        )


class GestorNotas:
    def __init__(self):
        self.notas = []

    def crear_nota(self, titulo, descripcion, color):
        nota = Nota(titulo, descripcion, color)
        self.notas.append(nota)
        print(f"Nota creada correctamente: '{titulo}'")

    def eliminar_nota(self, titulo):
        for nota in self.notas:
            if nota.titulo == titulo:
                self.notas.remove(nota)
                print(f"Nota eliminada: '{titulo}'")
                return
        print(f"No existe ninguna nota con título '{titulo}'")

    def listar_notas(self):
        if not self.notas:
            print("No hay notas guardadas aún.")
            return

        print("LISTADO DE NOTAS")
        print("=" * 40)
        for nota in self.notas:
            print(nota)


gestor = GestorNotas()

# Crear notas
gestor.crear_nota("Compra", "Comprar leche, pan y huevos", "amarillo")
gestor.crear_nota("Estudiar", "Repasar Python y POO", "verde")
gestor.crear_nota("Ideas", "Pensar proyecto nuevo", "cyan")

# Listar notas
gestor.listar_notas()

# Eliminar una nota
gestor.eliminar_nota("Estudiar")

# Listar otra vez
gestor.listar_notas()
