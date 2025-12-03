def divisoresComunes(num1,num2):
    divisores=[]
    try:
        mayor=0
        if num1>mayor:
            mayor=num1
        else:
            mayor=num2
        for n in range(1,mayor+1):
            if(num1%n == 0 and num2%n==0):
                divisores.append(str(n))

        assert num1 > 0, "No puedo calcualr los divisores comunes de esos números"
        assert num2 > 0, "No puedo calcualr los divisores comunes de esos números"
        return divisores
    except ZeroDivisionError:
        print("No puedo calcualr los divisores comunes de esos números")
    except:
        print("No puedo calcualr los divisores comunes de esos números")

num1=1725
num2=2500
divisores=str(divisoresComunes(num1,num2)).replace("'","").replace("[","").replace("]","")
if(len(divisores)==1):
    print("Los divisores comunes de", num1, "y", num2, "es:", divisores)
else:
    print("Los divisores comunes de",num1,"y",num2,"son:",divisores)