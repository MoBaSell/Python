import random

dado1=0
dado2=1
tiradas=0
while dado1 != dado2:
    dado1 = random.randint(1,6)
    dado2 = random.randint(1,6)
    print("Dado 1:", dado1, "Dado 2:", dado2)
    tiradas+=1

