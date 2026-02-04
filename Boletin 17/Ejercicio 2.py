
fichero = open("estadisticas.txt","rt")

texto = fichero.readlines()

hombres=0
mujeres=0
alturas=0
contador=0

for linea in texto:
    # .strip() elimina espacios y el salto de línea '\n'
    limpio = linea.strip()

    if limpio == "Hombre":
        hombres+=1
    elif limpio == "Mujer":
        mujeres+=1
    elif limpio!="":
        alturas+=float(limpio)
        contador=contador+1

media = alturas/contador

print(f"Hombres: {hombres}")
print(f"Mujeres: {mujeres}")
print(f"Estatura media: {media:.2f}")