exepciones=True
while exepciones==True:
    try:
        numero=int(input("Introduce un número: "))
        resultado=10/numero
        print(resultado)
        #if numero < 0:
        #    raise Exception("No es un entero positivo") #nos permite generar la excepcion que queramos
        assert numero>=0,"No admito números negativos" #lo mismo que raise pero de forma automatica / se ejecuta solo si es False
    except ZeroDivisionError:
      print("No se puede dividir entre cero")
    except ValueError:
      print("No has metido un entero")
    except:
     print("Excepcion, pero otra")
    else: #se ejecuta en caso de que no haya ninguna excepcion
        print("Todo bien")
        exepciones=False
    finally: #se ejecuta en ambos casos
       print("seguimos adelante...")

print("Programa finalizado")
