numero=4
match numero:
    case 2:
        print("El numero es el 2")
    case 3 | 4:
        print("El numero es el 3 o el 4")
    case _:
        print("No es ni 2 ni 3")
print("FIN")

opcion=""
while opcion!="X" and opcion!="x":
    opcion = input("Introduce una letra")
    match opcion:
        case "P" | "p" | "J" | "j":
            print("Jugar")
        case "C" | "c":
            print("Configurar")
        case "X" | "x":
            print("Salir")
        case _:
            print("Operación no reconocida")
print("FIN")