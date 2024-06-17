#Escribe un programa para solicitar al usuario tres números y mostrar enpantalla al menor de los tres

num1 = int(input("ingrese el primer numero\n"))
num2 = int(input("ingrese el segundo numero\n"))
num3 = int(input("ingrese el tercer numero\n"))
#si el primer numero ingresado pasa por todo el resto
if num1 > num2 or num1 > num3 :
    #lee si el numero 2 es mayor que el 3, si es verdadero el 3 es menor
    if num2 > num3:
        print("el tercer numero ingresado es el menor",num3)
        #el tercer numero es mayor que el segundo, el segundo es menor
    elif num3 > num2:
        print ("el segundo numero igresado es mmenor", num2)
  #el primer numero es menor que los otros 2
else:
    print ("el primer numero ingresado es el menor",num1)