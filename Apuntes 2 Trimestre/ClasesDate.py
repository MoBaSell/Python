from datetime import date, time, datetime, timedelta

#fecha
hoy= date.today()
print(hoy)

#poner datos personalizados
cumpleanyos=date(2003,11,20)
citaMedica=datetime(2025,12,15,10,11)
despertador=time(6,12) #Si lo dejamos vacio lo inicia en 0
print(cumpleanyos)
print(citaMedica)
print(despertador)

#hora, pero sale con la fecha
ahora = datetime.now()
print(ahora)
#para darle formato
formateado1=ahora.strftime("%H:%M") #La H es la hora, M los minutos, si ponemos un - delante(-H/-M) elimina los 0
formateado2=ahora.strftime("%d/%m/%y - %H:%M:%S")#Si ponemos el y en mayuscula nos muestra las 4 cifras(2025)
formateado3=ahora.strftime("(%w)(%W) %a %d/%b/%y (%j)- %I:%M:%S %p")
#Si ponemos a nos da el dia en texto, b para mes en texto, I para formato de hora en 12h, p para franja horaria, w indica el dia de la semana,
#W numero de la semana/U para contar desde el primer lunes del año, j para dia del año
#A la %A y %B los pone completos
print(formateado1)
print(formateado2)
print(formateado3)

#formateo automatico
formateado4=ahora.strftime("%c")
print(formateado4)

formateado4=ahora.strftime("%x")
print(formateado4)

formateado4=ahora.strftime("%X")
print(formateado4)

cadena="01-03-2025 14:30"
fecha = datetime.strptime(cadena,"%d-%m-%Y %H:%M") #strptime para pasar de cadena a objeto/ strftime de objeto a cadena
print(fecha)

#para elementos individuales
print(fecha.hour)
print(fecha.year)
print(ahora.microsecond)

#comparar
if ahora>citaMedica: #importante comparar objetos del mismo tipo
    print("La fecha de ahora es posterior a tu cita medica")
else:
    print("La fecha de ahora anterior a tu cita medica")

#para hacer operaciones
print(ahora)
nuevaFecha=ahora+timedelta(days=10,hours=2,weeks=1)
print(nuevaFecha)
