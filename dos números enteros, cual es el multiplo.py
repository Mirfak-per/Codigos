num1= int(input("ingrese el primer numero\n"))

num2= int(input("ingrese el segundo numero\n"))
# num1>num2 y viceversa lee cual numero es mayor, % lee si son pares entre 
#si, si lo son, quedan como multiplos de si, si no tira que no es multiplo
if num1 > num2 and num1 % num2 == 0:
 print ( num1, "es multiplo de", num2)
elif num1 > num2 and num1 % num2 != 0: 
    print ( num1, "no es multiplo de", num2)
    
#lo mismo que arriba pero ordena los numeros mayor a menor
elif num2> num1 and num2 % num1 == 0:
    print ( num2, "es multiplo de", num1)
elif num2 > num1 and num1 % num2 != 0: 
    print ( num2, "no es multiplo de", num1)