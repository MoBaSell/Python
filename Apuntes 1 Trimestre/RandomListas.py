import random
alumnos = ["Alvaro","Eva","Sara","Fernando","Juan"]
print(random.choice(alumnos)) #elige un elemento al azar
print(random.sample(alumnos,4)) #elige un numero elementos sin repetir
random.shuffle(alumnos) #desordena aleatoriamente la lista / modifica la original
print(alumnos)
