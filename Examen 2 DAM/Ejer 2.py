class Tarea:

    def __init__(self,ID,titulo,prioridad):
        self.ID = ID
        self.titulo = titulo
        self.prioridad = prioridad
        self.realizada = False

tareas = {}

def agregarTarea(ID,titulo,prioridad):
    if ID in tareas:
        print(f"Error: ID {ID} ya existente")
    else:
        tareas[ID] = Tarea(ID,titulo,prioridad)
        print(f"Tarea '{titulo}' (ID: {ID}) añadida.")

def eliminarTarea(ID):
    if ID in tareas:
        print(f"Tarea con ID {ID} ('{tareas[ID].titulo}') eliminada")
        del tareas[ID]
    else:
        print(f"Error: No se encontró una tarea con ID {ID}")

def marcarComoCompletada(ID):
    if ID in tareas:
        tareas[ID].realizada = True
        print(f"Tarea ID {ID} '{tareas[ID].titulo}' marcada como completada")
    else:
        print(f"Error: No se encontró una tarea con ID {ID}")

def mostrarTareasCompletadas():
    cont=0
    print("- LISTADO DE TAREAS:")
    for ID in tareas:
        if tareas[ID].realizada:
            cont+=1
            print(f"[{ID}] {tareas[ID].titulo} (Prioridad: {tareas[ID].prioridad})")
    if cont==0:
        print("No hay tareas no completadas")

def mostrarTareasNoCompletadas():
    cont = 0
    print("- LISTADO DE TAREAS:")
    for ID in tareas:
        if tareas[ID].realizada==False:
            cont += 1
            print(f"[{ID}] {tareas[ID].titulo} (Prioridad: {tareas[ID].prioridad})")
    if cont == 0:
        print("No hay tareas completadas")

agregarTarea("55","ducharse",5)

mostrarTareasNoCompletadas()


