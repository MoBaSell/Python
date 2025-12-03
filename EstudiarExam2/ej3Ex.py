def validar(*datos):
    validas = 0
    no_validas = 0

    for matricula in datos:
        matriculaLimpia = matricula.upper().replace(" ", "").replace("-", "")

        if len(matriculaLimpia) != 7:
            print(matricula, "no es valida")
            no_validas += 1
            
        numeros = matriculaLimpia[:4]
        letras = matriculaLimpia[4:]

        if numeros.isdigit() and letras.isalpha():
            valida = True  # asumimos que es válida
            for n in letras:
                if n in "AEIOUQÑ":  # si encuentra una letra prohibida
                    valida = False
                # no usamos break, pero la bandera se queda en False

            # Al salir del for:
            if valida:
                print(matricula, "es valida")
                validas += 1
            else:
                print(matricula, "no es valida")
                no_validas += 1
        else:
            print(matricula, "no es valida")
            no_validas += 1

    print("Matriculas válidas:", validas)
    print("Matriculas no válidas:", no_validas)


validar("22CDR", "7521-MXP", "1224MN")
