segundos=int(input("De cuantos segundos hablamos: "))

if segundos%86400==0:
    dias=int(segundos/86400)
    print(segundos,"segundos son",dias,"dias")
else:
    segundos2=int(segundos%60)
    minutos=int(segundos/60)
    horas=int(minutos/60)
    dias=int(horas/24)
if minutos%60==0:
    minutos=0
    print(segundos,"segundos son",dias,"días,",horas,"horas,",minutos,"minutos y",segundos2,"segundos")